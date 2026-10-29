import threading
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from types import SimpleNamespace

import httpx
import pytest

from qca import Forward, Managed
from qca.common._streaming import Stream


@contextmanager
def local_server(*, hanging):
    release = threading.Event()
    requests = []

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def do_GET(self):
            requests.append((self.path, self.client_address))
            sse = self.path.endswith("/stream")
            body = b'data: {"type":"agent.message"}\n\n' if sse else b'{"data":[],"has_more":false}'
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream" if sse else "application/json")
            if sse and hanging:
                self.send_header("Transfer-Encoding", "chunked")
                self.end_headers()
                self.wfile.flush()
                release.wait(timeout=10)
                self.close_connection = True
            else:
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                self.wfile.flush()

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}", requests, release
    finally:
        release.set()
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
        assert not thread.is_alive()


@pytest.mark.parametrize("mode", ["forward", "managed"])
@pytest.mark.parametrize("scope", ["session", "thread"])
def test_sync_close_wakes_real_http_read_without_reconnecting(mode, scope):
    reading = threading.Event()

    def trace(event, info):
        if event == "http11.receive_response_body.started":
            reading.set()

    def request_hook(request):
        request.extensions["trace"] = trace

    with local_server(hanging=True) as (base_url, requests, release):
        http_client = httpx.Client(trust_env=False, event_hooks={"request": [request_hook]})
        client = (Forward if mode == "forward" else Managed)(
            pat="test", base_url=base_url, http_client=http_client, timeout=3, max_retries=0
        )
        stream = (
            client.sessions.events.resumable_stream("session")
            if scope == "session"
            else client.sessions.threads.events.resumable_stream("thread", session_id="session")
        )
        executor = ThreadPoolExecutor(max_workers=1)
        pending = executor.submit(next, stream)
        try:
            assert reading.wait(timeout=2)
            with pytest.raises(TimeoutError):
                pending.result(timeout=0.1)
            stream.close()
            stream.close()
            with pytest.raises(StopIteration):
                pending.result(timeout=1)
            # A cancelled SSE connection must not poison or close the shared client.
            assert client.models.list().data == []
            assert len([path for path, _ in requests if path.endswith("/stream")]) == 1
        finally:
            release.set()
            stream.close()
            executor.shutdown(wait=True)
            client.close()


def test_fully_consumed_stream_can_reuse_connection_after_repeated_close():
    with local_server(hanging=False) as (base_url, requests, _):
        with httpx.Client(base_url=base_url, trust_env=False) as client:
            response = client.send(client.build_request("GET", "/stream"), stream=True)
            stream = Stream(response, dict)
            assert list(stream) == [{"type": "agent.message"}]
            stream.close()
            assert client.get("/models").status_code == 200
            stream.close()
            assert client.get("/models").status_code == 200
            assert len({address for _, address in requests}) == 1


@pytest.mark.parametrize("version", [b"HTTP/2", None])
def test_close_does_not_inspect_shared_or_unknown_protocol_socket(version):
    def get_extra_info(name):
        pytest.fail("must not access a shared or unknown protocol socket")

    response = httpx.Response(
        200,
        stream=httpx.ByteStream(b""),
        extensions={"http_version": version, "network_stream": SimpleNamespace(get_extra_info=get_extra_info)},
    )
    Stream(response, dict).close()
    assert response.is_closed


@pytest.mark.parametrize("unsupported", [None, OSError, NotImplementedError])
def test_custom_transport_without_socket_still_closes(unsupported):
    def get_extra_info(name):
        if unsupported:
            raise unsupported("socket metadata is unavailable")
        return None

    response = httpx.Response(
        200,
        stream=httpx.ByteStream(b""),
        extensions={"http_version": b"HTTP/1.1", "network_stream": SimpleNamespace(get_extra_info=get_extra_info)},
    )
    Stream(response, dict).close()
    assert response.is_closed
