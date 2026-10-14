"""Drive Beta: upload, page through a directory, download and delete a file.

Run: python -m examples.forward.drive
Uses the shared PAT / SA example configuration and a new, isolated Identity.
"""

from __future__ import annotations

import httpx

from examples.common.live import Run, name, run_cli
from qca import Forward


def run(client: Forward, context: Run) -> None:
    identity = client.identities.create(external_id=name("drive-identity"))
    context.track("identity", identity.id, lambda: client.identities.delete(identity.id))
    path = "sdk-example/说明.txt"
    context.track(
        "drive directory",
        "sdk-example",
        lambda: client.drives.delete_entry(identity_id=identity.id, path="sdk-example", recursive=True),
    )
    # A separate HTTP client sends only storage headers, never the QCA credential.
    with httpx.Client(timeout=30, follow_redirects=False) as storage:
        signed = client.drives.create_upload_url(identity_id=identity.id, path=path, content_type="text/plain")
        try:
            uploaded = storage.request(
                signed.method, signed.url, headers=signed.headers, content=b"Hello from QCA Drive"
            )
        except httpx.HTTPError:
            raise RuntimeError("Storage upload failed") from None
        if not uploaded.is_success:
            raise RuntimeError(f"Storage upload HTTP {uploaded.status_code}")
        cursor = None
        while True:
            page = client.drives.list_entries(
                identity_id=identity.id,
                path="sdk-example",
                limit=20,
                **({"page_token": cursor} if cursor else {}),
            )
            for entry in page.entries:
                context.output("drive_entry", {"path": entry.path, "type": entry.type, "size": entry.size})
            cursor = page.next_page_token
            if not cursor:
                break
        signed = client.drives.create_download_url(identity_id=identity.id, path=path)
        try:
            downloaded = storage.request(signed.method, signed.url, headers=signed.headers)
        except httpx.HTTPError:
            raise RuntimeError("Storage download failed") from None
        if not downloaded.is_success:
            raise RuntimeError(f"Storage download HTTP {downloaded.status_code}")
        context.output("download", downloaded.text)
    deleted = client.drives.delete_entry(identity_id=identity.id, path=path)
    context.output("deleted_count", deleted.deleted_count)


if __name__ == "__main__":
    run_cli("forward", Forward, {"drive": run})
