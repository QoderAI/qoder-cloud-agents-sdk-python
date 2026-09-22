<a id="qca.common._base_client"></a>

# qca.common.\_base\_client

<a id="qca.common._base_client.DEFAULT_TIMEOUT"></a>

#### DEFAULT\_TIMEOUT

<a id="qca.common._base_client.BaseClient"></a>

## BaseClient

```python
class BaseClient()
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.BaseClient.with_options"></a>

#### with\_options

```python
def with_options(
        *,
        pat: str | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | NotGiven = NOT_GIVEN,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | NotGiven = NOT_GIVEN,
        default_query: Mapping[str, Any] | NotGiven = NOT_GIVEN) -> Self
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.BaseClient.is_closed"></a>

#### is\_closed

```python
def is_closed() -> bool
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.SyncAPIClient"></a>

## SyncAPIClient

```python
class SyncAPIClient(BaseClient)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.SyncAPIClient.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*,
             pat: str | None = None,
             base_url: str | httpx.URL | None = None,
             timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
             max_retries: int = 2,
             default_headers: Mapping[str, str] | None = None,
             default_query: Mapping[str, Any] | None = None,
             http_client: httpx.Client | None = None,
             credential: Credential | None = None) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.SyncAPIClient.request"></a>

#### request

```python
def request(method: str,
            path: str,
            *,
            cast_to: Any,
            options: dict[str, Any],
            page_style: str | None = None,
            stream: bool = False,
            binary: bool = False,
            download_link: bool = False,
            file_fields: list[str] | None = None) -> Any
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.SyncAPIClient.close"></a>

#### close

```python
def close() -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.SyncAPIClient.__enter__"></a>

#### \_\_enter\_\_

```python
def __enter__() -> Self
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.SyncAPIClient.__exit__"></a>

#### \_\_exit\_\_

```python
def __exit__(*_: object) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.AsyncAPIClient"></a>

## AsyncAPIClient

```python
class AsyncAPIClient(BaseClient)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.AsyncAPIClient.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*,
             pat: str | None = None,
             base_url: str | httpx.URL | None = None,
             timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
             max_retries: int = 2,
             default_headers: Mapping[str, str] | None = None,
             default_query: Mapping[str, Any] | None = None,
             http_client: httpx.AsyncClient | None = None,
             credential: Credential | AsyncCredential | None = None) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.AsyncAPIClient.request"></a>

#### request

```python
async def request(method: str,
                  path: str,
                  *,
                  cast_to: Any,
                  options: dict[str, Any],
                  page_style: str | None = None,
                  stream: bool = False,
                  binary: bool = False,
                  download_link: bool = False,
                  file_fields: list[str] | None = None) -> Any
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.AsyncAPIClient.close"></a>

#### close

```python
async def close() -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.AsyncAPIClient.__aenter__"></a>

#### \_\_aenter\_\_

```python
async def __aenter__() -> Self
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._base_client.AsyncAPIClient.__aexit__"></a>

#### \_\_aexit\_\_

```python
async def __aexit__(*_: object) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_base_client.py)

<a id="qca.common._exceptions"></a>

# qca.common.\_exceptions

<a id="qca.common._exceptions.APIError"></a>

## APIError

```python
class APIError(Exception)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.APIError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str,
             *,
             request: httpx.Request,
             body: Any = None) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.APIConnectionError"></a>

## APIConnectionError

```python
class APIConnectionError(APIError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.APIConnectionError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*,
             request: httpx.Request,
             message: str = "Connection error.") -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.APITimeoutError"></a>

## APITimeoutError

```python
class APITimeoutError(APIConnectionError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.APITimeoutError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*, request: httpx.Request) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.APIResponseValidationError"></a>

## APIResponseValidationError

```python
class APIResponseValidationError(APIError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.APIResponseValidationError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*, response: httpx.Response, body: Any) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.APIStatusError"></a>

## APIStatusError

```python
class APIStatusError(APIError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.APIStatusError.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str, *, response: httpx.Response, body: Any) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.BadRequestError"></a>

## BadRequestError

```python
class BadRequestError(APIStatusError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.AuthenticationError"></a>

## AuthenticationError

```python
class AuthenticationError(APIStatusError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.PermissionDeniedError"></a>

## PermissionDeniedError

```python
class PermissionDeniedError(APIStatusError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.NotFoundError"></a>

## NotFoundError

```python
class NotFoundError(APIStatusError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.ConflictError"></a>

## ConflictError

```python
class ConflictError(APIStatusError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.UnprocessableEntityError"></a>

## UnprocessableEntityError

```python
class UnprocessableEntityError(APIStatusError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.RateLimitError"></a>

## RateLimitError

```python
class RateLimitError(APIStatusError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.InternalServerError"></a>

## InternalServerError

```python
class InternalServerError(APIStatusError)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._exceptions.status_error"></a>

#### status\_error

```python
def status_error(response: httpx.Response) -> APIStatusError
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_exceptions.py)

<a id="qca.common._files"></a>

# qca.common.\_files

<a id="qca.common._files.file_tuple"></a>

#### file\_tuple

```python
def file_tuple(value: Any) -> tuple[Any, ...]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_files.py)

<a id="qca.common._files.multipart_parts"></a>

#### multipart\_parts

```python
def multipart_parts(body: dict[str, Any],
                    file_fields: list[str]) -> list[tuple[str, Any]]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_files.py)

<a id="qca.common._models"></a>

# qca.common.\_models

<a id="qca.common._models.BaseModel"></a>

## BaseModel

```python
class BaseModel(PydanticBaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_models.py)

<a id="qca.common._models.BaseModel.model_config"></a>

#### model\_config

<a id="qca.common._models.BaseModel.to_dict"></a>

#### to\_dict

```python
def to_dict(*,
            mode: str = "python",
            use_api_names: bool = True,
            exclude_unset: bool = True) -> dict[str, Any]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_models.py)

<a id="qca.common._models.BaseModel.to_json"></a>

#### to\_json

```python
def to_json(*,
            indent: int | None = 2,
            use_api_names: bool = True,
            exclude_unset: bool = True) -> str
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_models.py)

<a id="qca.common._models.parse_response"></a>

#### parse\_response

```python
def parse_response(cast_to: Any, data: Any, response: Any) -> Any
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_models.py)

<a id="qca.common._platform"></a>

# qca.common.\_platform

<a id="qca.common._platform.platform_headers"></a>

#### platform\_headers

```python
def platform_headers() -> dict[str, str]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_platform.py)

<a id="qca.common._resource"></a>

# qca.common.\_resource

<a id="qca.common._resource.SyncAPIResource"></a>

## SyncAPIResource

```python
class SyncAPIResource()
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resource.py)

<a id="qca.common._resource.SyncAPIResource.__init__"></a>

#### \_\_init\_\_

```python
def __init__(client: SyncAPIClient) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resource.py)

<a id="qca.common._resource.SyncAPIResource.with_raw_response"></a>

#### with\_raw\_response

```python
@cached_property
def with_raw_response() -> RawResponseResource
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resource.py)

<a id="qca.common._resource.SyncAPIResource.with_streaming_response"></a>

#### with\_streaming\_response

```python
@cached_property
def with_streaming_response() -> RawResponseResource
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resource.py)

<a id="qca.common._resource.AsyncAPIResource"></a>

## AsyncAPIResource

```python
class AsyncAPIResource()
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resource.py)

<a id="qca.common._resource.AsyncAPIResource.__init__"></a>

#### \_\_init\_\_

```python
def __init__(client: AsyncAPIClient) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resource.py)

<a id="qca.common._resource.AsyncAPIResource.with_raw_response"></a>

#### with\_raw\_response

```python
@cached_property
def with_raw_response() -> RawResponseResource
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resource.py)

<a id="qca.common._resource.AsyncAPIResource.with_streaming_response"></a>

#### with\_streaming\_response

```python
@cached_property
def with_streaming_response() -> RawResponseResource
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resource.py)

<a id="qca.common._response"></a>

# qca.common.\_response

<a id="qca.common._response.T"></a>

#### T

<a id="qca.common._response.read_response"></a>

#### read\_response

```python
def read_response(response: httpx.Response) -> bytes
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.aread_response"></a>

#### aread\_response

```python
async def aread_response(response: httpx.Response) -> bytes
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.APIResponse"></a>

## APIResponse

```python
class APIResponse(Generic[T])
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.APIResponse.__init__"></a>

#### \_\_init\_\_

```python
def __init__(response: httpx.Response, parse: Callable[[], T]) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.APIResponse.headers"></a>

#### headers

```python
@property
def headers() -> httpx.Headers
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.APIResponse.status_code"></a>

#### status\_code

```python
@property
def status_code() -> int
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.APIResponse.parse"></a>

#### parse

```python
def parse() -> T
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.APIResponse.read"></a>

#### read

```python
def read() -> bytes
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.APIResponse.iter_bytes"></a>

#### iter\_bytes

```python
def iter_bytes(chunk_size: int | None = None) -> Iterator[bytes]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.APIResponse.iter_lines"></a>

#### iter\_lines

```python
def iter_lines() -> Iterator[str]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.APIResponse.close"></a>

#### close

```python
def close() -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncAPIResponse"></a>

## AsyncAPIResponse

```python
class AsyncAPIResponse(Generic[T])
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncAPIResponse.__init__"></a>

#### \_\_init\_\_

```python
def __init__(response: httpx.Response, parse: Callable[[], T]) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncAPIResponse.headers"></a>

#### headers

```python
@property
def headers() -> httpx.Headers
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncAPIResponse.status_code"></a>

#### status\_code

```python
@property
def status_code() -> int
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncAPIResponse.parse"></a>

#### parse

```python
async def parse() -> T
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncAPIResponse.read"></a>

#### read

```python
async def read() -> bytes
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncAPIResponse.iter_bytes"></a>

#### iter\_bytes

```python
async def iter_bytes(chunk_size: int | None = None) -> AsyncIterator[bytes]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncAPIResponse.iter_lines"></a>

#### iter\_lines

```python
async def iter_lines() -> AsyncIterator[str]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncAPIResponse.close"></a>

#### close

```python
async def close() -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.BinaryAPIResponse"></a>

## BinaryAPIResponse

```python
class BinaryAPIResponse()
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

A streaming download. Close it explicitly or use a context manager.

<a id="qca.common._response.BinaryAPIResponse.__init__"></a>

#### \_\_init\_\_

```python
def __init__(response: httpx.Response) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.BinaryAPIResponse.headers"></a>

#### headers

```python
@property
def headers() -> httpx.Headers
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.BinaryAPIResponse.status_code"></a>

#### status\_code

```python
@property
def status_code() -> int
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.BinaryAPIResponse.read"></a>

#### read

```python
def read() -> bytes
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.BinaryAPIResponse.iter_bytes"></a>

#### iter\_bytes

```python
def iter_bytes(chunk_size: int | None = None) -> Iterator[bytes]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.BinaryAPIResponse.write_to_file"></a>

#### write\_to\_file

```python
def write_to_file(path: str | Path) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.BinaryAPIResponse.close"></a>

#### close

```python
def close() -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.BinaryAPIResponse.__enter__"></a>

#### \_\_enter\_\_

```python
def __enter__() -> BinaryAPIResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.BinaryAPIResponse.__exit__"></a>

#### \_\_exit\_\_

```python
def __exit__(*_: object) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncBinaryAPIResponse"></a>

## AsyncBinaryAPIResponse

```python
class AsyncBinaryAPIResponse()
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncBinaryAPIResponse.__init__"></a>

#### \_\_init\_\_

```python
def __init__(response: httpx.Response) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncBinaryAPIResponse.headers"></a>

#### headers

```python
@property
def headers() -> httpx.Headers
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncBinaryAPIResponse.status_code"></a>

#### status\_code

```python
@property
def status_code() -> int
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncBinaryAPIResponse.read"></a>

#### read

```python
async def read() -> bytes
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncBinaryAPIResponse.iter_bytes"></a>

#### iter\_bytes

```python
async def iter_bytes(chunk_size: int | None = None) -> AsyncIterator[bytes]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncBinaryAPIResponse.write_to_file"></a>

#### write\_to\_file

```python
async def write_to_file(path: str | Path) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncBinaryAPIResponse.close"></a>

#### close

```python
async def close() -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncBinaryAPIResponse.__aenter__"></a>

#### \_\_aenter\_\_

```python
async def __aenter__() -> AsyncBinaryAPIResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncBinaryAPIResponse.__aexit__"></a>

#### \_\_aexit\_\_

```python
async def __aexit__(*_: object) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.RawResponseResource"></a>

## RawResponseResource

```python
class RawResponseResource()
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.RawResponseResource.__init__"></a>

#### \_\_init\_\_

```python
def __init__(resource: Any, *, streaming: bool = False) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.RawResponseResource.__getattr__"></a>

#### \_\_getattr\_\_

```python
def __getattr__(name: str) -> Any
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.ResponseContextManager"></a>

## ResponseContextManager

```python
class ResponseContextManager()
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.ResponseContextManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(request: Callable[[], Any]) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.ResponseContextManager.__enter__"></a>

#### \_\_enter\_\_

```python
def __enter__() -> Any
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.ResponseContextManager.__exit__"></a>

#### \_\_exit\_\_

```python
def __exit__(*_: object) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncResponseContextManager"></a>

## AsyncResponseContextManager

```python
class AsyncResponseContextManager()
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncResponseContextManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(request: Callable[[], Any]) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncResponseContextManager.__aenter__"></a>

#### \_\_aenter\_\_

```python
async def __aenter__() -> Any
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._response.AsyncResponseContextManager.__aexit__"></a>

#### \_\_aexit\_\_

```python
async def __aexit__(*_: object) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_response.py)

<a id="qca.common._resumable_streaming"></a>

# qca.common.\_resumable\_streaming

<a id="qca.common._resumable_streaming.T"></a>

#### T

<a id="qca.common._resumable_streaming.Retryable"></a>

#### Retryable

<a id="qca.common._resumable_streaming.ResumableStream"></a>

## ResumableStream

```python
class ResumableStream(Generic[T], Iterator[T])
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.ResumableStream.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*, open_stream: Callable[[str | None], Stream[T]],
             retryable: Retryable, last_event_id: str | None) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.ResumableStream.last_event_id"></a>

#### last\_event\_id

```python
@property
def last_event_id() -> str | None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.ResumableStream.__next__"></a>

#### \_\_next\_\_

```python
def __next__() -> T
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.ResumableStream.close"></a>

#### close

```python
def close() -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.ResumableStream.__enter__"></a>

#### \_\_enter\_\_

```python
def __enter__() -> ResumableStream[T]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.ResumableStream.__exit__"></a>

#### \_\_exit\_\_

```python
def __exit__(*_: object) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.AsyncResumableStream"></a>

## AsyncResumableStream

```python
class AsyncResumableStream(Generic[T], AsyncIterator[T])
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.AsyncResumableStream.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*, open_stream: Callable[[str | None], Awaitable[AsyncStream[T]]],
             retryable: Retryable, last_event_id: str | None) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.AsyncResumableStream.last_event_id"></a>

#### last\_event\_id

```python
@property
def last_event_id() -> str | None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.AsyncResumableStream.__anext__"></a>

#### \_\_anext\_\_

```python
async def __anext__() -> T
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.AsyncResumableStream.close"></a>

#### close

```python
async def close() -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.AsyncResumableStream.__aenter__"></a>

#### \_\_aenter\_\_

```python
async def __aenter__() -> AsyncResumableStream[T]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._resumable_streaming.AsyncResumableStream.__aexit__"></a>

#### \_\_aexit\_\_

```python
async def __aexit__(*_: object) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_resumable_streaming.py)

<a id="qca.common._streaming"></a>

# qca.common.\_streaming

<a id="qca.common._streaming.T"></a>

#### T

<a id="qca.common._streaming.SSEDecoder"></a>

## SSEDecoder

```python
class SSEDecoder()
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.SSEDecoder.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.SSEDecoder.decode"></a>

#### decode

```python
def decode(line: str) -> tuple[str | None, str] | None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.BaseStream"></a>

## BaseStream

```python
class BaseStream(Generic[T])
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.BaseStream.__init__"></a>

#### \_\_init\_\_

```python
def __init__(response: httpx.Response, cast_to: Any) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.BaseStream.last_event_id"></a>

#### last\_event\_id

```python
@property
def last_event_id() -> str | None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.Stream"></a>

## Stream

```python
class Stream(BaseStream[T], Iterator[T])
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.Stream.__init__"></a>

#### \_\_init\_\_

```python
def __init__(response: httpx.Response, cast_to: Any) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.Stream.__next__"></a>

#### \_\_next\_\_

```python
def __next__() -> T
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.Stream.close"></a>

#### close

```python
def close() -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.Stream.__enter__"></a>

#### \_\_enter\_\_

```python
def __enter__() -> Stream[T]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.Stream.__exit__"></a>

#### \_\_exit\_\_

```python
def __exit__(*_: object) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.AsyncStream"></a>

## AsyncStream

```python
class AsyncStream(BaseStream[T], AsyncIterator[T])
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.AsyncStream.__init__"></a>

#### \_\_init\_\_

```python
def __init__(response: httpx.Response, cast_to: Any) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.AsyncStream.__anext__"></a>

#### \_\_anext\_\_

```python
async def __anext__() -> T
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.AsyncStream.close"></a>

#### close

```python
async def close() -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.AsyncStream.__aenter__"></a>

#### \_\_aenter\_\_

```python
async def __aenter__() -> AsyncStream[T]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._streaming.AsyncStream.__aexit__"></a>

#### \_\_aexit\_\_

```python
async def __aexit__(*_: object) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_streaming.py)

<a id="qca.common._types"></a>

# qca.common.\_types

<a id="qca.common._types.NotGiven"></a>

## NotGiven

```python
class NotGiven()
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_types.py)

A missing argument, distinct from an explicitly supplied None.

<a id="qca.common._types.NotGiven.__bool__"></a>

#### \_\_bool\_\_

```python
def __bool__() -> bool
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_types.py)

<a id="qca.common._types.NotGiven.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_types.py)

<a id="qca.common._types.NOT_GIVEN"></a>

#### NOT\_GIVEN

<a id="qca.common._types.FileContent"></a>

#### FileContent

<a id="qca.common._types.FileTypes"></a>

#### FileTypes

<a id="qca.common._types.Body"></a>

#### Body

<a id="qca.common._utils"></a>

# qca.common.\_utils

<a id="qca.common._utils.strip_not_given"></a>

#### strip\_not\_given

```python
def strip_not_given(value: Any) -> Any
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_utils.py)

<a id="qca.common._utils.path_template"></a>

#### path\_template

```python
def path_template(path: str, **params: str) -> str
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_utils.py)

<a id="qca.common._utils.make_request_options"></a>

#### make\_request\_options

```python
def make_request_options(*,
                         body: Mapping[str, Any],
                         query: Mapping[str, Any],
                         headers: Mapping[str, Any],
                         extra_headers: Mapping[str, str] | None,
                         extra_query: Mapping[str, Any] | None,
                         extra_body: Mapping[str, Any] | None,
                         timeout: Any = NOT_GIVEN) -> dict[str, Any]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_utils.py)

<a id="qca.common._utils.query_pairs"></a>

#### query\_pairs

```python
def query_pairs(query: Mapping[str, Any]) -> list[tuple[str, str]]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/_utils.py)

<a id="qca.common.credentials"></a>

# qca.common.credentials

<a id="qca.common.credentials.Credential"></a>

## Credential

```python
class Credential(Protocol)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/credentials.py)

<a id="qca.common.credentials.Credential.get_token"></a>

#### get\_token

```python
def get_token() -> str
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/credentials.py)

Return the current access token. Called for each HTTP attempt.

<a id="qca.common.credentials.AsyncCredential"></a>

## AsyncCredential

```python
class AsyncCredential(Protocol)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/credentials.py)

<a id="qca.common.credentials.AsyncCredential.get_token"></a>

#### get\_token

```python
async def get_token() -> str
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/credentials.py)

<a id="qca.common.pagination"></a>

# qca.common.pagination

<a id="qca.common.pagination.T"></a>

#### T

<a id="qca.common.pagination.BasePage"></a>

## BasePage

```python
class BasePage(BaseModel, Generic[T])
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.BasePage.data"></a>

#### data

<a id="qca.common.pagination.BasePage.has_more"></a>

#### has\_more

<a id="qca.common.pagination.BasePage.first_id"></a>

#### first\_id

<a id="qca.common.pagination.BasePage.last_id"></a>

#### last\_id

<a id="qca.common.pagination.BasePage.next_page"></a>

#### next\_page

<a id="qca.common.pagination.BasePage.has_next_page"></a>

#### has\_next\_page

```python
def has_next_page() -> bool
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.SyncPage"></a>

## SyncPage

```python
class SyncPage(BasePage[T])
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.SyncPage.get_next_page"></a>

#### get\_next\_page

```python
def get_next_page() -> SyncPage[T]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.SyncPage.iter_pages"></a>

#### iter\_pages

```python
def iter_pages() -> Iterator[SyncPage[T]]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.SyncPage.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__() -> Iterator[T]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.AsyncPage"></a>

## AsyncPage

```python
class AsyncPage(BasePage[T])
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.AsyncPage.get_next_page"></a>

#### get\_next\_page

```python
async def get_next_page() -> AsyncPage[T]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.AsyncPage.iter_pages"></a>

#### iter\_pages

```python
async def iter_pages() -> AsyncIterator[AsyncPage[T]]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.AsyncPage.__aiter__"></a>

#### \_\_aiter\_\_

```python
async def __aiter__() -> AsyncIterator[T]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.AsyncPaginator"></a>

## AsyncPaginator

```python
class AsyncPaginator(Generic[T])
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

Await the first page, or iterate items directly with async for.

<a id="qca.common.pagination.AsyncPaginator.__init__"></a>

#### \_\_init\_\_

```python
def __init__(fetch: Callable[[], Awaitable[AsyncPage[T]]]) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.AsyncPaginator.__await__"></a>

#### \_\_await\_\_

```python
def __await__() -> Any
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.common.pagination.AsyncPaginator.__aiter__"></a>

#### \_\_aiter\_\_

```python
async def __aiter__() -> AsyncIterator[T]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/common/pagination.py)

<a id="qca.forward"></a>

# qca.forward

<a id="qca.forward.Client"></a>

#### Client

<a id="qca.forward.AsyncClient"></a>

#### AsyncClient

<a id="qca.forward.ForwardClient"></a>

#### ForwardClient

<a id="qca.forward.AsyncForwardClient"></a>

#### AsyncForwardClient

<a id="qca.forward._client"></a>

# qca.forward.\_client

<a id="qca.forward._client.Forward"></a>

## Forward

```python
class Forward(SyncAPIClient)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.templates"></a>

#### templates

```python
@cached_property
def templates() -> Templates
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.identities"></a>

#### identities

```python
@cached_property
def identities() -> Identities
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.sessions"></a>

#### sessions

```python
@cached_property
def sessions() -> Sessions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.schedules"></a>

#### schedules

```python
@cached_property
def schedules() -> Schedules
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.schedule_runs"></a>

#### schedule\_runs

```python
@cached_property
def schedule_runs() -> ScheduleRuns
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.batches"></a>

#### batches

```python
@cached_property
def batches() -> Batches
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.channels"></a>

#### channels

```python
@cached_property
def channels() -> Channels
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.channel_pairings"></a>

#### channel\_pairings

```python
@cached_property
def channel_pairings() -> ChannelPairings
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.environments"></a>

#### environments

```python
@cached_property
def environments() -> Environments
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.files"></a>

#### files

```python
@cached_property
def files() -> Files
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.skills"></a>

#### skills

```python
@cached_property
def skills() -> Skills
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.vaults"></a>

#### vaults

```python
@cached_property
def vaults() -> Vaults
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.memory_stores"></a>

#### memory\_stores

```python
@cached_property
def memory_stores() -> MemoryStores
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.Forward.models"></a>

#### models

```python
@cached_property
def models() -> Models
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward"></a>

## AsyncForward

```python
class AsyncForward(AsyncAPIClient)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.templates"></a>

#### templates

```python
@cached_property
def templates() -> AsyncTemplates
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.identities"></a>

#### identities

```python
@cached_property
def identities() -> AsyncIdentities
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.sessions"></a>

#### sessions

```python
@cached_property
def sessions() -> AsyncSessions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.schedules"></a>

#### schedules

```python
@cached_property
def schedules() -> AsyncSchedules
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.schedule_runs"></a>

#### schedule\_runs

```python
@cached_property
def schedule_runs() -> AsyncScheduleRuns
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.batches"></a>

#### batches

```python
@cached_property
def batches() -> AsyncBatches
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.channels"></a>

#### channels

```python
@cached_property
def channels() -> AsyncChannels
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.channel_pairings"></a>

#### channel\_pairings

```python
@cached_property
def channel_pairings() -> AsyncChannelPairings
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.environments"></a>

#### environments

```python
@cached_property
def environments() -> AsyncEnvironments
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.files"></a>

#### files

```python
@cached_property
def files() -> AsyncFiles
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.skills"></a>

#### skills

```python
@cached_property
def skills() -> AsyncSkills
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.vaults"></a>

#### vaults

```python
@cached_property
def vaults() -> AsyncVaults
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.memory_stores"></a>

#### memory\_stores

```python
@cached_property
def memory_stores() -> AsyncMemoryStores
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward._client.AsyncForward.models"></a>

#### models

```python
@cached_property
def models() -> AsyncModels
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/_client.py)

<a id="qca.forward.resources.batches.batches"></a>

# qca.forward.resources.batches.batches

<a id="qca.forward.resources.batches.batches.Batches"></a>

## Batches

```python
class Batches(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

<a id="qca.forward.resources.batches.batches.Batches.tasks"></a>

#### tasks

```python
@cached_property
def tasks() -> Tasks
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

<a id="qca.forward.resources.batches.batches.Batches.list"></a>

#### list

```python
def list(
    *,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Batch]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

GET /batches.

<a id="qca.forward.resources.batches.batches.Batches.create"></a>

#### create

```python
def create(
        *,
        input_file_id: str,
        completion_window: str,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Batch
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

POST /batches.

<a id="qca.forward.resources.batches.batches.Batches.retrieve"></a>

#### retrieve

```python
def retrieve(
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Batch
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

GET /batches/{batch_id}.

<a id="qca.forward.resources.batches.batches.Batches.cancel"></a>

#### cancel

```python
def cancel(
        batch_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Batch
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

POST /batches/{batch_id}/cancel.

<a id="qca.forward.resources.batches.batches.Batches.retrieve_error"></a>

#### retrieve\_error

```python
def retrieve_error(
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> BatchFile
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

GET /batches/{batch_id}/error.

<a id="qca.forward.resources.batches.batches.Batches.retrieve_output"></a>

#### retrieve\_output

```python
def retrieve_output(
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> BatchFile
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

GET /batches/{batch_id}/output.

<a id="qca.forward.resources.batches.batches.AsyncBatches"></a>

## AsyncBatches

```python
class AsyncBatches(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

<a id="qca.forward.resources.batches.batches.AsyncBatches.tasks"></a>

#### tasks

```python
@cached_property
def tasks() -> AsyncTasks
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

<a id="qca.forward.resources.batches.batches.AsyncBatches.list"></a>

#### list

```python
def list(
    *,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Batch]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

GET /batches.

<a id="qca.forward.resources.batches.batches.AsyncBatches.create"></a>

#### create

```python
async def create(
        *,
        input_file_id: str,
        completion_window: str,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Batch
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

POST /batches.

<a id="qca.forward.resources.batches.batches.AsyncBatches.retrieve"></a>

#### retrieve

```python
async def retrieve(
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Batch
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

GET /batches/{batch_id}.

<a id="qca.forward.resources.batches.batches.AsyncBatches.cancel"></a>

#### cancel

```python
async def cancel(
        batch_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Batch
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

POST /batches/{batch_id}/cancel.

<a id="qca.forward.resources.batches.batches.AsyncBatches.retrieve_error"></a>

#### retrieve\_error

```python
async def retrieve_error(
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> BatchFile
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

GET /batches/{batch_id}/error.

<a id="qca.forward.resources.batches.batches.AsyncBatches.retrieve_output"></a>

#### retrieve\_output

```python
async def retrieve_output(
        batch_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> BatchFile
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/batches.py)

GET /batches/{batch_id}/output.

<a id="qca.forward.resources.batches.tasks"></a>

# qca.forward.resources.batches.tasks

<a id="qca.forward.resources.batches.tasks.Tasks"></a>

## Tasks

```python
class Tasks(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/tasks.py)

<a id="qca.forward.resources.batches.tasks.Tasks.list"></a>

#### list

```python
def list(
    batch_id: str,
    *,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    custom_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[BatchTask]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/tasks.py)

GET /batches/{batch_id}/tasks.

<a id="qca.forward.resources.batches.tasks.AsyncTasks"></a>

## AsyncTasks

```python
class AsyncTasks(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/tasks.py)

<a id="qca.forward.resources.batches.tasks.AsyncTasks.list"></a>

#### list

```python
def list(
    batch_id: str,
    *,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    custom_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[BatchTask]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/batches/tasks.py)

GET /batches/{batch_id}/tasks.

<a id="qca.forward.resources.channel_pairings"></a>

# qca.forward.resources.channel\_pairings

<a id="qca.forward.resources.channel_pairings.ChannelPairings"></a>

## ChannelPairings

```python
class ChannelPairings(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channel_pairings.py)

<a id="qca.forward.resources.channel_pairings.ChannelPairings.create"></a>

#### create

```python
def create(
    *,
    code: str,
    identity_id: str,
    template_id: str,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ChannelPairing
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channel_pairings.py)

POST /channel_pairings.

<a id="qca.forward.resources.channel_pairings.ChannelPairings.delete"></a>

#### delete

```python
def delete(
    pairing_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedChannelPairing
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channel_pairings.py)

DELETE /channel_pairings/{pairing_id}.

<a id="qca.forward.resources.channel_pairings.AsyncChannelPairings"></a>

## AsyncChannelPairings

```python
class AsyncChannelPairings(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channel_pairings.py)

<a id="qca.forward.resources.channel_pairings.AsyncChannelPairings.create"></a>

#### create

```python
async def create(
    *,
    code: str,
    identity_id: str,
    template_id: str,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ChannelPairing
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channel_pairings.py)

POST /channel_pairings.

<a id="qca.forward.resources.channel_pairings.AsyncChannelPairings.delete"></a>

#### delete

```python
async def delete(
    pairing_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedChannelPairing
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channel_pairings.py)

DELETE /channel_pairings/{pairing_id}.

<a id="qca.forward.resources.channels.channels"></a>

# qca.forward.resources.channels.channels

<a id="qca.forward.resources.channels.channels.Channels"></a>

## Channels

```python
class Channels(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

<a id="qca.forward.resources.channels.channels.Channels.qr_sessions"></a>

#### qr\_sessions

```python
@cached_property
def qr_sessions() -> QrSessions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

<a id="qca.forward.resources.channels.channels.Channels.list"></a>

#### list

```python
def list(
    *,
    channel_type: Union[str, None, NotGiven] = NOT_GIVEN,
    enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
    binding_status: Union[str, None, NotGiven] = NOT_GIVEN,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Channel]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

GET /channels.

<a id="qca.forward.resources.channels.channels.Channels.create"></a>

#### create

```python
def create(
        *,
        channel_type: str,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_resolution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        channel_config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Channel
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

POST /channels.

<a id="qca.forward.resources.channels.channels.Channels.retrieve"></a>

#### retrieve

```python
def retrieve(
        channel_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Channel
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

GET /channels/{channel_id}.

<a id="qca.forward.resources.channels.channels.Channels.update"></a>

#### update

```python
def update(
        channel_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        channel_config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Channel
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

POST /channels/{channel_id}.

<a id="qca.forward.resources.channels.channels.Channels.delete"></a>

#### delete

```python
def delete(
    channel_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedChannel
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

DELETE /channels/{channel_id}.

<a id="qca.forward.resources.channels.channels.AsyncChannels"></a>

## AsyncChannels

```python
class AsyncChannels(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

<a id="qca.forward.resources.channels.channels.AsyncChannels.qr_sessions"></a>

#### qr\_sessions

```python
@cached_property
def qr_sessions() -> AsyncQrSessions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

<a id="qca.forward.resources.channels.channels.AsyncChannels.list"></a>

#### list

```python
def list(
    *,
    channel_type: Union[str, None, NotGiven] = NOT_GIVEN,
    enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
    binding_status: Union[str, None, NotGiven] = NOT_GIVEN,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Channel]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

GET /channels.

<a id="qca.forward.resources.channels.channels.AsyncChannels.create"></a>

#### create

```python
async def create(
        *,
        channel_type: str,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_resolution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        channel_config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Channel
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

POST /channels.

<a id="qca.forward.resources.channels.channels.AsyncChannels.retrieve"></a>

#### retrieve

```python
async def retrieve(
        channel_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Channel
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

GET /channels/{channel_id}.

<a id="qca.forward.resources.channels.channels.AsyncChannels.update"></a>

#### update

```python
async def update(
        channel_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        channel_config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Channel
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

POST /channels/{channel_id}.

<a id="qca.forward.resources.channels.channels.AsyncChannels.delete"></a>

#### delete

```python
async def delete(
    channel_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedChannel
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/channels.py)

DELETE /channels/{channel_id}.

<a id="qca.forward.resources.channels.qr_sessions"></a>

# qca.forward.resources.channels.qr\_sessions

<a id="qca.forward.resources.channels.qr_sessions.QrSessions"></a>

## QrSessions

```python
class QrSessions(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/qr_sessions.py)

<a id="qca.forward.resources.channels.qr_sessions.QrSessions.create"></a>

#### create

```python
def create(
    channel_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ChannelQRSession
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/qr_sessions.py)

POST /channels/{channel_id}/qr_sessions.

<a id="qca.forward.resources.channels.qr_sessions.QrSessions.retrieve"></a>

#### retrieve

```python
def retrieve(
    session_key: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ChannelQRSession
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/qr_sessions.py)

GET /qr_sessions/{session_key}.

<a id="qca.forward.resources.channels.qr_sessions.AsyncQrSessions"></a>

## AsyncQrSessions

```python
class AsyncQrSessions(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/qr_sessions.py)

<a id="qca.forward.resources.channels.qr_sessions.AsyncQrSessions.create"></a>

#### create

```python
async def create(
    channel_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ChannelQRSession
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/qr_sessions.py)

POST /channels/{channel_id}/qr_sessions.

<a id="qca.forward.resources.channels.qr_sessions.AsyncQrSessions.retrieve"></a>

#### retrieve

```python
async def retrieve(
    session_key: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ChannelQRSession
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/channels/qr_sessions.py)

GET /qr_sessions/{session_key}.

<a id="qca.forward.resources.environments"></a>

# qca.forward.resources.environments

<a id="qca.forward.resources.environments.Environments"></a>

## Environments

```python
class Environments(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

<a id="qca.forward.resources.environments.Environments.list"></a>

#### list

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Environment]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

GET /environments.

<a id="qca.forward.resources.environments.Environments.create"></a>

#### create

```python
def create(
    *,
    name: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

POST /environments.

<a id="qca.forward.resources.environments.Environments.retrieve"></a>

#### retrieve

```python
def retrieve(
    environment_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

GET /environments/{environment_id}.

<a id="qca.forward.resources.environments.Environments.update"></a>

#### update

```python
def update(
    environment_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

POST /environments/{environment_id}.

<a id="qca.forward.resources.environments.Environments.archive"></a>

#### archive

```python
def archive(
    environment_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

POST /environments/{environment_id}/archive.

<a id="qca.forward.resources.environments.Environments.delete"></a>

#### delete

```python
def delete(
        environment_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

DELETE /environments/{environment_id}.

<a id="qca.forward.resources.environments.AsyncEnvironments"></a>

## AsyncEnvironments

```python
class AsyncEnvironments(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

<a id="qca.forward.resources.environments.AsyncEnvironments.list"></a>

#### list

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Environment]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

GET /environments.

<a id="qca.forward.resources.environments.AsyncEnvironments.create"></a>

#### create

```python
async def create(
    *,
    name: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

POST /environments.

<a id="qca.forward.resources.environments.AsyncEnvironments.retrieve"></a>

#### retrieve

```python
async def retrieve(
    environment_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

GET /environments/{environment_id}.

<a id="qca.forward.resources.environments.AsyncEnvironments.update"></a>

#### update

```python
async def update(
    environment_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

POST /environments/{environment_id}.

<a id="qca.forward.resources.environments.AsyncEnvironments.archive"></a>

#### archive

```python
async def archive(
    environment_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

POST /environments/{environment_id}/archive.

<a id="qca.forward.resources.environments.AsyncEnvironments.delete"></a>

#### delete

```python
async def delete(
        environment_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/environments.py)

DELETE /environments/{environment_id}.

<a id="qca.forward.resources.files"></a>

# qca.forward.resources.files

<a id="qca.forward.resources.files.Files"></a>

## Files

```python
class Files(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

<a id="qca.forward.resources.files.Files.list"></a>

#### list

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    scope_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[FileMetadata]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

GET /files.

<a id="qca.forward.resources.files.Files.upload"></a>

#### upload

```python
def upload(
    *,
    file: FileTypes,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    purpose: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> FileMetadata
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

POST /files.

<a id="qca.forward.resources.files.Files.retrieve_metadata"></a>

#### retrieve\_metadata

```python
def retrieve_metadata(
    file_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> FileMetadata
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

GET /files/{file_id}.

<a id="qca.forward.resources.files.Files.delete"></a>

#### delete

```python
def delete(
        file_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

DELETE /files/{file_id}.

<a id="qca.forward.resources.files.Files.download"></a>

#### download

```python
def download(
    file_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> BinaryAPIResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

GET /files/{file_id}/content.

<a id="qca.forward.resources.files.AsyncFiles"></a>

## AsyncFiles

```python
class AsyncFiles(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

<a id="qca.forward.resources.files.AsyncFiles.list"></a>

#### list

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    scope_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[FileMetadata]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

GET /files.

<a id="qca.forward.resources.files.AsyncFiles.upload"></a>

#### upload

```python
async def upload(
    *,
    file: FileTypes,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    purpose: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> FileMetadata
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

POST /files.

<a id="qca.forward.resources.files.AsyncFiles.retrieve_metadata"></a>

#### retrieve\_metadata

```python
async def retrieve_metadata(
    file_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> FileMetadata
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

GET /files/{file_id}.

<a id="qca.forward.resources.files.AsyncFiles.delete"></a>

#### delete

```python
async def delete(
        file_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

DELETE /files/{file_id}.

<a id="qca.forward.resources.files.AsyncFiles.download"></a>

#### download

```python
async def download(
    file_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncBinaryAPIResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/files.py)

GET /files/{file_id}/content.

<a id="qca.forward.resources.identities.configs"></a>

# qca.forward.resources.identities.configs

<a id="qca.forward.resources.identities.configs.Configs"></a>

## Configs

```python
class Configs(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/configs.py)

<a id="qca.forward.resources.identities.configs.Configs.list"></a>

#### list

```python
def list(
    identity_id: str,
    *,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[IdentityConfig]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/configs.py)

GET /identities/{identity_id}/templates.

<a id="qca.forward.resources.identities.configs.Configs.retrieve"></a>

#### retrieve

```python
def retrieve(
    template_id: str,
    *,
    identity_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityConfig
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/configs.py)

GET /identities/{identity_id}/templates/{template_id}/config.

<a id="qca.forward.resources.identities.configs.Configs.upsert"></a>

#### upsert

```python
def upsert(
    template_id: str,
    *,
    identity_id: str,
    identity_config: IdentityConfigSpecParam,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityConfig
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/configs.py)

POST /identities/{identity_id}/templates/{template_id}/config.

<a id="qca.forward.resources.identities.configs.Configs.retrieve_effective"></a>

#### retrieve\_effective

```python
def retrieve_effective(
    template_id: str,
    *,
    identity_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> EffectiveConfig
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/configs.py)

GET /identities/{identity_id}/templates/{template_id}/effective.

<a id="qca.forward.resources.identities.configs.AsyncConfigs"></a>

## AsyncConfigs

```python
class AsyncConfigs(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/configs.py)

<a id="qca.forward.resources.identities.configs.AsyncConfigs.list"></a>

#### list

```python
def list(
    identity_id: str,
    *,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[IdentityConfig]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/configs.py)

GET /identities/{identity_id}/templates.

<a id="qca.forward.resources.identities.configs.AsyncConfigs.retrieve"></a>

#### retrieve

```python
async def retrieve(
    template_id: str,
    *,
    identity_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityConfig
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/configs.py)

GET /identities/{identity_id}/templates/{template_id}/config.

<a id="qca.forward.resources.identities.configs.AsyncConfigs.upsert"></a>

#### upsert

```python
async def upsert(
    template_id: str,
    *,
    identity_id: str,
    identity_config: IdentityConfigSpecParam,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityConfig
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/configs.py)

POST /identities/{identity_id}/templates/{template_id}/config.

<a id="qca.forward.resources.identities.configs.AsyncConfigs.retrieve_effective"></a>

#### retrieve\_effective

```python
async def retrieve_effective(
    template_id: str,
    *,
    identity_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> EffectiveConfig
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/configs.py)

GET /identities/{identity_id}/templates/{template_id}/effective.

<a id="qca.forward.resources.identities.identities"></a>

# qca.forward.resources.identities.identities

<a id="qca.forward.resources.identities.identities.Identities"></a>

## Identities

```python
class Identities(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

<a id="qca.forward.resources.identities.identities.Identities.configs"></a>

#### configs

```python
@cached_property
def configs() -> Configs
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

<a id="qca.forward.resources.identities.identities.Identities.memory_stores"></a>

#### memory\_stores

```python
@cached_property
def memory_stores() -> MemoryStores
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

<a id="qca.forward.resources.identities.identities.Identities.list"></a>

#### list

```python
def list(
    *,
    external_id: Union[str, None, NotGiven] = NOT_GIVEN,
    identity_i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
    search: Union[str, None, NotGiven] = NOT_GIVEN,
    enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Identity]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

GET /identities.

<a id="qca.forward.resources.identities.identities.Identities.create"></a>

#### create

```python
def create(
        *,
        external_id: str,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities.

<a id="qca.forward.resources.identities.identities.Identities.ensure_admin"></a>

#### ensure\_admin

```python
def ensure_admin(
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities/admin/ensure.

<a id="qca.forward.resources.identities.identities.Identities.stats"></a>

#### stats

```python
def stats(
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityStats
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

GET /identities/stats.

<a id="qca.forward.resources.identities.identities.Identities.retrieve"></a>

#### retrieve

```python
def retrieve(
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

GET /identities/{identity_id}.

<a id="qca.forward.resources.identities.identities.Identities.update"></a>

#### update

```python
def update(
        identity_id: str,
        *,
        external_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities/{identity_id}.

<a id="qca.forward.resources.identities.identities.Identities.delete"></a>

#### delete

```python
def delete(
    identity_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedIdentity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

DELETE /identities/{identity_id}.

<a id="qca.forward.resources.identities.identities.Identities.list_templates"></a>

#### list\_templates

```python
def list_templates(
    identity_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityListTemplatesResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

GET /identities/{identity_id}/agents.

<a id="qca.forward.resources.identities.identities.Identities.clear"></a>

#### clear

```python
def clear(
    identity_id: str,
    *,
    reason: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityClearResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities/{identity_id}/clear.

<a id="qca.forward.resources.identities.identities.Identities.disable"></a>

#### disable

```python
def disable(
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities/{identity_id}/disable.

<a id="qca.forward.resources.identities.identities.Identities.enable"></a>

#### enable

```python
def enable(
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities/{identity_id}/enable.

<a id="qca.forward.resources.identities.identities.AsyncIdentities"></a>

## AsyncIdentities

```python
class AsyncIdentities(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

<a id="qca.forward.resources.identities.identities.AsyncIdentities.configs"></a>

#### configs

```python
@cached_property
def configs() -> AsyncConfigs
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

<a id="qca.forward.resources.identities.identities.AsyncIdentities.memory_stores"></a>

#### memory\_stores

```python
@cached_property
def memory_stores() -> AsyncMemoryStores
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

<a id="qca.forward.resources.identities.identities.AsyncIdentities.list"></a>

#### list

```python
def list(
    *,
    external_id: Union[str, None, NotGiven] = NOT_GIVEN,
    identity_i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
    search: Union[str, None, NotGiven] = NOT_GIVEN,
    enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Identity]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

GET /identities.

<a id="qca.forward.resources.identities.identities.AsyncIdentities.create"></a>

#### create

```python
async def create(
        *,
        external_id: str,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities.

<a id="qca.forward.resources.identities.identities.AsyncIdentities.ensure_admin"></a>

#### ensure\_admin

```python
async def ensure_admin(
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities/admin/ensure.

<a id="qca.forward.resources.identities.identities.AsyncIdentities.stats"></a>

#### stats

```python
async def stats(
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityStats
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

GET /identities/stats.

<a id="qca.forward.resources.identities.identities.AsyncIdentities.retrieve"></a>

#### retrieve

```python
async def retrieve(
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

GET /identities/{identity_id}.

<a id="qca.forward.resources.identities.identities.AsyncIdentities.update"></a>

#### update

```python
async def update(
        identity_id: str,
        *,
        external_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        enabled: Union[bool, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities/{identity_id}.

<a id="qca.forward.resources.identities.identities.AsyncIdentities.delete"></a>

#### delete

```python
async def delete(
    identity_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedIdentity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

DELETE /identities/{identity_id}.

<a id="qca.forward.resources.identities.identities.AsyncIdentities.list_templates"></a>

#### list\_templates

```python
async def list_templates(
    identity_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityListTemplatesResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

GET /identities/{identity_id}/agents.

<a id="qca.forward.resources.identities.identities.AsyncIdentities.clear"></a>

#### clear

```python
async def clear(
    identity_id: str,
    *,
    reason: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityClearResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities/{identity_id}/clear.

<a id="qca.forward.resources.identities.identities.AsyncIdentities.disable"></a>

#### disable

```python
async def disable(
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities/{identity_id}/disable.

<a id="qca.forward.resources.identities.identities.AsyncIdentities.enable"></a>

#### enable

```python
async def enable(
        identity_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Identity
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/identities.py)

POST /identities/{identity_id}/enable.

<a id="qca.forward.resources.identities.memory_stores"></a>

# qca.forward.resources.identities.memory\_stores

<a id="qca.forward.resources.identities.memory_stores.MemoryStores"></a>

## MemoryStores

```python
class MemoryStores(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/memory_stores.py)

<a id="qca.forward.resources.identities.memory_stores.MemoryStores.list"></a>

#### list

```python
def list(
    template_id: str,
    *,
    identity_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityMemoryStoreListResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/memory_stores.py)

GET /identities/{identity_id}/templates/{template_id}/memory_stores.

<a id="qca.forward.resources.identities.memory_stores.MemoryStores.mount"></a>

#### mount

```python
def mount(
    template_id: str,
    *,
    identity_id: str,
    memory_store_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStoreMount
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/memory_stores.py)

POST /identities/{identity_id}/templates/{template_id}/memory_stores.

<a id="qca.forward.resources.identities.memory_stores.MemoryStores.detach"></a>

#### detach

```python
def detach(
    memory_store_id: str,
    *,
    template_id: str,
    identity_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedMemoryStoreMount
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/memory_stores.py)

DELETE /identities/{identity_id}/templates/{template_id}/memory_stores/{memory_store_id}.

<a id="qca.forward.resources.identities.memory_stores.AsyncMemoryStores"></a>

## AsyncMemoryStores

```python
class AsyncMemoryStores(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/memory_stores.py)

<a id="qca.forward.resources.identities.memory_stores.AsyncMemoryStores.list"></a>

#### list

```python
async def list(
    template_id: str,
    *,
    identity_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> IdentityMemoryStoreListResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/memory_stores.py)

GET /identities/{identity_id}/templates/{template_id}/memory_stores.

<a id="qca.forward.resources.identities.memory_stores.AsyncMemoryStores.mount"></a>

#### mount

```python
async def mount(
    template_id: str,
    *,
    identity_id: str,
    memory_store_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStoreMount
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/memory_stores.py)

POST /identities/{identity_id}/templates/{template_id}/memory_stores.

<a id="qca.forward.resources.identities.memory_stores.AsyncMemoryStores.detach"></a>

#### detach

```python
async def detach(
    memory_store_id: str,
    *,
    template_id: str,
    identity_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedMemoryStoreMount
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/identities/memory_stores.py)

DELETE /identities/{identity_id}/templates/{template_id}/memory_stores/{memory_store_id}.

<a id="qca.forward.resources.memory_stores.memories"></a>

# qca.forward.resources.memory\_stores.memories

<a id="qca.forward.resources.memory_stores.memories.Memories"></a>

## Memories

```python
class Memories(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

<a id="qca.forward.resources.memory_stores.memories.Memories.list"></a>

#### list

```python
def list(
    memory_store_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    path_prefix: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Memory]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

GET /memory_stores/{memory_store_id}/memories.

<a id="qca.forward.resources.memory_stores.memories.Memories.create"></a>

#### create

```python
def create(
        memory_store_id: str,
        *,
        path: str,
        content: str,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

POST /memory_stores/{memory_store_id}/memories.

<a id="qca.forward.resources.memory_stores.memories.Memories.retrieve"></a>

#### retrieve

```python
def retrieve(
        memory_id: str,
        *,
        memory_store_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

GET /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.forward.resources.memory_stores.memories.Memories.update"></a>

#### update

```python
def update(
        memory_id: str,
        *,
        memory_store_id: str,
        content: str,
        content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

POST /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.forward.resources.memory_stores.memories.Memories.delete"></a>

#### delete

```python
def delete(
    memory_id: str,
    *,
    memory_store_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedMemory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

DELETE /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.forward.resources.memory_stores.memories.AsyncMemories"></a>

## AsyncMemories

```python
class AsyncMemories(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

<a id="qca.forward.resources.memory_stores.memories.AsyncMemories.list"></a>

#### list

```python
def list(
    memory_store_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    path_prefix: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Memory]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

GET /memory_stores/{memory_store_id}/memories.

<a id="qca.forward.resources.memory_stores.memories.AsyncMemories.create"></a>

#### create

```python
async def create(
        memory_store_id: str,
        *,
        path: str,
        content: str,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

POST /memory_stores/{memory_store_id}/memories.

<a id="qca.forward.resources.memory_stores.memories.AsyncMemories.retrieve"></a>

#### retrieve

```python
async def retrieve(
        memory_id: str,
        *,
        memory_store_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

GET /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.forward.resources.memory_stores.memories.AsyncMemories.update"></a>

#### update

```python
async def update(
        memory_id: str,
        *,
        memory_store_id: str,
        content: str,
        content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

POST /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.forward.resources.memory_stores.memories.AsyncMemories.delete"></a>

#### delete

```python
async def delete(
    memory_id: str,
    *,
    memory_store_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedMemory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memories.py)

DELETE /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.forward.resources.memory_stores.memory_stores"></a>

# qca.forward.resources.memory\_stores.memory\_stores

<a id="qca.forward.resources.memory_stores.memory_stores.MemoryStores"></a>

## MemoryStores

```python
class MemoryStores(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

<a id="qca.forward.resources.memory_stores.memory_stores.MemoryStores.memories"></a>

#### memories

```python
@cached_property
def memories() -> Memories
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

<a id="qca.forward.resources.memory_stores.memory_stores.MemoryStores.memory_versions"></a>

#### memory\_versions

```python
@cached_property
def memory_versions() -> MemoryVersions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

<a id="qca.forward.resources.memory_stores.memory_stores.MemoryStores.list"></a>

#### list

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    system_managed: Union[bool, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[MemoryStore]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

GET /memory_stores.

<a id="qca.forward.resources.memory_stores.memory_stores.MemoryStores.create"></a>

#### create

```python
def create(
    *,
    name: str,
    idempotency_key: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

POST /memory_stores.

<a id="qca.forward.resources.memory_stores.memory_stores.MemoryStores.retrieve"></a>

#### retrieve

```python
def retrieve(
    memory_store_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

GET /memory_stores/{memory_store_id}.

<a id="qca.forward.resources.memory_stores.memory_stores.MemoryStores.update"></a>

#### update

```python
def update(
    memory_store_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

POST /memory_stores/{memory_store_id}.

<a id="qca.forward.resources.memory_stores.memory_stores.MemoryStores.delete"></a>

#### delete

```python
def delete(
    memory_store_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedMemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

DELETE /memory_stores/{memory_store_id}.

<a id="qca.forward.resources.memory_stores.memory_stores.MemoryStores.archive"></a>

#### archive

```python
def archive(
    memory_store_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

POST /memory_stores/{memory_store_id}/archive.

<a id="qca.forward.resources.memory_stores.memory_stores.AsyncMemoryStores"></a>

## AsyncMemoryStores

```python
class AsyncMemoryStores(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

<a id="qca.forward.resources.memory_stores.memory_stores.AsyncMemoryStores.memories"></a>

#### memories

```python
@cached_property
def memories() -> AsyncMemories
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

<a id="qca.forward.resources.memory_stores.memory_stores.AsyncMemoryStores.memory_versions"></a>

#### memory\_versions

```python
@cached_property
def memory_versions() -> AsyncMemoryVersions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

<a id="qca.forward.resources.memory_stores.memory_stores.AsyncMemoryStores.list"></a>

#### list

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    system_managed: Union[bool, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[MemoryStore]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

GET /memory_stores.

<a id="qca.forward.resources.memory_stores.memory_stores.AsyncMemoryStores.create"></a>

#### create

```python
async def create(
    *,
    name: str,
    idempotency_key: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

POST /memory_stores.

<a id="qca.forward.resources.memory_stores.memory_stores.AsyncMemoryStores.retrieve"></a>

#### retrieve

```python
async def retrieve(
    memory_store_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

GET /memory_stores/{memory_store_id}.

<a id="qca.forward.resources.memory_stores.memory_stores.AsyncMemoryStores.update"></a>

#### update

```python
async def update(
    memory_store_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

POST /memory_stores/{memory_store_id}.

<a id="qca.forward.resources.memory_stores.memory_stores.AsyncMemoryStores.delete"></a>

#### delete

```python
async def delete(
    memory_store_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedMemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

DELETE /memory_stores/{memory_store_id}.

<a id="qca.forward.resources.memory_stores.memory_stores.AsyncMemoryStores.archive"></a>

#### archive

```python
async def archive(
    memory_store_id: str,
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_stores.py)

POST /memory_stores/{memory_store_id}/archive.

<a id="qca.forward.resources.memory_stores.memory_versions"></a>

# qca.forward.resources.memory\_stores.memory\_versions

<a id="qca.forward.resources.memory_stores.memory_versions.MemoryVersions"></a>

## MemoryVersions

```python
class MemoryVersions(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_versions.py)

<a id="qca.forward.resources.memory_stores.memory_versions.MemoryVersions.list"></a>

#### list

```python
def list(
    memory_store_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    memory_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[MemoryVersion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_versions.py)

GET /memory_stores/{memory_store_id}/memory_versions.

<a id="qca.forward.resources.memory_stores.memory_versions.MemoryVersions.retrieve"></a>

#### retrieve

```python
def retrieve(
    memory_version_id: str,
    *,
    memory_store_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_versions.py)

GET /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}.

<a id="qca.forward.resources.memory_stores.memory_versions.MemoryVersions.redact"></a>

#### redact

```python
def redact(
    memory_version_id: str,
    *,
    memory_store_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_versions.py)

POST /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact.

<a id="qca.forward.resources.memory_stores.memory_versions.AsyncMemoryVersions"></a>

## AsyncMemoryVersions

```python
class AsyncMemoryVersions(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_versions.py)

<a id="qca.forward.resources.memory_stores.memory_versions.AsyncMemoryVersions.list"></a>

#### list

```python
def list(
    memory_store_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    memory_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[MemoryVersion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_versions.py)

GET /memory_stores/{memory_store_id}/memory_versions.

<a id="qca.forward.resources.memory_stores.memory_versions.AsyncMemoryVersions.retrieve"></a>

#### retrieve

```python
async def retrieve(
    memory_version_id: str,
    *,
    memory_store_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_versions.py)

GET /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}.

<a id="qca.forward.resources.memory_stores.memory_versions.AsyncMemoryVersions.redact"></a>

#### redact

```python
async def redact(
    memory_version_id: str,
    *,
    memory_store_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/memory_stores/memory_versions.py)

POST /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact.

<a id="qca.forward.resources.models"></a>

# qca.forward.resources.models

<a id="qca.forward.resources.models.Models"></a>

## Models

```python
class Models(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/models.py)

<a id="qca.forward.resources.models.Models.list"></a>

#### list

```python
def list(
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ModelListResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/models.py)

GET /models.

<a id="qca.forward.resources.models.AsyncModels"></a>

## AsyncModels

```python
class AsyncModels(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/models.py)

<a id="qca.forward.resources.models.AsyncModels.list"></a>

#### list

```python
async def list(
    *,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ModelListResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/models.py)

GET /models.

<a id="qca.forward.resources.schedule_runs"></a>

# qca.forward.resources.schedule\_runs

<a id="qca.forward.resources.schedule_runs.ScheduleRuns"></a>

## ScheduleRuns

```python
class ScheduleRuns(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedule_runs.py)

<a id="qca.forward.resources.schedule_runs.ScheduleRuns.list"></a>

#### list

```python
def list(
    *,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    schedule_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    trigger_type: Union[str, None, NotGiven] = NOT_GIVEN,
    has_error: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    sort_by: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[ScheduleRun]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedule_runs.py)

GET /schedule_runs.

<a id="qca.forward.resources.schedule_runs.ScheduleRuns.retrieve"></a>

#### retrieve

```python
def retrieve(
    run_id: str,
    *,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ScheduleRun
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedule_runs.py)

GET /schedule_runs/{run_id}.

<a id="qca.forward.resources.schedule_runs.AsyncScheduleRuns"></a>

## AsyncScheduleRuns

```python
class AsyncScheduleRuns(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedule_runs.py)

<a id="qca.forward.resources.schedule_runs.AsyncScheduleRuns.list"></a>

#### list

```python
def list(
    *,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    schedule_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    trigger_type: Union[str, None, NotGiven] = NOT_GIVEN,
    has_error: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    sort_by: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[ScheduleRun]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedule_runs.py)

GET /schedule_runs.

<a id="qca.forward.resources.schedule_runs.AsyncScheduleRuns.retrieve"></a>

#### retrieve

```python
async def retrieve(
    run_id: str,
    *,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ScheduleRun
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedule_runs.py)

GET /schedule_runs/{run_id}.

<a id="qca.forward.resources.schedules"></a>

# qca.forward.resources.schedules

<a id="qca.forward.resources.schedules.Schedules"></a>

## Schedules

```python
class Schedules(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

<a id="qca.forward.resources.schedules.Schedules.list"></a>

#### list

```python
def list(
    *,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    sort_by: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Schedule]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

GET /schedules.

<a id="qca.forward.resources.schedules.Schedules.create"></a>

#### create

```python
def create(
        *,
        identity_id: str,
        template_id: str,
        name: str,
        initial_events: List[Dict[str, Any]],
        environment_id: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        execution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        trigger_policy: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        sinks: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules.

<a id="qca.forward.resources.schedules.Schedules.archive_many"></a>

#### archive\_many

```python
def archive_many(
    *,
    schedule_ids: List[str],
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ScheduleArchiveManyResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/archive. Scope is set to by_schedule_ids automatically.

<a id="qca.forward.resources.schedules.Schedules.retrieve"></a>

#### retrieve

```python
def retrieve(
        schedule_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

GET /schedules/{schedule_id}.

<a id="qca.forward.resources.schedules.Schedules.update"></a>

#### update

```python
def update(
        schedule_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        initial_events: Union[List[Dict[str, Any]], None,
                              NotGiven] = NOT_GIVEN,
        execution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        trigger_policy: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        sinks: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/{schedule_id}.

<a id="qca.forward.resources.schedules.Schedules.archive"></a>

#### archive

```python
def archive(
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/{schedule_id}/archive.

<a id="qca.forward.resources.schedules.Schedules.pause"></a>

#### pause

```python
def pause(
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/{schedule_id}/pause.

<a id="qca.forward.resources.schedules.Schedules.run"></a>

#### run

```python
def run(
    schedule_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ScheduleRun
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/{schedule_id}/run.

<a id="qca.forward.resources.schedules.Schedules.unpause"></a>

#### unpause

```python
def unpause(
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/{schedule_id}/unpause.

<a id="qca.forward.resources.schedules.AsyncSchedules"></a>

## AsyncSchedules

```python
class AsyncSchedules(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

<a id="qca.forward.resources.schedules.AsyncSchedules.list"></a>

#### list

```python
def list(
    *,
    identity_id: Union[str, None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    sort_by: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Schedule]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

GET /schedules.

<a id="qca.forward.resources.schedules.AsyncSchedules.create"></a>

#### create

```python
async def create(
        *,
        identity_id: str,
        template_id: str,
        name: str,
        initial_events: List[Dict[str, Any]],
        environment_id: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        execution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        trigger_policy: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        sinks: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules.

<a id="qca.forward.resources.schedules.AsyncSchedules.archive_many"></a>

#### archive\_many

```python
async def archive_many(
    *,
    schedule_ids: List[str],
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ScheduleArchiveManyResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/archive. Scope is set to by_schedule_ids automatically.

<a id="qca.forward.resources.schedules.AsyncSchedules.retrieve"></a>

#### retrieve

```python
async def retrieve(
        schedule_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

GET /schedules/{schedule_id}.

<a id="qca.forward.resources.schedules.AsyncSchedules.update"></a>

#### update

```python
async def update(
        schedule_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        template_id: Union[str, None, NotGiven] = NOT_GIVEN,
        initial_events: Union[List[Dict[str, Any]], None,
                              NotGiven] = NOT_GIVEN,
        execution: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        trigger_policy: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        sinks: Union[List[Dict[str, Any]], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/{schedule_id}.

<a id="qca.forward.resources.schedules.AsyncSchedules.archive"></a>

#### archive

```python
async def archive(
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/{schedule_id}/archive.

<a id="qca.forward.resources.schedules.AsyncSchedules.pause"></a>

#### pause

```python
async def pause(
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/{schedule_id}/pause.

<a id="qca.forward.resources.schedules.AsyncSchedules.run"></a>

#### run

```python
async def run(
    schedule_id: str,
    *,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ScheduleRun
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/{schedule_id}/run.

<a id="qca.forward.resources.schedules.AsyncSchedules.unpause"></a>

#### unpause

```python
async def unpause(
        schedule_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Schedule
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/schedules.py)

POST /schedules/{schedule_id}/unpause.

<a id="qca.forward.resources.sessions.events"></a>

# qca.forward.resources.sessions.events

<a id="qca.forward.resources.sessions.events.Events"></a>

## Events

```python
class Events(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/events.py)

<a id="qca.forward.resources.sessions.events.Events.list"></a>

#### list

```python
def list(
    session_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
    type: Union[str, None, NotGiven] = NOT_GIVEN,
    types: Union[List[str], None, NotGiven] = NOT_GIVEN,
    include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
    include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/events.py)

GET /sessions/{session_id}/events.

<a id="qca.forward.resources.sessions.events.Events.send"></a>

#### send

```python
def send(
    session_id: str,
    *,
    events: List[SessionEventParam],
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionEventSendResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/events.py)

POST /sessions/{session_id}/events.

<a id="qca.forward.resources.sessions.events.Events.stream"></a>

#### stream

```python
def stream(
    session_id: str,
    *,
    event_deltas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
    include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Stream[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/events.py)

GET /sessions/{session_id}/events/stream.

<a id="qca.forward.resources.sessions.events.Events.resumable_stream"></a>

#### resumable\_stream

```python
def resumable_stream(
    session_id: str,
    *,
    event_deltas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
    include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ResumableStream[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/events.py)

Continuously reconnect GET /sessions/{session_id}/events/stream.

<a id="qca.forward.resources.sessions.events.AsyncEvents"></a>

## AsyncEvents

```python
class AsyncEvents(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/events.py)

<a id="qca.forward.resources.sessions.events.AsyncEvents.list"></a>

#### list

```python
def list(
    session_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
    type: Union[str, None, NotGiven] = NOT_GIVEN,
    types: Union[List[str], None, NotGiven] = NOT_GIVEN,
    include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
    include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/events.py)

GET /sessions/{session_id}/events.

<a id="qca.forward.resources.sessions.events.AsyncEvents.send"></a>

#### send

```python
async def send(
    session_id: str,
    *,
    events: List[SessionEventParam],
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionEventSendResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/events.py)

POST /sessions/{session_id}/events.

<a id="qca.forward.resources.sessions.events.AsyncEvents.stream"></a>

#### stream

```python
async def stream(
    session_id: str,
    *,
    event_deltas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
    include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncStream[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/events.py)

GET /sessions/{session_id}/events/stream.

<a id="qca.forward.resources.sessions.events.AsyncEvents.resumable_stream"></a>

#### resumable\_stream

```python
def resumable_stream(
    session_id: str,
    *,
    event_deltas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    include_tool_calls: Union[bool, None, NotGiven] = NOT_GIVEN,
    include_thinking: Union[bool, None, NotGiven] = NOT_GIVEN,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncResumableStream[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/events.py)

Continuously reconnect GET /sessions/{session_id}/events/stream.

<a id="qca.forward.resources.sessions.resources"></a>

# qca.forward.resources.sessions.resources

<a id="qca.forward.resources.sessions.resources.Resources"></a>

## Resources

```python
class Resources(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/resources.py)

<a id="qca.forward.resources.sessions.resources.Resources.add"></a>

#### add

```python
def add(
    session_id: str,
    *,
    type: str,
    file_id: str,
    mount_path: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionResource
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/resources.py)

POST /sessions/{session_id}/resources.

<a id="qca.forward.resources.sessions.resources.AsyncResources"></a>

## AsyncResources

```python
class AsyncResources(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/resources.py)

<a id="qca.forward.resources.sessions.resources.AsyncResources.add"></a>

#### add

```python
async def add(
    session_id: str,
    *,
    type: str,
    file_id: str,
    mount_path: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionResource
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/resources.py)

POST /sessions/{session_id}/resources.

<a id="qca.forward.resources.sessions.sessions"></a>

# qca.forward.resources.sessions.sessions

<a id="qca.forward.resources.sessions.sessions.Sessions"></a>

## Sessions

```python
class Sessions(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

<a id="qca.forward.resources.sessions.sessions.Sessions.events"></a>

#### events

```python
@cached_property
def events() -> Events
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

<a id="qca.forward.resources.sessions.sessions.Sessions.resources"></a>

#### resources

```python
@cached_property
def resources() -> Resources
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

<a id="qca.forward.resources.sessions.sessions.Sessions.threads"></a>

#### threads

```python
@cached_property
def threads() -> Threads
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

<a id="qca.forward.resources.sessions.sessions.Sessions.list"></a>

#### list

```python
def list(
    *,
    identity_i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    source_type: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Session]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

GET /sessions.

<a id="qca.forward.resources.sessions.sessions.Sessions.create"></a>

#### create

```python
def create(
        *,
        identity_id: str,
        template_id: str,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        config: Union[SessionCreateParamsConfigParam, None,
                      NotGiven] = NOT_GIVEN,
        resources: Union[List[SessionResourceSpecParam], None,
                         NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

POST /sessions.

<a id="qca.forward.resources.sessions.sessions.Sessions.retrieve"></a>

#### retrieve

```python
def retrieve(
        session_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

GET /sessions/{session_id}.

<a id="qca.forward.resources.sessions.sessions.Sessions.update"></a>

#### update

```python
def update(
        session_id: str,
        *,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        config: Union[SessionUpdateParamsConfigParam, None,
                      NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

POST /sessions/{session_id}.

<a id="qca.forward.resources.sessions.sessions.Sessions.archive"></a>

#### archive

```python
def archive(
        session_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

POST /sessions/{session_id}/archive.

<a id="qca.forward.resources.sessions.sessions.Sessions.cancel"></a>

#### cancel

```python
def cancel(
        session_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

POST /sessions/{session_id}/cancel.

<a id="qca.forward.resources.sessions.sessions.AsyncSessions"></a>

## AsyncSessions

```python
class AsyncSessions(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

<a id="qca.forward.resources.sessions.sessions.AsyncSessions.events"></a>

#### events

```python
@cached_property
def events() -> AsyncEvents
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

<a id="qca.forward.resources.sessions.sessions.AsyncSessions.resources"></a>

#### resources

```python
@cached_property
def resources() -> AsyncResources
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

<a id="qca.forward.resources.sessions.sessions.AsyncSessions.threads"></a>

#### threads

```python
@cached_property
def threads() -> AsyncThreads
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

<a id="qca.forward.resources.sessions.sessions.AsyncSessions.list"></a>

#### list

```python
def list(
    *,
    identity_i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
    template_id: Union[str, None, NotGiven] = NOT_GIVEN,
    source_type: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    updated_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Session]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

GET /sessions.

<a id="qca.forward.resources.sessions.sessions.AsyncSessions.create"></a>

#### create

```python
async def create(
        *,
        identity_id: str,
        template_id: str,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        config: Union[SessionCreateParamsConfigParam, None,
                      NotGiven] = NOT_GIVEN,
        resources: Union[List[SessionResourceSpecParam], None,
                         NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

POST /sessions.

<a id="qca.forward.resources.sessions.sessions.AsyncSessions.retrieve"></a>

#### retrieve

```python
async def retrieve(
        session_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

GET /sessions/{session_id}.

<a id="qca.forward.resources.sessions.sessions.AsyncSessions.update"></a>

#### update

```python
async def update(
        session_id: str,
        *,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        config: Union[SessionUpdateParamsConfigParam, None,
                      NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

POST /sessions/{session_id}.

<a id="qca.forward.resources.sessions.sessions.AsyncSessions.archive"></a>

#### archive

```python
async def archive(
        session_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

POST /sessions/{session_id}/archive.

<a id="qca.forward.resources.sessions.sessions.AsyncSessions.cancel"></a>

#### cancel

```python
async def cancel(
        session_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/sessions.py)

POST /sessions/{session_id}/cancel.

<a id="qca.forward.resources.sessions.threads.events"></a>

# qca.forward.resources.sessions.threads.events

<a id="qca.forward.resources.sessions.threads.events.Events"></a>

## Events

```python
class Events(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/events.py)

<a id="qca.forward.resources.sessions.threads.events.Events.list"></a>

#### list

```python
def list(
    thread_id: str,
    *,
    session_id: str,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/events.py)

GET /sessions/{session_id}/threads/{thread_id}/events.

<a id="qca.forward.resources.sessions.threads.events.Events.stream"></a>

#### stream

```python
def stream(
    thread_id: str,
    *,
    session_id: str,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Stream[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/events.py)

GET /sessions/{session_id}/threads/{thread_id}/stream.

<a id="qca.forward.resources.sessions.threads.events.AsyncEvents"></a>

## AsyncEvents

```python
class AsyncEvents(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/events.py)

<a id="qca.forward.resources.sessions.threads.events.AsyncEvents.list"></a>

#### list

```python
def list(
    thread_id: str,
    *,
    session_id: str,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/events.py)

GET /sessions/{session_id}/threads/{thread_id}/events.

<a id="qca.forward.resources.sessions.threads.events.AsyncEvents.stream"></a>

#### stream

```python
async def stream(
    thread_id: str,
    *,
    session_id: str,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncStream[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/events.py)

GET /sessions/{session_id}/threads/{thread_id}/stream.

<a id="qca.forward.resources.sessions.threads.threads"></a>

# qca.forward.resources.sessions.threads.threads

<a id="qca.forward.resources.sessions.threads.threads.Threads"></a>

## Threads

```python
class Threads(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/threads.py)

<a id="qca.forward.resources.sessions.threads.threads.Threads.events"></a>

#### events

```python
@cached_property
def events() -> Events
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/threads.py)

<a id="qca.forward.resources.sessions.threads.threads.Threads.list"></a>

#### list

```python
def list(
    session_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[SessionThread]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/threads.py)

GET /sessions/{session_id}/threads.

<a id="qca.forward.resources.sessions.threads.threads.Threads.retrieve"></a>

#### retrieve

```python
def retrieve(
    thread_id: str,
    *,
    session_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionThread
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/threads.py)

GET /sessions/{session_id}/threads/{thread_id}.

<a id="qca.forward.resources.sessions.threads.threads.Threads.archive"></a>

#### archive

```python
def archive(
    thread_id: str,
    *,
    session_id: str,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionThread
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/threads.py)

POST /sessions/{session_id}/threads/{thread_id}/archive.

<a id="qca.forward.resources.sessions.threads.threads.AsyncThreads"></a>

## AsyncThreads

```python
class AsyncThreads(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/threads.py)

<a id="qca.forward.resources.sessions.threads.threads.AsyncThreads.events"></a>

#### events

```python
@cached_property
def events() -> AsyncEvents
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/threads.py)

<a id="qca.forward.resources.sessions.threads.threads.AsyncThreads.list"></a>

#### list

```python
def list(
    session_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[SessionThread]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/threads.py)

GET /sessions/{session_id}/threads.

<a id="qca.forward.resources.sessions.threads.threads.AsyncThreads.retrieve"></a>

#### retrieve

```python
async def retrieve(
    thread_id: str,
    *,
    session_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionThread
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/threads.py)

GET /sessions/{session_id}/threads/{thread_id}.

<a id="qca.forward.resources.sessions.threads.threads.AsyncThreads.archive"></a>

#### archive

```python
async def archive(
    thread_id: str,
    *,
    session_id: str,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionThread
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/sessions/threads/threads.py)

POST /sessions/{session_id}/threads/{thread_id}/archive.

<a id="qca.forward.resources.skills.skills"></a>

# qca.forward.resources.skills.skills

<a id="qca.forward.resources.skills.skills.Skills"></a>

## Skills

```python
class Skills(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

<a id="qca.forward.resources.skills.skills.Skills.versions"></a>

#### versions

```python
@cached_property
def versions() -> Versions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

<a id="qca.forward.resources.skills.skills.Skills.list"></a>

#### list

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    display_title: Union[str, None, NotGiven] = NOT_GIVEN,
    source: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Skill]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

GET /skills.

<a id="qca.forward.resources.skills.skills.Skills.create"></a>

#### create

```python
def create(
        *,
        files: Union[List[FileTypes], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        icon_id: Union[str, None, NotGiven] = NOT_GIVEN,
        file: Union[FileTypes, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        type: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Skill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

POST /skills.

<a id="qca.forward.resources.skills.skills.Skills.retrieve"></a>

#### retrieve

```python
def retrieve(
        skill_id: str,
        *,
        include_content: Union[bool, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Skill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

GET /skills/{skill_id}.

<a id="qca.forward.resources.skills.skills.Skills.update"></a>

#### update

```python
def update(
        skill_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        content: Union[str, None, NotGiven] = NOT_GIVEN,
        content_encoding: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        icon_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Skill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

PUT /skills/{skill_id}.

<a id="qca.forward.resources.skills.skills.Skills.delete"></a>

#### delete

```python
def delete(
        skill_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

DELETE /skills/{skill_id}.

<a id="qca.forward.resources.skills.skills.AsyncSkills"></a>

## AsyncSkills

```python
class AsyncSkills(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

<a id="qca.forward.resources.skills.skills.AsyncSkills.versions"></a>

#### versions

```python
@cached_property
def versions() -> AsyncVersions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

<a id="qca.forward.resources.skills.skills.AsyncSkills.list"></a>

#### list

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    display_title: Union[str, None, NotGiven] = NOT_GIVEN,
    source: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Skill]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

GET /skills.

<a id="qca.forward.resources.skills.skills.AsyncSkills.create"></a>

#### create

```python
async def create(
        *,
        files: Union[List[FileTypes], None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        icon_id: Union[str, None, NotGiven] = NOT_GIVEN,
        file: Union[FileTypes, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        type: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Skill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

POST /skills.

<a id="qca.forward.resources.skills.skills.AsyncSkills.retrieve"></a>

#### retrieve

```python
async def retrieve(
        skill_id: str,
        *,
        include_content: Union[bool, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Skill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

GET /skills/{skill_id}.

<a id="qca.forward.resources.skills.skills.AsyncSkills.update"></a>

#### update

```python
async def update(
        skill_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        content: Union[str, None, NotGiven] = NOT_GIVEN,
        content_encoding: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        icon_id: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Skill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

PUT /skills/{skill_id}.

<a id="qca.forward.resources.skills.skills.AsyncSkills.delete"></a>

#### delete

```python
async def delete(
        skill_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/skills.py)

DELETE /skills/{skill_id}.

<a id="qca.forward.resources.skills.versions"></a>

# qca.forward.resources.skills.versions

<a id="qca.forward.resources.skills.versions.Versions"></a>

## Versions

```python
class Versions(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

<a id="qca.forward.resources.skills.versions.Versions.list"></a>

#### list

```python
def list(
    skill_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[SkillVersion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

GET /skills/{skill_id}/versions.

<a id="qca.forward.resources.skills.versions.Versions.create"></a>

#### create

```python
def create(
    skill_id: str,
    *,
    files: List[FileTypes],
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

POST /skills/{skill_id}/versions.

<a id="qca.forward.resources.skills.versions.Versions.retrieve"></a>

#### retrieve

```python
def retrieve(
    version: str,
    *,
    skill_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

GET /skills/{skill_id}/versions/{version}.

<a id="qca.forward.resources.skills.versions.Versions.delete"></a>

#### delete

```python
def delete(
    version: str,
    *,
    skill_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedSkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

DELETE /skills/{skill_id}/versions/{version}.

<a id="qca.forward.resources.skills.versions.Versions.download"></a>

#### download

```python
def download(
    version: str,
    *,
    skill_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> BinaryAPIResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

GET /skills/{skill_id}/versions/{version}/content.

<a id="qca.forward.resources.skills.versions.AsyncVersions"></a>

## AsyncVersions

```python
class AsyncVersions(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

<a id="qca.forward.resources.skills.versions.AsyncVersions.list"></a>

#### list

```python
def list(
    skill_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[SkillVersion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

GET /skills/{skill_id}/versions.

<a id="qca.forward.resources.skills.versions.AsyncVersions.create"></a>

#### create

```python
async def create(
    skill_id: str,
    *,
    files: List[FileTypes],
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

POST /skills/{skill_id}/versions.

<a id="qca.forward.resources.skills.versions.AsyncVersions.retrieve"></a>

#### retrieve

```python
async def retrieve(
    version: str,
    *,
    skill_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

GET /skills/{skill_id}/versions/{version}.

<a id="qca.forward.resources.skills.versions.AsyncVersions.delete"></a>

#### delete

```python
async def delete(
    version: str,
    *,
    skill_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedSkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

DELETE /skills/{skill_id}/versions/{version}.

<a id="qca.forward.resources.skills.versions.AsyncVersions.download"></a>

#### download

```python
async def download(
    version: str,
    *,
    skill_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncBinaryAPIResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/skills/versions.py)

GET /skills/{skill_id}/versions/{version}/content.

<a id="qca.forward.resources.templates"></a>

# qca.forward.resources.templates

<a id="qca.forward.resources.templates.Templates"></a>

## Templates

```python
class Templates(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

<a id="qca.forward.resources.templates.Templates.list"></a>

#### list

```python
def list(
    *,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Template]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

GET /templates.

<a id="qca.forward.resources.templates.Templates.create"></a>

#### create

```python
def create(
        *,
        name: str,
        model: Union[str, ModelConfigParam],
        environment_id: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolParam], None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[MCPServerParam], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[SkillBindingParam], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentConfigParam, None, NotGiven] = NOT_GIVEN,
        vaults: Union[Dict[str, ResourceBindingParam], None,
                      NotGiven] = NOT_GIVEN,
        files: Union[Dict[str, ResourceBindingParam], None,
                     NotGiven] = NOT_GIVEN,
        github_repositories: Union[Dict[str, GitHubRepositoryParam], None,
                                   NotGiven] = NOT_GIVEN,
        environment_variables: Union[Union[Dict[str, Any], str], None,
                                     NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        beta: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Template
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

POST /templates.

<a id="qca.forward.resources.templates.Templates.retrieve"></a>

#### retrieve

```python
def retrieve(
        template_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Template
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

GET /templates/{template_id}.

<a id="qca.forward.resources.templates.Templates.update"></a>

#### update

```python
def update(
        template_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        model: Union[Union[str, ModelConfigParam], None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolParam], None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[MCPServerParam], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[SkillBindingParam], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentConfigParam, None, NotGiven] = NOT_GIVEN,
        environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        vaults: Union[Dict[str, ResourceBindingParam], None,
                      NotGiven] = NOT_GIVEN,
        files: Union[Dict[str, ResourceBindingParam], None,
                     NotGiven] = NOT_GIVEN,
        github_repositories: Union[Dict[str, GitHubRepositoryParam], None,
                                   NotGiven] = NOT_GIVEN,
        environment_variables: Union[Union[Dict[str, Any], str], None,
                                     NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        beta: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Template
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

POST /templates/{template_id}.

<a id="qca.forward.resources.templates.Templates.archive"></a>

#### archive

```python
def archive(
        template_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Template
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

POST /templates/{template_id}/archive.

<a id="qca.forward.resources.templates.Templates.clone"></a>

#### clone

```python
def clone(
        template_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Template
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

POST /templates/{template_id}/clone.

<a id="qca.forward.resources.templates.AsyncTemplates"></a>

## AsyncTemplates

```python
class AsyncTemplates(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

<a id="qca.forward.resources.templates.AsyncTemplates.list"></a>

#### list

```python
def list(
    *,
    status: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Template]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

GET /templates.

<a id="qca.forward.resources.templates.AsyncTemplates.create"></a>

#### create

```python
async def create(
        *,
        name: str,
        model: Union[str, ModelConfigParam],
        environment_id: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolParam], None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[MCPServerParam], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[SkillBindingParam], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentConfigParam, None, NotGiven] = NOT_GIVEN,
        vaults: Union[Dict[str, ResourceBindingParam], None,
                      NotGiven] = NOT_GIVEN,
        files: Union[Dict[str, ResourceBindingParam], None,
                     NotGiven] = NOT_GIVEN,
        github_repositories: Union[Dict[str, GitHubRepositoryParam], None,
                                   NotGiven] = NOT_GIVEN,
        environment_variables: Union[Union[Dict[str, Any], str], None,
                                     NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        beta: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Template
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

POST /templates.

<a id="qca.forward.resources.templates.AsyncTemplates.retrieve"></a>

#### retrieve

```python
async def retrieve(
        template_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Template
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

GET /templates/{template_id}.

<a id="qca.forward.resources.templates.AsyncTemplates.update"></a>

#### update

```python
async def update(
        template_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        model: Union[Union[str, ModelConfigParam], None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        tools: Union[List[ToolParam], None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[MCPServerParam], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[SkillBindingParam], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentConfigParam, None, NotGiven] = NOT_GIVEN,
        environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
        vaults: Union[Dict[str, ResourceBindingParam], None,
                      NotGiven] = NOT_GIVEN,
        files: Union[Dict[str, ResourceBindingParam], None,
                     NotGiven] = NOT_GIVEN,
        github_repositories: Union[Dict[str, GitHubRepositoryParam], None,
                                   NotGiven] = NOT_GIVEN,
        environment_variables: Union[Union[Dict[str, Any], str], None,
                                     NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        beta: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Template
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

POST /templates/{template_id}.

<a id="qca.forward.resources.templates.AsyncTemplates.archive"></a>

#### archive

```python
async def archive(
        template_id: str,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Template
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

POST /templates/{template_id}/archive.

<a id="qca.forward.resources.templates.AsyncTemplates.clone"></a>

#### clone

```python
async def clone(
        template_id: str,
        *,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Template
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/templates.py)

POST /templates/{template_id}/clone.

<a id="qca.forward.resources.vaults.credentials"></a>

# qca.forward.resources.vaults.credentials

<a id="qca.forward.resources.vaults.credentials.Credentials"></a>

## Credentials

```python
class Credentials(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/credentials.py)

<a id="qca.forward.resources.vaults.credentials.Credentials.list"></a>

#### list

```python
def list(
    vault_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[VaultCredential]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/credentials.py)

GET /vaults/{vault_id}/credentials.

<a id="qca.forward.resources.vaults.credentials.Credentials.create"></a>

#### create

```python
def create(
    vault_id: str,
    *,
    auth: Dict[str, Any],
    display_name: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> VaultCredential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/credentials.py)

POST /vaults/{vault_id}/credentials.

<a id="qca.forward.resources.vaults.credentials.Credentials.retrieve"></a>

#### retrieve

```python
def retrieve(
    credential_id: str,
    *,
    vault_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> VaultCredential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/credentials.py)

GET /vaults/{vault_id}/credentials/{credential_id}.

<a id="qca.forward.resources.vaults.credentials.Credentials.delete"></a>

#### delete

```python
def delete(
        credential_id: str,
        *,
        vault_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/credentials.py)

DELETE /vaults/{vault_id}/credentials/{credential_id}.

<a id="qca.forward.resources.vaults.credentials.AsyncCredentials"></a>

## AsyncCredentials

```python
class AsyncCredentials(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/credentials.py)

<a id="qca.forward.resources.vaults.credentials.AsyncCredentials.list"></a>

#### list

```python
def list(
    vault_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[VaultCredential]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/credentials.py)

GET /vaults/{vault_id}/credentials.

<a id="qca.forward.resources.vaults.credentials.AsyncCredentials.create"></a>

#### create

```python
async def create(
    vault_id: str,
    *,
    auth: Dict[str, Any],
    display_name: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> VaultCredential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/credentials.py)

POST /vaults/{vault_id}/credentials.

<a id="qca.forward.resources.vaults.credentials.AsyncCredentials.retrieve"></a>

#### retrieve

```python
async def retrieve(
    credential_id: str,
    *,
    vault_id: str,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> VaultCredential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/credentials.py)

GET /vaults/{vault_id}/credentials/{credential_id}.

<a id="qca.forward.resources.vaults.credentials.AsyncCredentials.delete"></a>

#### delete

```python
async def delete(
        credential_id: str,
        *,
        vault_id: str,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/credentials.py)

DELETE /vaults/{vault_id}/credentials/{credential_id}.

<a id="qca.forward.resources.vaults.vaults"></a>

# qca.forward.resources.vaults.vaults

<a id="qca.forward.resources.vaults.vaults.Vaults"></a>

## Vaults

```python
class Vaults(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

<a id="qca.forward.resources.vaults.vaults.Vaults.credentials"></a>

#### credentials

```python
@cached_property
def credentials() -> Credentials
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

<a id="qca.forward.resources.vaults.vaults.Vaults.list"></a>

#### list

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Vault]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

GET /vaults.

<a id="qca.forward.resources.vaults.vaults.Vaults.create"></a>

#### create

```python
def create(
        *,
        display_name: str,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Vault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

POST /vaults.

<a id="qca.forward.resources.vaults.vaults.Vaults.retrieve"></a>

#### retrieve

```python
def retrieve(
        vault_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Vault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

GET /vaults/{vault_id}.

<a id="qca.forward.resources.vaults.vaults.Vaults.delete"></a>

#### delete

```python
def delete(
        vault_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

DELETE /vaults/{vault_id}.

<a id="qca.forward.resources.vaults.vaults.AsyncVaults"></a>

## AsyncVaults

```python
class AsyncVaults(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

<a id="qca.forward.resources.vaults.vaults.AsyncVaults.credentials"></a>

#### credentials

```python
@cached_property
def credentials() -> AsyncCredentials
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

<a id="qca.forward.resources.vaults.vaults.AsyncVaults.list"></a>

#### list

```python
def list(
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Vault]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

GET /vaults.

<a id="qca.forward.resources.vaults.vaults.AsyncVaults.create"></a>

#### create

```python
async def create(
        *,
        display_name: str,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Vault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

POST /vaults.

<a id="qca.forward.resources.vaults.vaults.AsyncVaults.retrieve"></a>

#### retrieve

```python
async def retrieve(
        vault_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Vault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

GET /vaults/{vault_id}.

<a id="qca.forward.resources.vaults.vaults.AsyncVaults.delete"></a>

#### delete

```python
async def delete(
        vault_id: str,
        *,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> None
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/resources/vaults/vaults.py)

DELETE /vaults/{vault_id}.

<a id="qca.forward.types.batch"></a>

# qca.forward.types.batch

<a id="qca.forward.types.batch.Batch"></a>

## Batch

```python
class Batch(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch.py)

<a id="qca.forward.types.batch.Batch.id"></a>

#### id

<a id="qca.forward.types.batch.Batch.object"></a>

#### object

<a id="qca.forward.types.batch.Batch.status"></a>

#### status

<a id="qca.forward.types.batch.Batch.input_file_id"></a>

#### input\_file\_id

<a id="qca.forward.types.batch.Batch.output_file_id"></a>

#### output\_file\_id

<a id="qca.forward.types.batch.Batch.completion_window"></a>

#### completion\_window

<a id="qca.forward.types.batch.Batch.created_at"></a>

#### created\_at

<a id="qca.forward.types.batch.Batch.expires_at"></a>

#### expires\_at

<a id="qca.forward.types.batch.Batch.request_counts"></a>

#### request\_counts

<a id="qca.forward.types.batch.Batch.usage"></a>

#### usage

<a id="qca.forward.types.batch.Batch.metadata"></a>

#### metadata

<a id="qca.forward.types.batch.Batch.total"></a>

#### total

<a id="qca.forward.types.batch.Batch.pending"></a>

#### pending

<a id="qca.forward.types.batch.Batch.running"></a>

#### running

<a id="qca.forward.types.batch.Batch.completed"></a>

#### completed

<a id="qca.forward.types.batch.Batch.failed"></a>

#### failed

<a id="qca.forward.types.batch.Batch.cancelled"></a>

#### cancelled

<a id="qca.forward.types.batch.Batch.expired"></a>

#### expired

<a id="qca.forward.types.batch.Batch.error_file_id"></a>

#### error\_file\_id

<a id="qca.forward.types.batch.Batch.error_message"></a>

#### error\_message

<a id="qca.forward.types.batch_cancel_params"></a>

# qca.forward.types.batch\_cancel\_params

<a id="qca.forward.types.batch_cancel_params.BatchCancelParams"></a>

## BatchCancelParams

```python
class BatchCancelParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch_cancel_params.py)

<a id="qca.forward.types.batch_cancel_params.BatchCancelParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.batch_create_params"></a>

# qca.forward.types.batch\_create\_params

<a id="qca.forward.types.batch_create_params.BatchCreateParams"></a>

## BatchCreateParams

```python
class BatchCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch_create_params.py)

<a id="qca.forward.types.batch_create_params.BatchCreateParams.input_file_id"></a>

#### input\_file\_id

<a id="qca.forward.types.batch_create_params.BatchCreateParams.completion_window"></a>

#### completion\_window

<a id="qca.forward.types.batch_create_params.BatchCreateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.batch_create_params.BatchCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.batch_file"></a>

# qca.forward.types.batch\_file

<a id="qca.forward.types.batch_file.BatchFile"></a>

## BatchFile

```python
class BatchFile(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch_file.py)

<a id="qca.forward.types.batch_file.BatchFile.url"></a>

#### url

<a id="qca.forward.types.batch_file.BatchFile.expires_at"></a>

#### expires\_at

<a id="qca.forward.types.batch_list_params"></a>

# qca.forward.types.batch\_list\_params

<a id="qca.forward.types.batch_list_params.BatchListParams"></a>

## BatchListParams

```python
class BatchListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch_list_params.py)

<a id="qca.forward.types.batch_list_params.BatchListParams.status"></a>

#### status

<a id="qca.forward.types.batch_list_params.BatchListParams.limit"></a>

#### limit

<a id="qca.forward.types.batch_list_params.BatchListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.batch_list_params.BatchListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.batch_request_counts"></a>

# qca.forward.types.batch\_request\_counts

<a id="qca.forward.types.batch_request_counts.BatchRequestCounts"></a>

## BatchRequestCounts

```python
class BatchRequestCounts(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch_request_counts.py)

<a id="qca.forward.types.batch_request_counts.BatchRequestCounts.total"></a>

#### total

<a id="qca.forward.types.batch_request_counts.BatchRequestCounts.pending"></a>

#### pending

<a id="qca.forward.types.batch_request_counts.BatchRequestCounts.running"></a>

#### running

<a id="qca.forward.types.batch_request_counts.BatchRequestCounts.completed"></a>

#### completed

<a id="qca.forward.types.batch_request_counts.BatchRequestCounts.failed"></a>

#### failed

<a id="qca.forward.types.batch_request_counts.BatchRequestCounts.cancelled"></a>

#### cancelled

<a id="qca.forward.types.batch_request_counts.BatchRequestCounts.expired"></a>

#### expired

<a id="qca.forward.types.batch_task"></a>

# qca.forward.types.batch\_task

<a id="qca.forward.types.batch_task.BatchTask"></a>

## BatchTask

```python
class BatchTask(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch_task.py)

<a id="qca.forward.types.batch_task.BatchTask.custom_id"></a>

#### custom\_id

<a id="qca.forward.types.batch_task.BatchTask.status"></a>

#### status

<a id="qca.forward.types.batch_task.BatchTask.started_at"></a>

#### started\_at

<a id="qca.forward.types.batch_task.BatchTask.completed_at"></a>

#### completed\_at

<a id="qca.forward.types.batch_task.BatchTask.output_summary"></a>

#### output\_summary

<a id="qca.forward.types.batch_task.BatchTask.usage"></a>

#### usage

<a id="qca.forward.types.batch_task.BatchTask.artifacts"></a>

#### artifacts

<a id="qca.forward.types.batch_task.BatchTask.error"></a>

#### error

<a id="qca.forward.types.batch_task_artifacts_item"></a>

# qca.forward.types.batch\_task\_artifacts\_item

<a id="qca.forward.types.batch_task_artifacts_item.BatchTaskArtifactsItem"></a>

## BatchTaskArtifactsItem

```python
class BatchTaskArtifactsItem(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch_task_artifacts_item.py)

<a id="qca.forward.types.batch_task_artifacts_item.BatchTaskArtifactsItem.file_id"></a>

#### file\_id

<a id="qca.forward.types.batch_task_artifacts_item.BatchTaskArtifactsItem.name"></a>

#### name

<a id="qca.forward.types.batch_task_artifacts_item.BatchTaskArtifactsItem.size"></a>

#### size

<a id="qca.forward.types.batch_task_artifacts_item.BatchTaskArtifactsItem.content_type"></a>

#### content\_type

<a id="qca.forward.types.batch_task_error"></a>

# qca.forward.types.batch\_task\_error

<a id="qca.forward.types.batch_task_error.BatchTaskError"></a>

## BatchTaskError

```python
class BatchTaskError(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch_task_error.py)

<a id="qca.forward.types.batch_task_error.BatchTaskError.code"></a>

#### code

<a id="qca.forward.types.batch_task_error.BatchTaskError.message"></a>

#### message

<a id="qca.forward.types.batch_task_list_params"></a>

# qca.forward.types.batch\_task\_list\_params

<a id="qca.forward.types.batch_task_list_params.BatchTaskListParams"></a>

## BatchTaskListParams

```python
class BatchTaskListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch_task_list_params.py)

<a id="qca.forward.types.batch_task_list_params.BatchTaskListParams.status"></a>

#### status

<a id="qca.forward.types.batch_task_list_params.BatchTaskListParams.custom_id"></a>

#### custom\_id

<a id="qca.forward.types.batch_task_list_params.BatchTaskListParams.limit"></a>

#### limit

<a id="qca.forward.types.batch_task_list_params.BatchTaskListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.batch_task_usage"></a>

# qca.forward.types.batch\_task\_usage

<a id="qca.forward.types.batch_task_usage.BatchTaskUsage"></a>

## BatchTaskUsage

```python
class BatchTaskUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch_task_usage.py)

<a id="qca.forward.types.batch_task_usage.BatchTaskUsage.total_credits"></a>

#### total\_credits

<a id="qca.forward.types.batch_usage"></a>

# qca.forward.types.batch\_usage

<a id="qca.forward.types.batch_usage.BatchUsage"></a>

## BatchUsage

```python
class BatchUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/batch_usage.py)

<a id="qca.forward.types.batch_usage.BatchUsage.total_credits"></a>

#### total\_credits

<a id="qca.forward.types.channel"></a>

# qca.forward.types.channel

<a id="qca.forward.types.channel.Channel"></a>

## Channel

```python
class Channel(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/channel.py)

<a id="qca.forward.types.channel.Channel.id"></a>

#### id

<a id="qca.forward.types.channel.Channel.type"></a>

#### type

<a id="qca.forward.types.channel.Channel.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.channel.Channel.identity_resolution"></a>

#### identity\_resolution

<a id="qca.forward.types.channel.Channel.template_id"></a>

#### template\_id

<a id="qca.forward.types.channel.Channel.channel_type"></a>

#### channel\_type

<a id="qca.forward.types.channel.Channel.name"></a>

#### name

<a id="qca.forward.types.channel.Channel.enabled"></a>

#### enabled

<a id="qca.forward.types.channel.Channel.binding_status"></a>

#### binding\_status

<a id="qca.forward.types.channel.Channel.channel_config"></a>

#### channel\_config

<a id="qca.forward.types.channel.Channel.created_at"></a>

#### created\_at

<a id="qca.forward.types.channel.Channel.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.channel_channel_config"></a>

# qca.forward.types.channel\_channel\_config

<a id="qca.forward.types.channel_channel_config.ChannelChannelConfig"></a>

## ChannelChannelConfig

```python
class ChannelChannelConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/channel_channel_config.py)

<a id="qca.forward.types.channel_channel_config.ChannelChannelConfig.response_options"></a>

#### response\_options

<a id="qca.forward.types.channel_channel_config_response_options"></a>

# qca.forward.types.channel\_channel\_config\_response\_options

<a id="qca.forward.types.channel_channel_config_response_options.ChannelChannelConfigResponseOptions"></a>

## ChannelChannelConfigResponseOptions

```python
class ChannelChannelConfigResponseOptions(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/channel_channel_config_response_options.py)

<a id="qca.forward.types.channel_channel_config_response_options.ChannelChannelConfigResponseOptions.include_tool_calls"></a>

#### include\_tool\_calls

<a id="qca.forward.types.channel_channel_config_response_options.ChannelChannelConfigResponseOptions.include_thinking"></a>

#### include\_thinking

<a id="qca.forward.types.channel_create_params"></a>

# qca.forward.types.channel\_create\_params

<a id="qca.forward.types.channel_create_params.ChannelCreateParams"></a>

## ChannelCreateParams

```python
class ChannelCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/channel_create_params.py)

<a id="qca.forward.types.channel_create_params.ChannelCreateParams.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.channel_create_params.ChannelCreateParams.identity_resolution"></a>

#### identity\_resolution

<a id="qca.forward.types.channel_create_params.ChannelCreateParams.template_id"></a>

#### template\_id

<a id="qca.forward.types.channel_create_params.ChannelCreateParams.channel_type"></a>

#### channel\_type

<a id="qca.forward.types.channel_create_params.ChannelCreateParams.name"></a>

#### name

<a id="qca.forward.types.channel_create_params.ChannelCreateParams.enabled"></a>

#### enabled

<a id="qca.forward.types.channel_create_params.ChannelCreateParams.channel_config"></a>

#### channel\_config

<a id="qca.forward.types.channel_create_params.ChannelCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.channel_identity_resolution"></a>

# qca.forward.types.channel\_identity\_resolution

<a id="qca.forward.types.channel_identity_resolution.ChannelIdentityResolution"></a>

## ChannelIdentityResolution

```python
class ChannelIdentityResolution(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/channel_identity_resolution.py)

<a id="qca.forward.types.channel_identity_resolution.ChannelIdentityResolution.mode"></a>

#### mode

<a id="qca.forward.types.channel_list_params"></a>

# qca.forward.types.channel\_list\_params

<a id="qca.forward.types.channel_list_params.ChannelListParams"></a>

## ChannelListParams

```python
class ChannelListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/channel_list_params.py)

<a id="qca.forward.types.channel_list_params.ChannelListParams.channel_type"></a>

#### channel\_type

<a id="qca.forward.types.channel_list_params.ChannelListParams.enabled"></a>

#### enabled

<a id="qca.forward.types.channel_list_params.ChannelListParams.binding_status"></a>

#### binding\_status

<a id="qca.forward.types.channel_list_params.ChannelListParams.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.channel_list_params.ChannelListParams.template_id"></a>

#### template\_id

<a id="qca.forward.types.channel_list_params.ChannelListParams.limit"></a>

#### limit

<a id="qca.forward.types.channel_list_params.ChannelListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.channel_list_params.ChannelListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.channel_pairing"></a>

# qca.forward.types.channel\_pairing

<a id="qca.forward.types.channel_pairing.ChannelPairing"></a>

## ChannelPairing

```python
class ChannelPairing(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/channel_pairing.py)

<a id="qca.forward.types.channel_pairing.ChannelPairing.id"></a>

#### id

<a id="qca.forward.types.channel_pairing.ChannelPairing.type"></a>

#### type

<a id="qca.forward.types.channel_pairing.ChannelPairing.channel_id"></a>

#### channel\_id

<a id="qca.forward.types.channel_pairing.ChannelPairing.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.channel_pairing.ChannelPairing.template_id"></a>

#### template\_id

<a id="qca.forward.types.channel_pairing.ChannelPairing.status"></a>

#### status

<a id="qca.forward.types.channel_pairing.ChannelPairing.paired_at"></a>

#### paired\_at

<a id="qca.forward.types.channel_pairing_create_params"></a>

# qca.forward.types.channel\_pairing\_create\_params

<a id="qca.forward.types.channel_pairing_create_params.ChannelPairingCreateParams"></a>

## ChannelPairingCreateParams

```python
class ChannelPairingCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/channel_pairing_create_params.py)

<a id="qca.forward.types.channel_pairing_create_params.ChannelPairingCreateParams.code"></a>

#### code

<a id="qca.forward.types.channel_pairing_create_params.ChannelPairingCreateParams.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.channel_pairing_create_params.ChannelPairingCreateParams.template_id"></a>

#### template\_id

<a id="qca.forward.types.channel_pairing_create_params.ChannelPairingCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.channel_qr_session"></a>

# qca.forward.types.channel\_qr\_session

<a id="qca.forward.types.channel_qr_session.ChannelQRSession"></a>

## ChannelQRSession

```python
class ChannelQRSession(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/channel_qr_session.py)

<a id="qca.forward.types.channel_qr_session.ChannelQRSession.session_key"></a>

#### session\_key

<a id="qca.forward.types.channel_qr_session.ChannelQRSession.channel_id"></a>

#### channel\_id

<a id="qca.forward.types.channel_qr_session.ChannelQRSession.channel_type"></a>

#### channel\_type

<a id="qca.forward.types.channel_qr_session.ChannelQRSession.status"></a>

#### status

<a id="qca.forward.types.channel_qr_session.ChannelQRSession.qr_code_content"></a>

#### qr\_code\_content

<a id="qca.forward.types.channel_qr_session.ChannelQRSession.qr_code_image_base64"></a>

#### qr\_code\_image\_base64

<a id="qca.forward.types.channel_qr_session.ChannelQRSession.expires_at"></a>

#### expires\_at

<a id="qca.forward.types.channel_qr_session.ChannelQRSession.err_code"></a>

#### err\_code

<a id="qca.forward.types.channel_qr_session.ChannelQRSession.err_msg"></a>

#### err\_msg

<a id="qca.forward.types.channel_qr_session_create_params"></a>

# qca.forward.types.channel\_qr\_session\_create\_params

<a id="qca.forward.types.channel_qr_session_create_params.ChannelQRSessionCreateParams"></a>

## ChannelQRSessionCreateParams

```python
class ChannelQRSessionCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/channel_qr_session_create_params.py)

<a id="qca.forward.types.channel_qr_session_create_params.ChannelQRSessionCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.channel_update_params"></a>

# qca.forward.types.channel\_update\_params

<a id="qca.forward.types.channel_update_params.ChannelUpdateParams"></a>

## ChannelUpdateParams

```python
class ChannelUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/channel_update_params.py)

<a id="qca.forward.types.channel_update_params.ChannelUpdateParams.name"></a>

#### name

<a id="qca.forward.types.channel_update_params.ChannelUpdateParams.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.channel_update_params.ChannelUpdateParams.template_id"></a>

#### template\_id

<a id="qca.forward.types.channel_update_params.ChannelUpdateParams.enabled"></a>

#### enabled

<a id="qca.forward.types.channel_update_params.ChannelUpdateParams.channel_config"></a>

#### channel\_config

<a id="qca.forward.types.channel_update_params.ChannelUpdateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.content_block_param"></a>

# qca.forward.types.content\_block\_param

<a id="qca.forward.types.content_block_param.ContentBlockParam"></a>

## ContentBlockParam

```python
class ContentBlockParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/content_block_param.py)

<a id="qca.forward.types.content_block_param.ContentBlockParam.type"></a>

#### type

<a id="qca.forward.types.content_block_param.ContentBlockParam.text"></a>

#### text

<a id="qca.forward.types.content_block_param.ContentBlockParam.thinking"></a>

#### thinking

<a id="qca.forward.types.content_block_param.ContentBlockParam.source"></a>

#### source

<a id="qca.forward.types.deleted_channel"></a>

# qca.forward.types.deleted\_channel

<a id="qca.forward.types.deleted_channel.DeletedChannel"></a>

## DeletedChannel

```python
class DeletedChannel(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/deleted_channel.py)

<a id="qca.forward.types.deleted_channel.DeletedChannel.id"></a>

#### id

<a id="qca.forward.types.deleted_channel.DeletedChannel.deleted"></a>

#### deleted

<a id="qca.forward.types.deleted_channel_pairing"></a>

# qca.forward.types.deleted\_channel\_pairing

<a id="qca.forward.types.deleted_channel_pairing.DeletedChannelPairing"></a>

## DeletedChannelPairing

```python
class DeletedChannelPairing(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/deleted_channel_pairing.py)

<a id="qca.forward.types.deleted_channel_pairing.DeletedChannelPairing.id"></a>

#### id

<a id="qca.forward.types.deleted_channel_pairing.DeletedChannelPairing.deleted"></a>

#### deleted

<a id="qca.forward.types.deleted_identity"></a>

# qca.forward.types.deleted\_identity

<a id="qca.forward.types.deleted_identity.DeletedIdentity"></a>

## DeletedIdentity

```python
class DeletedIdentity(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/deleted_identity.py)

<a id="qca.forward.types.deleted_identity.DeletedIdentity.id"></a>

#### id

<a id="qca.forward.types.deleted_identity.DeletedIdentity.deleted"></a>

#### deleted

<a id="qca.forward.types.deleted_memory"></a>

# qca.forward.types.deleted\_memory

<a id="qca.forward.types.deleted_memory.DeletedMemory"></a>

## DeletedMemory

```python
class DeletedMemory(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/deleted_memory.py)

<a id="qca.forward.types.deleted_memory.DeletedMemory.id"></a>

#### id

<a id="qca.forward.types.deleted_memory.DeletedMemory.type"></a>

#### type

<a id="qca.forward.types.deleted_memory.DeletedMemory.deleted"></a>

#### deleted

<a id="qca.forward.types.deleted_memory_store"></a>

# qca.forward.types.deleted\_memory\_store

<a id="qca.forward.types.deleted_memory_store.DeletedMemoryStore"></a>

## DeletedMemoryStore

```python
class DeletedMemoryStore(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/deleted_memory_store.py)

<a id="qca.forward.types.deleted_memory_store.DeletedMemoryStore.id"></a>

#### id

<a id="qca.forward.types.deleted_memory_store.DeletedMemoryStore.type"></a>

#### type

<a id="qca.forward.types.deleted_memory_store.DeletedMemoryStore.deleted"></a>

#### deleted

<a id="qca.forward.types.deleted_memory_store_mount"></a>

# qca.forward.types.deleted\_memory\_store\_mount

<a id="qca.forward.types.deleted_memory_store_mount.DeletedMemoryStoreMount"></a>

## DeletedMemoryStoreMount

```python
class DeletedMemoryStoreMount(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/deleted_memory_store_mount.py)

<a id="qca.forward.types.deleted_memory_store_mount.DeletedMemoryStoreMount.id"></a>

#### id

<a id="qca.forward.types.deleted_memory_store_mount.DeletedMemoryStoreMount.type"></a>

#### type

<a id="qca.forward.types.deleted_memory_store_mount.DeletedMemoryStoreMount.deleted"></a>

#### deleted

<a id="qca.forward.types.deleted_skill_version"></a>

# qca.forward.types.deleted\_skill\_version

<a id="qca.forward.types.deleted_skill_version.DeletedSkillVersion"></a>

## DeletedSkillVersion

```python
class DeletedSkillVersion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/deleted_skill_version.py)

<a id="qca.forward.types.deleted_skill_version.DeletedSkillVersion.id"></a>

#### id

<a id="qca.forward.types.deleted_skill_version.DeletedSkillVersion.type"></a>

#### type

<a id="qca.forward.types.deleted_skill_version.DeletedSkillVersion.deleted"></a>

#### deleted

<a id="qca.forward.types.effective_config"></a>

# qca.forward.types.effective\_config

<a id="qca.forward.types.effective_config.EffectiveConfig"></a>

## EffectiveConfig

```python
class EffectiveConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/effective_config.py)

<a id="qca.forward.types.effective_config.EffectiveConfig.type"></a>

#### type

<a id="qca.forward.types.effective_config.EffectiveConfig.agent_effective_hash"></a>

#### agent\_effective\_hash

<a id="qca.forward.types.effective_config.EffectiveConfig.session_effective_hash"></a>

#### session\_effective\_hash

<a id="qca.forward.types.effective_config.EffectiveConfig.effective_hash"></a>

#### effective\_hash

<a id="qca.forward.types.effective_config.EffectiveConfig.agent"></a>

#### agent

<a id="qca.forward.types.effective_config.EffectiveConfig.session"></a>

#### session

<a id="qca.forward.types.effective_config.EffectiveConfig.id"></a>

#### id

<a id="qca.forward.types.effective_config.EffectiveConfig.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.effective_config.EffectiveConfig.template_id"></a>

#### template\_id

<a id="qca.forward.types.effective_config_agent"></a>

# qca.forward.types.effective\_config\_agent

<a id="qca.forward.types.effective_config_agent.EffectiveConfigAgent"></a>

## EffectiveConfigAgent

```python
class EffectiveConfigAgent(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/effective_config_agent.py)

<a id="qca.forward.types.effective_config_agent.EffectiveConfigAgent.model"></a>

#### model

<a id="qca.forward.types.effective_config_agent.EffectiveConfigAgent.system"></a>

#### system

<a id="qca.forward.types.effective_config_agent.EffectiveConfigAgent.tools"></a>

#### tools

<a id="qca.forward.types.effective_config_agent.EffectiveConfigAgent.mcp_servers"></a>

#### mcp\_servers

<a id="qca.forward.types.effective_config_agent.EffectiveConfigAgent.skills"></a>

#### skills

<a id="qca.forward.types.effective_config_agent_tools_item"></a>

# qca.forward.types.effective\_config\_agent\_tools\_item

<a id="qca.forward.types.effective_config_agent_tools_item.EffectiveConfigAgentToolsItem"></a>

## EffectiveConfigAgentToolsItem

```python
class EffectiveConfigAgentToolsItem(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/effective_config_agent_tools_item.py)

<a id="qca.forward.types.effective_config_agent_tools_item.EffectiveConfigAgentToolsItem.type"></a>

#### type

<a id="qca.forward.types.effective_config_agent_tools_item.EffectiveConfigAgentToolsItem.configs"></a>

#### configs

<a id="qca.forward.types.effective_config_agent_tools_item_configs_item"></a>

# qca.forward.types.effective\_config\_agent\_tools\_item\_configs\_item

<a id="qca.forward.types.effective_config_agent_tools_item_configs_item.EffectiveConfigAgentToolsItemConfigsItem"></a>

## EffectiveConfigAgentToolsItemConfigsItem

```python
class EffectiveConfigAgentToolsItemConfigsItem(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/effective_config_agent_tools_item_configs_item.py)

<a id="qca.forward.types.effective_config_agent_tools_item_configs_item.EffectiveConfigAgentToolsItemConfigsItem.name"></a>

#### name

<a id="qca.forward.types.effective_config_agent_tools_item_configs_item.EffectiveConfigAgentToolsItemConfigsItem.enabled"></a>

#### enabled

<a id="qca.forward.types.effective_config_session"></a>

# qca.forward.types.effective\_config\_session

<a id="qca.forward.types.effective_config_session.EffectiveConfigSession"></a>

## EffectiveConfigSession

```python
class EffectiveConfigSession(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/effective_config_session.py)

<a id="qca.forward.types.effective_config_session.EffectiveConfigSession.environment_id"></a>

#### environment\_id

<a id="qca.forward.types.effective_config_session.EffectiveConfigSession.environment_variables"></a>

#### environment\_variables

<a id="qca.forward.types.effective_config_session.EffectiveConfigSession.vault_ids"></a>

#### vault\_ids

<a id="qca.forward.types.effective_config_session.EffectiveConfigSession.resources"></a>

#### resources

<a id="qca.forward.types.effective_config_session_resources_item"></a>

# qca.forward.types.effective\_config\_session\_resources\_item

<a id="qca.forward.types.effective_config_session_resources_item.EffectiveConfigSessionResourcesItem"></a>

## EffectiveConfigSessionResourcesItem

```python
class EffectiveConfigSessionResourcesItem(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/effective_config_session_resources_item.py)

<a id="qca.forward.types.effective_config_session_resources_item.EffectiveConfigSessionResourcesItem.type"></a>

#### type

<a id="qca.forward.types.effective_config_session_resources_item.EffectiveConfigSessionResourcesItem.file_id"></a>

#### file\_id

<a id="qca.forward.types.effective_config_session_resources_item.EffectiveConfigSessionResourcesItem.url"></a>

#### url

<a id="qca.forward.types.effective_config_session_resources_item.EffectiveConfigSessionResourcesItem.mount_path"></a>

#### mount\_path

<a id="qca.forward.types.environment"></a>

# qca.forward.types.environment

<a id="qca.forward.types.environment.Environment"></a>

## Environment

```python
class Environment(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/environment.py)

<a id="qca.forward.types.environment.Environment.id"></a>

#### id

<a id="qca.forward.types.environment.Environment.type"></a>

#### type

<a id="qca.forward.types.environment.Environment.name"></a>

#### name

<a id="qca.forward.types.environment.Environment.description"></a>

#### description

<a id="qca.forward.types.environment.Environment.config"></a>

#### config

<a id="qca.forward.types.environment.Environment.metadata"></a>

#### metadata

<a id="qca.forward.types.environment.Environment.created_at"></a>

#### created\_at

<a id="qca.forward.types.environment.Environment.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.environment.Environment.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.environment.Environment.archived_at"></a>

#### archived\_at

<a id="qca.forward.types.environment_config"></a>

# qca.forward.types.environment\_config

<a id="qca.forward.types.environment_config.EnvironmentConfig"></a>

## EnvironmentConfig

```python
class EnvironmentConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/environment_config.py)

<a id="qca.forward.types.environment_config.EnvironmentConfig.type"></a>

#### type

<a id="qca.forward.types.environment_config.EnvironmentConfig.packages"></a>

#### packages

<a id="qca.forward.types.environment_config_packages"></a>

# qca.forward.types.environment\_config\_packages

<a id="qca.forward.types.environment_config_packages.EnvironmentConfigPackages"></a>

## EnvironmentConfigPackages

```python
class EnvironmentConfigPackages(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/environment_config_packages.py)

<a id="qca.forward.types.environment_config_packages.EnvironmentConfigPackages.type"></a>

#### type

<a id="qca.forward.types.environment_config_packages.EnvironmentConfigPackages.apt"></a>

#### apt

<a id="qca.forward.types.environment_config_packages.EnvironmentConfigPackages.cargo"></a>

#### cargo

<a id="qca.forward.types.environment_config_packages.EnvironmentConfigPackages.gem"></a>

#### gem

<a id="qca.forward.types.environment_config_packages.EnvironmentConfigPackages.go"></a>

#### go

<a id="qca.forward.types.environment_config_packages.EnvironmentConfigPackages.npm"></a>

#### npm

<a id="qca.forward.types.environment_config_packages.EnvironmentConfigPackages.pip"></a>

#### pip

<a id="qca.forward.types.environment_create_params"></a>

# qca.forward.types.environment\_create\_params

<a id="qca.forward.types.environment_create_params.EnvironmentCreateParams"></a>

## EnvironmentCreateParams

```python
class EnvironmentCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/environment_create_params.py)

<a id="qca.forward.types.environment_create_params.EnvironmentCreateParams.name"></a>

#### name

<a id="qca.forward.types.environment_create_params.EnvironmentCreateParams.description"></a>

#### description

<a id="qca.forward.types.environment_create_params.EnvironmentCreateParams.config"></a>

#### config

<a id="qca.forward.types.environment_create_params.EnvironmentCreateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.environment_create_params.EnvironmentCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.environment_list_params"></a>

# qca.forward.types.environment\_list\_params

<a id="qca.forward.types.environment_list_params.EnvironmentListParams"></a>

## EnvironmentListParams

```python
class EnvironmentListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/environment_list_params.py)

<a id="qca.forward.types.environment_list_params.EnvironmentListParams.limit"></a>

#### limit

<a id="qca.forward.types.environment_list_params.EnvironmentListParams.page"></a>

#### page

<a id="qca.forward.types.environment_list_params.EnvironmentListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.environment_list_params.EnvironmentListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.environment_update_params"></a>

# qca.forward.types.environment\_update\_params

<a id="qca.forward.types.environment_update_params.EnvironmentUpdateParams"></a>

## EnvironmentUpdateParams

```python
class EnvironmentUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/environment_update_params.py)

<a id="qca.forward.types.environment_update_params.EnvironmentUpdateParams.name"></a>

#### name

<a id="qca.forward.types.environment_update_params.EnvironmentUpdateParams.description"></a>

#### description

<a id="qca.forward.types.environment_update_params.EnvironmentUpdateParams.config"></a>

#### config

<a id="qca.forward.types.environment_update_params.EnvironmentUpdateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.environment_variable_override"></a>

# qca.forward.types.environment\_variable\_override

<a id="qca.forward.types.environment_variable_override.EnvironmentVariableOverride"></a>

## EnvironmentVariableOverride

```python
class EnvironmentVariableOverride(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/environment_variable_override.py)

<a id="qca.forward.types.environment_variable_override.EnvironmentVariableOverride.op"></a>

#### op

<a id="qca.forward.types.environment_variable_override.EnvironmentVariableOverride.value"></a>

#### value

<a id="qca.forward.types.environment_variable_override_param"></a>

# qca.forward.types.environment\_variable\_override\_param

<a id="qca.forward.types.environment_variable_override_param.EnvironmentVariableOverrideParam"></a>

## EnvironmentVariableOverrideParam

```python
class EnvironmentVariableOverrideParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/environment_variable_override_param.py)

<a id="qca.forward.types.environment_variable_override_param.EnvironmentVariableOverrideParam.op"></a>

#### op

<a id="qca.forward.types.environment_variable_override_param.EnvironmentVariableOverrideParam.value"></a>

#### value

<a id="qca.forward.types.file_list_params"></a>

# qca.forward.types.file\_list\_params

<a id="qca.forward.types.file_list_params.FileListParams"></a>

## FileListParams

```python
class FileListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/file_list_params.py)

<a id="qca.forward.types.file_list_params.FileListParams.limit"></a>

#### limit

<a id="qca.forward.types.file_list_params.FileListParams.page"></a>

#### page

<a id="qca.forward.types.file_list_params.FileListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.file_list_params.FileListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.file_list_params.FileListParams.name"></a>

#### name

<a id="qca.forward.types.file_list_params.FileListParams.scope_id"></a>

#### scope\_id

<a id="qca.forward.types.file_metadata"></a>

# qca.forward.types.file\_metadata

<a id="qca.forward.types.file_metadata.FileMetadata"></a>

## FileMetadata

```python
class FileMetadata(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/file_metadata.py)

<a id="qca.forward.types.file_metadata.FileMetadata.id"></a>

#### id

<a id="qca.forward.types.file_metadata.FileMetadata.type"></a>

#### type

<a id="qca.forward.types.file_metadata.FileMetadata.filename"></a>

#### filename

<a id="qca.forward.types.file_metadata.FileMetadata.size_bytes"></a>

#### size\_bytes

<a id="qca.forward.types.file_metadata.FileMetadata.mime_type"></a>

#### mime\_type

<a id="qca.forward.types.file_metadata.FileMetadata.created_at"></a>

#### created\_at

<a id="qca.forward.types.file_metadata.FileMetadata.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.file_metadata.FileMetadata.downloadable"></a>

#### downloadable

<a id="qca.forward.types.file_metadata.FileMetadata.scope"></a>

#### scope

<a id="qca.forward.types.file_metadata.FileMetadata.metadata"></a>

#### metadata

<a id="qca.forward.types.file_metadata.FileMetadata.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.file_upload_params"></a>

# qca.forward.types.file\_upload\_params

<a id="qca.forward.types.file_upload_params.FileUploadParams"></a>

## FileUploadParams

```python
class FileUploadParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/file_upload_params.py)

<a id="qca.forward.types.file_upload_params.FileUploadParams.file"></a>

#### file

<a id="qca.forward.types.file_upload_params.FileUploadParams.name"></a>

#### name

<a id="qca.forward.types.file_upload_params.FileUploadParams.purpose"></a>

#### purpose

<a id="qca.forward.types.file_upload_params.FileUploadParams.metadata"></a>

#### metadata

<a id="qca.forward.types.file_upload_params.FileUploadParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.git_hub_repository"></a>

# qca.forward.types.git\_hub\_repository

<a id="qca.forward.types.git_hub_repository.GitHubRepository"></a>

## GitHubRepository

```python
class GitHubRepository(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/git_hub_repository.py)

<a id="qca.forward.types.git_hub_repository.GitHubRepository.url"></a>

#### url

<a id="qca.forward.types.git_hub_repository.GitHubRepository.mount_path"></a>

#### mount\_path

<a id="qca.forward.types.git_hub_repository.GitHubRepository.enabled"></a>

#### enabled

<a id="qca.forward.types.git_hub_repository_param"></a>

# qca.forward.types.git\_hub\_repository\_param

<a id="qca.forward.types.git_hub_repository_param.GitHubRepositoryParam"></a>

## GitHubRepositoryParam

```python
class GitHubRepositoryParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/git_hub_repository_param.py)

<a id="qca.forward.types.git_hub_repository_param.GitHubRepositoryParam.url"></a>

#### url

<a id="qca.forward.types.git_hub_repository_param.GitHubRepositoryParam.mount_path"></a>

#### mount\_path

<a id="qca.forward.types.git_hub_repository_param.GitHubRepositoryParam.enabled"></a>

#### enabled

<a id="qca.forward.types.git_hub_repository_param.GitHubRepositoryParam.authorization_token"></a>

#### authorization\_token

<a id="qca.forward.types.identity"></a>

# qca.forward.types.identity

<a id="qca.forward.types.identity.Identity"></a>

## Identity

```python
class Identity(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity.py)

<a id="qca.forward.types.identity.Identity.id"></a>

#### id

<a id="qca.forward.types.identity.Identity.external_id"></a>

#### external\_id

<a id="qca.forward.types.identity.Identity.name"></a>

#### name

<a id="qca.forward.types.identity.Identity.identity_type"></a>

#### identity\_type

<a id="qca.forward.types.identity.Identity.enabled"></a>

#### enabled

<a id="qca.forward.types.identity.Identity.metadata"></a>

#### metadata

<a id="qca.forward.types.identity.Identity.created_at"></a>

#### created\_at

<a id="qca.forward.types.identity.Identity.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.identity_clear_params"></a>

# qca.forward.types.identity\_clear\_params

<a id="qca.forward.types.identity_clear_params.IdentityClearParams"></a>

## IdentityClearParams

```python
class IdentityClearParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_clear_params.py)

<a id="qca.forward.types.identity_clear_params.IdentityClearParams.reason"></a>

#### reason

<a id="qca.forward.types.identity_clear_response"></a>

# qca.forward.types.identity\_clear\_response

<a id="qca.forward.types.identity_clear_response.IdentityClearResponse"></a>

## IdentityClearResponse

```python
class IdentityClearResponse(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_clear_response.py)

<a id="qca.forward.types.identity_clear_response.IdentityClearResponse.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.identity_clear_response.IdentityClearResponse.status"></a>

#### status

<a id="qca.forward.types.identity_clear_response.IdentityClearResponse.completed_at"></a>

#### completed\_at

<a id="qca.forward.types.identity_clear_response.IdentityClearResponse.summary"></a>

#### summary

<a id="qca.forward.types.identity_clear_response_summary"></a>

# qca.forward.types.identity\_clear\_response\_summary

<a id="qca.forward.types.identity_clear_response_summary.IdentityClearResponseSummary"></a>

## IdentityClearResponseSummary

```python
class IdentityClearResponseSummary(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_clear_response_summary.py)

<a id="qca.forward.types.identity_clear_response_summary.IdentityClearResponseSummary.identity_configs_archived"></a>

#### identity\_configs\_archived

<a id="qca.forward.types.identity_clear_response_summary.IdentityClearResponseSummary.resource_bindings_archived"></a>

#### resource\_bindings\_archived

<a id="qca.forward.types.identity_clear_response_summary.IdentityClearResponseSummary.identity_owned_resources_archived"></a>

#### identity\_owned\_resources\_archived

<a id="qca.forward.types.identity_clear_response_summary.IdentityClearResponseSummary.schedules_archived"></a>

#### schedules\_archived

<a id="qca.forward.types.identity_clear_response_summary.IdentityClearResponseSummary.schedule_runs_skipped"></a>

#### schedule\_runs\_skipped

<a id="qca.forward.types.identity_clear_response_summary.IdentityClearResponseSummary.sessions_archived"></a>

#### sessions\_archived

<a id="qca.forward.types.identity_config"></a>

# qca.forward.types.identity\_config

<a id="qca.forward.types.identity_config.IdentityConfig"></a>

## IdentityConfig

```python
class IdentityConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_config.py)

<a id="qca.forward.types.identity_config.IdentityConfig.type"></a>

#### type

<a id="qca.forward.types.identity_config.IdentityConfig.id"></a>

#### id

<a id="qca.forward.types.identity_config.IdentityConfig.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.identity_config.IdentityConfig.template_id"></a>

#### template\_id

<a id="qca.forward.types.identity_config.IdentityConfig.name"></a>

#### name

<a id="qca.forward.types.identity_config.IdentityConfig.status"></a>

#### status

<a id="qca.forward.types.identity_config.IdentityConfig.effective_hash"></a>

#### effective\_hash

<a id="qca.forward.types.identity_config.IdentityConfig.created_at"></a>

#### created\_at

<a id="qca.forward.types.identity_config.IdentityConfig.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.identity_config.IdentityConfig.identity_config"></a>

#### identity\_config

<a id="qca.forward.types.identity_config.IdentityConfig.metadata"></a>

#### metadata

<a id="qca.forward.types.identity_config_list_params"></a>

# qca.forward.types.identity\_config\_list\_params

<a id="qca.forward.types.identity_config_list_params.IdentityConfigListParams"></a>

## IdentityConfigListParams

```python
class IdentityConfigListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_config_list_params.py)

<a id="qca.forward.types.identity_config_list_params.IdentityConfigListParams.template_id"></a>

#### template\_id

<a id="qca.forward.types.identity_config_list_params.IdentityConfigListParams.status"></a>

#### status

<a id="qca.forward.types.identity_config_list_params.IdentityConfigListParams.limit"></a>

#### limit

<a id="qca.forward.types.identity_config_list_params.IdentityConfigListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.identity_config_list_params.IdentityConfigListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.identity_config_spec"></a>

# qca.forward.types.identity\_config\_spec

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec"></a>

## IdentityConfigSpec

```python
class IdentityConfigSpec(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_config_spec.py)

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec.system"></a>

#### system

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec.model"></a>

#### model

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec.tools"></a>

#### tools

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec.mcp_servers"></a>

#### mcp\_servers

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec.skills"></a>

#### skills

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec.toolsets"></a>

#### toolsets

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec.agent_metadata"></a>

#### agent\_metadata

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec.vaults"></a>

#### vaults

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec.files"></a>

#### files

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec.github_repositories"></a>

#### github\_repositories

<a id="qca.forward.types.identity_config_spec.IdentityConfigSpec.environment_variables"></a>

#### environment\_variables

<a id="qca.forward.types.identity_config_spec_param"></a>

# qca.forward.types.identity\_config\_spec\_param

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam"></a>

## IdentityConfigSpecParam

```python
class IdentityConfigSpecParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_config_spec_param.py)

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam.system"></a>

#### system

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam.model"></a>

#### model

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam.tools"></a>

#### tools

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam.mcp_servers"></a>

#### mcp\_servers

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam.skills"></a>

#### skills

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam.toolsets"></a>

#### toolsets

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam.agent_metadata"></a>

#### agent\_metadata

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam.vaults"></a>

#### vaults

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam.files"></a>

#### files

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam.github_repositories"></a>

#### github\_repositories

<a id="qca.forward.types.identity_config_spec_param.IdentityConfigSpecParam.environment_variables"></a>

#### environment\_variables

<a id="qca.forward.types.identity_config_upsert_params"></a>

# qca.forward.types.identity\_config\_upsert\_params

<a id="qca.forward.types.identity_config_upsert_params.IdentityConfigUpsertParams"></a>

## IdentityConfigUpsertParams

```python
class IdentityConfigUpsertParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_config_upsert_params.py)

<a id="qca.forward.types.identity_config_upsert_params.IdentityConfigUpsertParams.name"></a>

#### name

<a id="qca.forward.types.identity_config_upsert_params.IdentityConfigUpsertParams.identity_config"></a>

#### identity\_config

<a id="qca.forward.types.identity_config_upsert_params.IdentityConfigUpsertParams.metadata"></a>

#### metadata

<a id="qca.forward.types.identity_config_upsert_params.IdentityConfigUpsertParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.identity_create_params"></a>

# qca.forward.types.identity\_create\_params

<a id="qca.forward.types.identity_create_params.IdentityCreateParams"></a>

## IdentityCreateParams

```python
class IdentityCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_create_params.py)

<a id="qca.forward.types.identity_create_params.IdentityCreateParams.external_id"></a>

#### external\_id

<a id="qca.forward.types.identity_create_params.IdentityCreateParams.name"></a>

#### name

<a id="qca.forward.types.identity_create_params.IdentityCreateParams.enabled"></a>

#### enabled

<a id="qca.forward.types.identity_create_params.IdentityCreateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.identity_create_params.IdentityCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.identity_list_params"></a>

# qca.forward.types.identity\_list\_params

<a id="qca.forward.types.identity_list_params.IdentityListParams"></a>

## IdentityListParams

```python
class IdentityListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_list_params.py)

<a id="qca.forward.types.identity_list_params.IdentityListParams.external_id"></a>

#### external\_id

<a id="qca.forward.types.identity_list_params.IdentityListParams.identity_i_ds"></a>

#### identity\_i\_ds

<a id="qca.forward.types.identity_list_params.IdentityListParams.search"></a>

#### search

<a id="qca.forward.types.identity_list_params.IdentityListParams.enabled"></a>

#### enabled

<a id="qca.forward.types.identity_list_params.IdentityListParams.limit"></a>

#### limit

<a id="qca.forward.types.identity_list_params.IdentityListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.identity_list_params.IdentityListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.identity_list_templates_response"></a>

# qca.forward.types.identity\_list\_templates\_response

<a id="qca.forward.types.identity_list_templates_response.IdentityListTemplatesResponse"></a>

## IdentityListTemplatesResponse

```python
class IdentityListTemplatesResponse(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_list_templates_response.py)

<a id="qca.forward.types.identity_list_templates_response.IdentityListTemplatesResponse.data"></a>

#### data

<a id="qca.forward.types.identity_memory_store_list_response"></a>

# qca.forward.types.identity\_memory\_store\_list\_response

<a id="qca.forward.types.identity_memory_store_list_response.IdentityMemoryStoreListResponse"></a>

## IdentityMemoryStoreListResponse

```python
class IdentityMemoryStoreListResponse(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_memory_store_list_response.py)

<a id="qca.forward.types.identity_memory_store_list_response.IdentityMemoryStoreListResponse.data"></a>

#### data

<a id="qca.forward.types.identity_memory_store_list_response.IdentityMemoryStoreListResponse.has_more"></a>

#### has\_more

<a id="qca.forward.types.identity_memory_store_mount_params"></a>

# qca.forward.types.identity\_memory\_store\_mount\_params

<a id="qca.forward.types.identity_memory_store_mount_params.IdentityMemoryStoreMountParams"></a>

## IdentityMemoryStoreMountParams

```python
class IdentityMemoryStoreMountParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_memory_store_mount_params.py)

<a id="qca.forward.types.identity_memory_store_mount_params.IdentityMemoryStoreMountParams.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.forward.types.identity_stats"></a>

# qca.forward.types.identity\_stats

<a id="qca.forward.types.identity_stats.IdentityStats"></a>

## IdentityStats

```python
class IdentityStats(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_stats.py)

<a id="qca.forward.types.identity_stats.IdentityStats.total_identities"></a>

#### total\_identities

<a id="qca.forward.types.identity_stats.IdentityStats.active_identities"></a>

#### active\_identities

<a id="qca.forward.types.identity_stats.IdentityStats.total_agents"></a>

#### total\_agents

<a id="qca.forward.types.identity_stats.IdentityStats.total_sessions"></a>

#### total\_sessions

<a id="qca.forward.types.identity_template"></a>

# qca.forward.types.identity\_template

<a id="qca.forward.types.identity_template.IdentityTemplate"></a>

## IdentityTemplate

```python
class IdentityTemplate(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_template.py)

<a id="qca.forward.types.identity_template.IdentityTemplate.template_id"></a>

#### template\_id

<a id="qca.forward.types.identity_template.IdentityTemplate.template_name"></a>

#### template\_name

<a id="qca.forward.types.identity_template.IdentityTemplate.session_count"></a>

#### session\_count

<a id="qca.forward.types.identity_template.IdentityTemplate.last_active_at"></a>

#### last\_active\_at

<a id="qca.forward.types.identity_update_params"></a>

# qca.forward.types.identity\_update\_params

<a id="qca.forward.types.identity_update_params.IdentityUpdateParams"></a>

## IdentityUpdateParams

```python
class IdentityUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/identity_update_params.py)

<a id="qca.forward.types.identity_update_params.IdentityUpdateParams.external_id"></a>

#### external\_id

<a id="qca.forward.types.identity_update_params.IdentityUpdateParams.name"></a>

#### name

<a id="qca.forward.types.identity_update_params.IdentityUpdateParams.enabled"></a>

#### enabled

<a id="qca.forward.types.identity_update_params.IdentityUpdateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.identity_update_params.IdentityUpdateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.image_source_param"></a>

# qca.forward.types.image\_source\_param

<a id="qca.forward.types.image_source_param.ImageSourceParam"></a>

## ImageSourceParam

```python
class ImageSourceParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/image_source_param.py)

<a id="qca.forward.types.image_source_param.ImageSourceParam.type"></a>

#### type

<a id="qca.forward.types.image_source_param.ImageSourceParam.media_type"></a>

#### media\_type

<a id="qca.forward.types.image_source_param.ImageSourceParam.data"></a>

#### data

<a id="qca.forward.types.image_source_param.ImageSourceParam.url"></a>

#### url

<a id="qca.forward.types.image_source_param.ImageSourceParam.file_id"></a>

#### file\_id

<a id="qca.forward.types.mcp_server"></a>

# qca.forward.types.mcp\_server

<a id="qca.forward.types.mcp_server.MCPServer"></a>

## MCPServer

```python
class MCPServer(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/mcp_server.py)

<a id="qca.forward.types.mcp_server.MCPServer.type"></a>

#### type

<a id="qca.forward.types.mcp_server.MCPServer.name"></a>

#### name

<a id="qca.forward.types.mcp_server.MCPServer.url"></a>

#### url

<a id="qca.forward.types.mcp_server_override"></a>

# qca.forward.types.mcp\_server\_override

<a id="qca.forward.types.mcp_server_override.MCPServerOverride"></a>

## MCPServerOverride

```python
class MCPServerOverride(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/mcp_server_override.py)

<a id="qca.forward.types.mcp_server_override.MCPServerOverride.enabled"></a>

#### enabled

<a id="qca.forward.types.mcp_server_override.MCPServerOverride.type"></a>

#### type

<a id="qca.forward.types.mcp_server_override.MCPServerOverride.url"></a>

#### url

<a id="qca.forward.types.mcp_server_override_param"></a>

# qca.forward.types.mcp\_server\_override\_param

<a id="qca.forward.types.mcp_server_override_param.MCPServerOverrideParam"></a>

## MCPServerOverrideParam

```python
class MCPServerOverrideParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/mcp_server_override_param.py)

<a id="qca.forward.types.mcp_server_override_param.MCPServerOverrideParam.enabled"></a>

#### enabled

<a id="qca.forward.types.mcp_server_override_param.MCPServerOverrideParam.type"></a>

#### type

<a id="qca.forward.types.mcp_server_override_param.MCPServerOverrideParam.url"></a>

#### url

<a id="qca.forward.types.mcp_server_param"></a>

# qca.forward.types.mcp\_server\_param

<a id="qca.forward.types.mcp_server_param.MCPServerParam"></a>

## MCPServerParam

```python
class MCPServerParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/mcp_server_param.py)

<a id="qca.forward.types.mcp_server_param.MCPServerParam.type"></a>

#### type

<a id="qca.forward.types.mcp_server_param.MCPServerParam.name"></a>

#### name

<a id="qca.forward.types.mcp_server_param.MCPServerParam.url"></a>

#### url

<a id="qca.forward.types.memory"></a>

# qca.forward.types.memory

<a id="qca.forward.types.memory.Memory"></a>

## Memory

```python
class Memory(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/memory.py)

<a id="qca.forward.types.memory.Memory.id"></a>

#### id

<a id="qca.forward.types.memory.Memory.type"></a>

#### type

<a id="qca.forward.types.memory.Memory.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.forward.types.memory.Memory.path"></a>

#### path

<a id="qca.forward.types.memory.Memory.content_size_bytes"></a>

#### content\_size\_bytes

<a id="qca.forward.types.memory.Memory.content_sha256"></a>

#### content\_sha256

<a id="qca.forward.types.memory.Memory.metadata"></a>

#### metadata

<a id="qca.forward.types.memory.Memory.created_at"></a>

#### created\_at

<a id="qca.forward.types.memory.Memory.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.memory.Memory.content"></a>

#### content

<a id="qca.forward.types.memory_store"></a>

# qca.forward.types.memory\_store

<a id="qca.forward.types.memory_store.MemoryStore"></a>

## MemoryStore

```python
class MemoryStore(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/memory_store.py)

<a id="qca.forward.types.memory_store.MemoryStore.id"></a>

#### id

<a id="qca.forward.types.memory_store.MemoryStore.type"></a>

#### type

<a id="qca.forward.types.memory_store.MemoryStore.name"></a>

#### name

<a id="qca.forward.types.memory_store.MemoryStore.description"></a>

#### description

<a id="qca.forward.types.memory_store.MemoryStore.status"></a>

#### status

<a id="qca.forward.types.memory_store.MemoryStore.entry_count"></a>

#### entry\_count

<a id="qca.forward.types.memory_store.MemoryStore.total_size"></a>

#### total\_size

<a id="qca.forward.types.memory_store.MemoryStore.metadata"></a>

#### metadata

<a id="qca.forward.types.memory_store.MemoryStore.system_managed"></a>

#### system\_managed

<a id="qca.forward.types.memory_store.MemoryStore.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.memory_store.MemoryStore.created_at"></a>

#### created\_at

<a id="qca.forward.types.memory_store.MemoryStore.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.memory_store.MemoryStore.archived_at"></a>

#### archived\_at

<a id="qca.forward.types.memory_store.MemoryStore.binding_info"></a>

#### binding\_info

<a id="qca.forward.types.memory_store_create_params"></a>

# qca.forward.types.memory\_store\_create\_params

<a id="qca.forward.types.memory_store_create_params.MemoryStoreCreateParams"></a>

## MemoryStoreCreateParams

```python
class MemoryStoreCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/memory_store_create_params.py)

<a id="qca.forward.types.memory_store_create_params.MemoryStoreCreateParams.name"></a>

#### name

<a id="qca.forward.types.memory_store_create_params.MemoryStoreCreateParams.description"></a>

#### description

<a id="qca.forward.types.memory_store_create_params.MemoryStoreCreateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.memory_store_create_params.MemoryStoreCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.memory_store_list_params"></a>

# qca.forward.types.memory\_store\_list\_params

<a id="qca.forward.types.memory_store_list_params.MemoryStoreListParams"></a>

## MemoryStoreListParams

```python
class MemoryStoreListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/memory_store_list_params.py)

<a id="qca.forward.types.memory_store_list_params.MemoryStoreListParams.limit"></a>

#### limit

<a id="qca.forward.types.memory_store_list_params.MemoryStoreListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.memory_store_list_params.MemoryStoreListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.memory_store_list_params.MemoryStoreListParams.system_managed"></a>

#### system\_managed

<a id="qca.forward.types.memory_store_memory_create_params"></a>

# qca.forward.types.memory\_store\_memory\_create\_params

<a id="qca.forward.types.memory_store_memory_create_params.MemoryStoreMemoryCreateParams"></a>

## MemoryStoreMemoryCreateParams

```python
class MemoryStoreMemoryCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/memory_store_memory_create_params.py)

<a id="qca.forward.types.memory_store_memory_create_params.MemoryStoreMemoryCreateParams.path"></a>

#### path

<a id="qca.forward.types.memory_store_memory_create_params.MemoryStoreMemoryCreateParams.content"></a>

#### content

<a id="qca.forward.types.memory_store_memory_create_params.MemoryStoreMemoryCreateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.memory_store_memory_list_params"></a>

# qca.forward.types.memory\_store\_memory\_list\_params

<a id="qca.forward.types.memory_store_memory_list_params.MemoryStoreMemoryListParams"></a>

## MemoryStoreMemoryListParams

```python
class MemoryStoreMemoryListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/memory_store_memory_list_params.py)

<a id="qca.forward.types.memory_store_memory_list_params.MemoryStoreMemoryListParams.limit"></a>

#### limit

<a id="qca.forward.types.memory_store_memory_list_params.MemoryStoreMemoryListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.memory_store_memory_list_params.MemoryStoreMemoryListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.memory_store_memory_list_params.MemoryStoreMemoryListParams.path_prefix"></a>

#### path\_prefix

<a id="qca.forward.types.memory_store_memory_update_params"></a>

# qca.forward.types.memory\_store\_memory\_update\_params

<a id="qca.forward.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams"></a>

## MemoryStoreMemoryUpdateParams

```python
class MemoryStoreMemoryUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/memory_store_memory_update_params.py)

<a id="qca.forward.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams.content"></a>

#### content

<a id="qca.forward.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams.content_sha256"></a>

#### content\_sha256

<a id="qca.forward.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.memory_store_memory_version_list_params"></a>

# qca.forward.types.memory\_store\_memory\_version\_list\_params

<a id="qca.forward.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams"></a>

## MemoryStoreMemoryVersionListParams

```python
class MemoryStoreMemoryVersionListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/memory_store_memory_version_list_params.py)

<a id="qca.forward.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.limit"></a>

#### limit

<a id="qca.forward.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.memory_id"></a>

#### memory\_id

<a id="qca.forward.types.memory_store_mount"></a>

# qca.forward.types.memory\_store\_mount

<a id="qca.forward.types.memory_store_mount.MemoryStoreMount"></a>

## MemoryStoreMount

```python
class MemoryStoreMount(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/memory_store_mount.py)

<a id="qca.forward.types.memory_store_mount.MemoryStoreMount.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.forward.types.memory_store_mount.MemoryStoreMount.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.memory_store_mount.MemoryStoreMount.template_id"></a>

#### template\_id

<a id="qca.forward.types.memory_store_mount.MemoryStoreMount.access"></a>

#### access

<a id="qca.forward.types.memory_store_mount.MemoryStoreMount.system_managed"></a>

#### system\_managed

<a id="qca.forward.types.memory_store_mount.MemoryStoreMount.name"></a>

#### name

<a id="qca.forward.types.memory_store_mount.MemoryStoreMount.status"></a>

#### status

<a id="qca.forward.types.memory_store_mount.MemoryStoreMount.entry_count"></a>

#### entry\_count

<a id="qca.forward.types.memory_store_mount.MemoryStoreMount.created_at"></a>

#### created\_at

<a id="qca.forward.types.memory_store_update_params"></a>

# qca.forward.types.memory\_store\_update\_params

<a id="qca.forward.types.memory_store_update_params.MemoryStoreUpdateParams"></a>

## MemoryStoreUpdateParams

```python
class MemoryStoreUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/memory_store_update_params.py)

<a id="qca.forward.types.memory_store_update_params.MemoryStoreUpdateParams.name"></a>

#### name

<a id="qca.forward.types.memory_store_update_params.MemoryStoreUpdateParams.description"></a>

#### description

<a id="qca.forward.types.memory_store_update_params.MemoryStoreUpdateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.memory_version"></a>

# qca.forward.types.memory\_version

<a id="qca.forward.types.memory_version.MemoryVersion"></a>

## MemoryVersion

```python
class MemoryVersion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/memory_version.py)

<a id="qca.forward.types.memory_version.MemoryVersion.id"></a>

#### id

<a id="qca.forward.types.memory_version.MemoryVersion.type"></a>

#### type

<a id="qca.forward.types.memory_version.MemoryVersion.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.forward.types.memory_version.MemoryVersion.memory_id"></a>

#### memory\_id

<a id="qca.forward.types.memory_version.MemoryVersion.path"></a>

#### path

<a id="qca.forward.types.memory_version.MemoryVersion.content_size_bytes"></a>

#### content\_size\_bytes

<a id="qca.forward.types.memory_version.MemoryVersion.content_sha256"></a>

#### content\_sha256

<a id="qca.forward.types.memory_version.MemoryVersion.operation"></a>

#### operation

<a id="qca.forward.types.memory_version.MemoryVersion.redacted"></a>

#### redacted

<a id="qca.forward.types.memory_version.MemoryVersion.redacted_at"></a>

#### redacted\_at

<a id="qca.forward.types.memory_version.MemoryVersion.created_at"></a>

#### created\_at

<a id="qca.forward.types.memory_version.MemoryVersion.content"></a>

#### content

<a id="qca.forward.types.model"></a>

# qca.forward.types.model

<a id="qca.forward.types.model.Model"></a>

## Model

```python
class Model(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/model.py)

<a id="qca.forward.types.model.Model.id"></a>

#### id

<a id="qca.forward.types.model.Model.display_name"></a>

#### display\_name

<a id="qca.forward.types.model.Model.is_enabled"></a>

#### is\_enabled

<a id="qca.forward.types.model.Model.is_new"></a>

#### is\_new

<a id="qca.forward.types.model.Model.is_vl"></a>

#### is\_vl

<a id="qca.forward.types.model.Model.support_disable_reasoning"></a>

#### support\_disable\_reasoning

<a id="qca.forward.types.model.Model.price_factor"></a>

#### price\_factor

<a id="qca.forward.types.model.Model.efforts"></a>

#### efforts

<a id="qca.forward.types.model.Model.default_effort"></a>

#### default\_effort

<a id="qca.forward.types.model.Model.speed"></a>

#### speed

<a id="qca.forward.types.model.Model.max_input_tokens"></a>

#### max\_input\_tokens

<a id="qca.forward.types.model.Model.default_context_window"></a>

#### default\_context\_window

<a id="qca.forward.types.model.Model.available_context_windows"></a>

#### available\_context\_windows

<a id="qca.forward.types.model_config"></a>

# qca.forward.types.model\_config

<a id="qca.forward.types.model_config.ModelConfig"></a>

## ModelConfig

```python
class ModelConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/model_config.py)

<a id="qca.forward.types.model_config.ModelConfig.id"></a>

#### id

<a id="qca.forward.types.model_config.ModelConfig.effort"></a>

#### effort

<a id="qca.forward.types.model_config.ModelConfig.context_window"></a>

#### context\_window

<a id="qca.forward.types.model_config_param"></a>

# qca.forward.types.model\_config\_param

<a id="qca.forward.types.model_config_param.ModelConfigParam"></a>

## ModelConfigParam

```python
class ModelConfigParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/model_config_param.py)

<a id="qca.forward.types.model_config_param.ModelConfigParam.id"></a>

#### id

<a id="qca.forward.types.model_config_param.ModelConfigParam.effort"></a>

#### effort

<a id="qca.forward.types.model_config_param.ModelConfigParam.context_window"></a>

#### context\_window

<a id="qca.forward.types.model_list_response"></a>

# qca.forward.types.model\_list\_response

<a id="qca.forward.types.model_list_response.ModelListResponse"></a>

## ModelListResponse

```python
class ModelListResponse(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/model_list_response.py)

<a id="qca.forward.types.model_list_response.ModelListResponse.data"></a>

#### data

<a id="qca.forward.types.model_list_response.ModelListResponse.has_more"></a>

#### has\_more

<a id="qca.forward.types.multiagent_config"></a>

# qca.forward.types.multiagent\_config

<a id="qca.forward.types.multiagent_config.MultiagentConfig"></a>

## MultiagentConfig

```python
class MultiagentConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/multiagent_config.py)

<a id="qca.forward.types.multiagent_config.MultiagentConfig.type"></a>

#### type

<a id="qca.forward.types.multiagent_config.MultiagentConfig.agents"></a>

#### agents

<a id="qca.forward.types.multiagent_config_param"></a>

# qca.forward.types.multiagent\_config\_param

<a id="qca.forward.types.multiagent_config_param.MultiagentConfigParam"></a>

## MultiagentConfigParam

```python
class MultiagentConfigParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/multiagent_config_param.py)

<a id="qca.forward.types.multiagent_config_param.MultiagentConfigParam.type"></a>

#### type

<a id="qca.forward.types.multiagent_config_param.MultiagentConfigParam.agents"></a>

#### agents

<a id="qca.forward.types.multiagent_entry"></a>

# qca.forward.types.multiagent\_entry

<a id="qca.forward.types.multiagent_entry.MultiagentEntry"></a>

## MultiagentEntry

```python
class MultiagentEntry(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/multiagent_entry.py)

<a id="qca.forward.types.multiagent_entry.MultiagentEntry.type"></a>

#### type

<a id="qca.forward.types.multiagent_entry.MultiagentEntry.template_id"></a>

#### template\_id

<a id="qca.forward.types.multiagent_entry.MultiagentEntry.name"></a>

#### name

<a id="qca.forward.types.multiagent_entry_param"></a>

# qca.forward.types.multiagent\_entry\_param

<a id="qca.forward.types.multiagent_entry_param.MultiagentEntryParam"></a>

## MultiagentEntryParam

```python
class MultiagentEntryParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/multiagent_entry_param.py)

<a id="qca.forward.types.multiagent_entry_param.MultiagentEntryParam.type"></a>

#### type

<a id="qca.forward.types.multiagent_entry_param.MultiagentEntryParam.template_id"></a>

#### template\_id

<a id="qca.forward.types.multiagent_entry_param.MultiagentEntryParam.name"></a>

#### name

<a id="qca.forward.types.permission_policy"></a>

# qca.forward.types.permission\_policy

<a id="qca.forward.types.permission_policy.PermissionPolicy"></a>

## PermissionPolicy

```python
class PermissionPolicy(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/permission_policy.py)

<a id="qca.forward.types.permission_policy.PermissionPolicy.type"></a>

#### type

<a id="qca.forward.types.permission_policy_param"></a>

# qca.forward.types.permission\_policy\_param

<a id="qca.forward.types.permission_policy_param.PermissionPolicyParam"></a>

## PermissionPolicyParam

```python
class PermissionPolicyParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/permission_policy_param.py)

<a id="qca.forward.types.permission_policy_param.PermissionPolicyParam.type"></a>

#### type

<a id="qca.forward.types.resource_binding"></a>

# qca.forward.types.resource\_binding

<a id="qca.forward.types.resource_binding.ResourceBinding"></a>

## ResourceBinding

```python
class ResourceBinding(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/resource_binding.py)

<a id="qca.forward.types.resource_binding.ResourceBinding.enabled"></a>

#### enabled

<a id="qca.forward.types.resource_binding_param"></a>

# qca.forward.types.resource\_binding\_param

<a id="qca.forward.types.resource_binding_param.ResourceBindingParam"></a>

## ResourceBindingParam

```python
class ResourceBindingParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/resource_binding_param.py)

<a id="qca.forward.types.resource_binding_param.ResourceBindingParam.enabled"></a>

#### enabled

<a id="qca.forward.types.schedule"></a>

# qca.forward.types.schedule

<a id="qca.forward.types.schedule.Schedule"></a>

## Schedule

```python
class Schedule(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule.py)

<a id="qca.forward.types.schedule.Schedule.id"></a>

#### id

<a id="qca.forward.types.schedule.Schedule.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.schedule.Schedule.template_id"></a>

#### template\_id

<a id="qca.forward.types.schedule.Schedule.name"></a>

#### name

<a id="qca.forward.types.schedule.Schedule.description"></a>

#### description

<a id="qca.forward.types.schedule.Schedule.status"></a>

#### status

<a id="qca.forward.types.schedule.Schedule.initial_events"></a>

#### initial\_events

<a id="qca.forward.types.schedule.Schedule.execution"></a>

#### execution

<a id="qca.forward.types.schedule.Schedule.trigger_policy"></a>

#### trigger\_policy

<a id="qca.forward.types.schedule.Schedule.environment_id"></a>

#### environment\_id

<a id="qca.forward.types.schedule.Schedule.sinks"></a>

#### sinks

<a id="qca.forward.types.schedule.Schedule.metadata"></a>

#### metadata

<a id="qca.forward.types.schedule.Schedule.created_at"></a>

#### created\_at

<a id="qca.forward.types.schedule.Schedule.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.schedule.Schedule.archived_at"></a>

#### archived\_at

<a id="qca.forward.types.schedule.Schedule.paused_reason"></a>

#### paused\_reason

<a id="qca.forward.types.schedule_archive_many_params"></a>

# qca.forward.types.schedule\_archive\_many\_params

<a id="qca.forward.types.schedule_archive_many_params.ScheduleArchiveManyParams"></a>

## ScheduleArchiveManyParams

```python
class ScheduleArchiveManyParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_archive_many_params.py)

<a id="qca.forward.types.schedule_archive_many_params.ScheduleArchiveManyParams.schedule_ids"></a>

#### schedule\_ids

<a id="qca.forward.types.schedule_archive_many_params.ScheduleArchiveManyParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.schedule_archive_many_response"></a>

# qca.forward.types.schedule\_archive\_many\_response

<a id="qca.forward.types.schedule_archive_many_response.ScheduleArchiveManyResponse"></a>

## ScheduleArchiveManyResponse

```python
class ScheduleArchiveManyResponse(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_archive_many_response.py)

<a id="qca.forward.types.schedule_archive_many_response.ScheduleArchiveManyResponse.archived_count"></a>

#### archived\_count

<a id="qca.forward.types.schedule_archive_params"></a>

# qca.forward.types.schedule\_archive\_params

<a id="qca.forward.types.schedule_archive_params.ScheduleArchiveParams"></a>

## ScheduleArchiveParams

```python
class ScheduleArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_archive_params.py)

<a id="qca.forward.types.schedule_archive_params.ScheduleArchiveParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.schedule_create_params"></a>

# qca.forward.types.schedule\_create\_params

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams"></a>

## ScheduleCreateParams

```python
class ScheduleCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_create_params.py)

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams.template_id"></a>

#### template\_id

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams.name"></a>

#### name

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams.description"></a>

#### description

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams.initial_events"></a>

#### initial\_events

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams.execution"></a>

#### execution

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams.trigger_policy"></a>

#### trigger\_policy

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams.environment_id"></a>

#### environment\_id

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams.sinks"></a>

#### sinks

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.schedule_create_params.ScheduleCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.schedule_execution"></a>

# qca.forward.types.schedule\_execution

<a id="qca.forward.types.schedule_execution.ScheduleExecution"></a>

## ScheduleExecution

```python
class ScheduleExecution(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_execution.py)

<a id="qca.forward.types.schedule_execution.ScheduleExecution.session_mode"></a>

#### session\_mode

<a id="qca.forward.types.schedule_execution.ScheduleExecution.max_concurrent_runs"></a>

#### max\_concurrent\_runs

<a id="qca.forward.types.schedule_execution.ScheduleExecution.max_attempts"></a>

#### max\_attempts

<a id="qca.forward.types.schedule_execution.ScheduleExecution.timeout_ms"></a>

#### timeout\_ms

<a id="qca.forward.types.schedule_initial_events_item"></a>

# qca.forward.types.schedule\_initial\_events\_item

<a id="qca.forward.types.schedule_initial_events_item.ScheduleInitialEventsItem"></a>

## ScheduleInitialEventsItem

```python
class ScheduleInitialEventsItem(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_initial_events_item.py)

<a id="qca.forward.types.schedule_initial_events_item.ScheduleInitialEventsItem.type"></a>

#### type

<a id="qca.forward.types.schedule_initial_events_item.ScheduleInitialEventsItem.content"></a>

#### content

<a id="qca.forward.types.schedule_list_params"></a>

# qca.forward.types.schedule\_list\_params

<a id="qca.forward.types.schedule_list_params.ScheduleListParams"></a>

## ScheduleListParams

```python
class ScheduleListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_list_params.py)

<a id="qca.forward.types.schedule_list_params.ScheduleListParams.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.schedule_list_params.ScheduleListParams.template_id"></a>

#### template\_id

<a id="qca.forward.types.schedule_list_params.ScheduleListParams.status"></a>

#### status

<a id="qca.forward.types.schedule_list_params.ScheduleListParams.include_archived"></a>

#### include\_archived

<a id="qca.forward.types.schedule_list_params.ScheduleListParams.limit"></a>

#### limit

<a id="qca.forward.types.schedule_list_params.ScheduleListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.schedule_list_params.ScheduleListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.schedule_list_params.ScheduleListParams.sort_by"></a>

#### sort\_by

<a id="qca.forward.types.schedule_list_params.ScheduleListParams.order"></a>

#### order

<a id="qca.forward.types.schedule_pause_params"></a>

# qca.forward.types.schedule\_pause\_params

<a id="qca.forward.types.schedule_pause_params.SchedulePauseParams"></a>

## SchedulePauseParams

```python
class SchedulePauseParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_pause_params.py)

<a id="qca.forward.types.schedule_pause_params.SchedulePauseParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.schedule_paused_reason"></a>

# qca.forward.types.schedule\_paused\_reason

<a id="qca.forward.types.schedule_paused_reason.SchedulePausedReason"></a>

## SchedulePausedReason

```python
class SchedulePausedReason(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_paused_reason.py)

<a id="qca.forward.types.schedule_paused_reason.SchedulePausedReason.type"></a>

#### type

<a id="qca.forward.types.schedule_run"></a>

# qca.forward.types.schedule\_run

<a id="qca.forward.types.schedule_run.ScheduleRun"></a>

## ScheduleRun

```python
class ScheduleRun(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_run.py)

<a id="qca.forward.types.schedule_run.ScheduleRun.id"></a>

#### id

<a id="qca.forward.types.schedule_run.ScheduleRun.schedule_id"></a>

#### schedule\_id

<a id="qca.forward.types.schedule_run.ScheduleRun.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.schedule_run.ScheduleRun.template_id"></a>

#### template\_id

<a id="qca.forward.types.schedule_run.ScheduleRun.session_id"></a>

#### session\_id

<a id="qca.forward.types.schedule_run.ScheduleRun.status"></a>

#### status

<a id="qca.forward.types.schedule_run.ScheduleRun.trigger_context"></a>

#### trigger\_context

<a id="qca.forward.types.schedule_run.ScheduleRun.result_payload"></a>

#### result\_payload

<a id="qca.forward.types.schedule_run.ScheduleRun.push_sink"></a>

#### push\_sink

<a id="qca.forward.types.schedule_run.ScheduleRun.push_status"></a>

#### push\_status

<a id="qca.forward.types.schedule_run.ScheduleRun.push_finished_at"></a>

#### push\_finished\_at

<a id="qca.forward.types.schedule_run.ScheduleRun.attempt"></a>

#### attempt

<a id="qca.forward.types.schedule_run.ScheduleRun.triggered_at"></a>

#### triggered\_at

<a id="qca.forward.types.schedule_run.ScheduleRun.started_at"></a>

#### started\_at

<a id="qca.forward.types.schedule_run.ScheduleRun.completed_at"></a>

#### completed\_at

<a id="qca.forward.types.schedule_run.ScheduleRun.duration_ms"></a>

#### duration\_ms

<a id="qca.forward.types.schedule_run.ScheduleRun.created_at"></a>

#### created\_at

<a id="qca.forward.types.schedule_run.ScheduleRun.error"></a>

#### error

<a id="qca.forward.types.schedule_run.ScheduleRun.error_message"></a>

#### error\_message

<a id="qca.forward.types.schedule_run_list_params"></a>

# qca.forward.types.schedule\_run\_list\_params

<a id="qca.forward.types.schedule_run_list_params.ScheduleRunListParams"></a>

## ScheduleRunListParams

```python
class ScheduleRunListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_run_list_params.py)

<a id="qca.forward.types.schedule_run_list_params.ScheduleRunListParams.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.schedule_run_list_params.ScheduleRunListParams.schedule_id"></a>

#### schedule\_id

<a id="qca.forward.types.schedule_run_list_params.ScheduleRunListParams.status"></a>

#### status

<a id="qca.forward.types.schedule_run_list_params.ScheduleRunListParams.trigger_type"></a>

#### trigger\_type

<a id="qca.forward.types.schedule_run_list_params.ScheduleRunListParams.has_error"></a>

#### has\_error

<a id="qca.forward.types.schedule_run_list_params.ScheduleRunListParams.limit"></a>

#### limit

<a id="qca.forward.types.schedule_run_list_params.ScheduleRunListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.schedule_run_list_params.ScheduleRunListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.schedule_run_list_params.ScheduleRunListParams.sort_by"></a>

#### sort\_by

<a id="qca.forward.types.schedule_run_list_params.ScheduleRunListParams.order"></a>

#### order

<a id="qca.forward.types.schedule_run_params"></a>

# qca.forward.types.schedule\_run\_params

<a id="qca.forward.types.schedule_run_params.ScheduleRunParams"></a>

## ScheduleRunParams

```python
class ScheduleRunParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_run_params.py)

<a id="qca.forward.types.schedule_run_params.ScheduleRunParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.schedule_run_retrieve_params"></a>

# qca.forward.types.schedule\_run\_retrieve\_params

<a id="qca.forward.types.schedule_run_retrieve_params.ScheduleRunRetrieveParams"></a>

## ScheduleRunRetrieveParams

```python
class ScheduleRunRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_run_retrieve_params.py)

<a id="qca.forward.types.schedule_run_retrieve_params.ScheduleRunRetrieveParams.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.schedule_run_trigger_context"></a>

# qca.forward.types.schedule\_run\_trigger\_context

<a id="qca.forward.types.schedule_run_trigger_context.ScheduleRunTriggerContext"></a>

## ScheduleRunTriggerContext

```python
class ScheduleRunTriggerContext(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_run_trigger_context.py)

<a id="qca.forward.types.schedule_run_trigger_context.ScheduleRunTriggerContext.type"></a>

#### type

<a id="qca.forward.types.schedule_run_trigger_context.ScheduleRunTriggerContext.scheduled_at"></a>

#### scheduled\_at

<a id="qca.forward.types.schedule_sinks_item"></a>

# qca.forward.types.schedule\_sinks\_item

<a id="qca.forward.types.schedule_sinks_item.ScheduleSinksItem"></a>

## ScheduleSinksItem

```python
class ScheduleSinksItem(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_sinks_item.py)

<a id="qca.forward.types.schedule_sinks_item.ScheduleSinksItem.type"></a>

#### type

<a id="qca.forward.types.schedule_sinks_item.ScheduleSinksItem.channel_id"></a>

#### channel\_id

<a id="qca.forward.types.schedule_sinks_item.ScheduleSinksItem.target"></a>

#### target

<a id="qca.forward.types.schedule_sinks_item_target"></a>

# qca.forward.types.schedule\_sinks\_item\_target

<a id="qca.forward.types.schedule_sinks_item_target.ScheduleSinksItemTarget"></a>

## ScheduleSinksItemTarget

```python
class ScheduleSinksItemTarget(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_sinks_item_target.py)

<a id="qca.forward.types.schedule_sinks_item_target.ScheduleSinksItemTarget.type"></a>

#### type

<a id="qca.forward.types.schedule_sinks_item_target.ScheduleSinksItemTarget.external_id"></a>

#### external\_id

<a id="qca.forward.types.schedule_trigger_policy"></a>

# qca.forward.types.schedule\_trigger\_policy

<a id="qca.forward.types.schedule_trigger_policy.ScheduleTriggerPolicy"></a>

## ScheduleTriggerPolicy

```python
class ScheduleTriggerPolicy(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_trigger_policy.py)

<a id="qca.forward.types.schedule_trigger_policy.ScheduleTriggerPolicy.type"></a>

#### type

<a id="qca.forward.types.schedule_trigger_policy.ScheduleTriggerPolicy.expression"></a>

#### expression

<a id="qca.forward.types.schedule_trigger_policy.ScheduleTriggerPolicy.timezone"></a>

#### timezone

<a id="qca.forward.types.schedule_trigger_policy.ScheduleTriggerPolicy.upcoming_runs_at"></a>

#### upcoming\_runs\_at

<a id="qca.forward.types.schedule_unpause_params"></a>

# qca.forward.types.schedule\_unpause\_params

<a id="qca.forward.types.schedule_unpause_params.ScheduleUnpauseParams"></a>

## ScheduleUnpauseParams

```python
class ScheduleUnpauseParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_unpause_params.py)

<a id="qca.forward.types.schedule_unpause_params.ScheduleUnpauseParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.schedule_update_params"></a>

# qca.forward.types.schedule\_update\_params

<a id="qca.forward.types.schedule_update_params.ScheduleUpdateParams"></a>

## ScheduleUpdateParams

```python
class ScheduleUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/schedule_update_params.py)

<a id="qca.forward.types.schedule_update_params.ScheduleUpdateParams.name"></a>

#### name

<a id="qca.forward.types.schedule_update_params.ScheduleUpdateParams.description"></a>

#### description

<a id="qca.forward.types.schedule_update_params.ScheduleUpdateParams.template_id"></a>

#### template\_id

<a id="qca.forward.types.schedule_update_params.ScheduleUpdateParams.initial_events"></a>

#### initial\_events

<a id="qca.forward.types.schedule_update_params.ScheduleUpdateParams.execution"></a>

#### execution

<a id="qca.forward.types.schedule_update_params.ScheduleUpdateParams.trigger_policy"></a>

#### trigger\_policy

<a id="qca.forward.types.schedule_update_params.ScheduleUpdateParams.environment_id"></a>

#### environment\_id

<a id="qca.forward.types.schedule_update_params.ScheduleUpdateParams.sinks"></a>

#### sinks

<a id="qca.forward.types.schedule_update_params.ScheduleUpdateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.schedule_update_params.ScheduleUpdateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.session"></a>

# qca.forward.types.session

<a id="qca.forward.types.session.Session"></a>

## Session

```python
class Session(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session.py)

<a id="qca.forward.types.session.Session.id"></a>

#### id

<a id="qca.forward.types.session.Session.type"></a>

#### type

<a id="qca.forward.types.session.Session.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.session.Session.template"></a>

#### template

<a id="qca.forward.types.session.Session.source_type"></a>

#### source\_type

<a id="qca.forward.types.session.Session.status"></a>

#### status

<a id="qca.forward.types.session.Session.title"></a>

#### title

<a id="qca.forward.types.session.Session.metadata"></a>

#### metadata

<a id="qca.forward.types.session.Session.config"></a>

#### config

<a id="qca.forward.types.session.Session.resources"></a>

#### resources

<a id="qca.forward.types.session.Session.stats"></a>

#### stats

<a id="qca.forward.types.session.Session.usage"></a>

#### usage

<a id="qca.forward.types.session.Session.archived_at"></a>

#### archived\_at

<a id="qca.forward.types.session.Session.created_at"></a>

#### created\_at

<a id="qca.forward.types.session.Session.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.session_archive_params"></a>

# qca.forward.types.session\_archive\_params

<a id="qca.forward.types.session_archive_params.SessionArchiveParams"></a>

## SessionArchiveParams

```python
class SessionArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_archive_params.py)

<a id="qca.forward.types.session_archive_params.SessionArchiveParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.session_cancel_params"></a>

# qca.forward.types.session\_cancel\_params

<a id="qca.forward.types.session_cancel_params.SessionCancelParams"></a>

## SessionCancelParams

```python
class SessionCancelParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_cancel_params.py)

<a id="qca.forward.types.session_cancel_params.SessionCancelParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.session_config"></a>

# qca.forward.types.session\_config

<a id="qca.forward.types.session_config.SessionConfig"></a>

## SessionConfig

```python
class SessionConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_config.py)

<a id="qca.forward.types.session_config.SessionConfig.environment_variables"></a>

#### environment\_variables

<a id="qca.forward.types.session_create_params"></a>

# qca.forward.types.session\_create\_params

<a id="qca.forward.types.session_create_params.SessionCreateParams"></a>

## SessionCreateParams

```python
class SessionCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_create_params.py)

<a id="qca.forward.types.session_create_params.SessionCreateParams.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.session_create_params.SessionCreateParams.template_id"></a>

#### template\_id

<a id="qca.forward.types.session_create_params.SessionCreateParams.title"></a>

#### title

<a id="qca.forward.types.session_create_params.SessionCreateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.session_create_params.SessionCreateParams.config"></a>

#### config

<a id="qca.forward.types.session_create_params.SessionCreateParams.resources"></a>

#### resources

<a id="qca.forward.types.session_create_params.SessionCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.session_create_params_config_param"></a>

# qca.forward.types.session\_create\_params\_config\_param

<a id="qca.forward.types.session_create_params_config_param.SessionCreateParamsConfigParam"></a>

## SessionCreateParamsConfigParam

```python
class SessionCreateParamsConfigParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_create_params_config_param.py)

<a id="qca.forward.types.session_create_params_config_param.SessionCreateParamsConfigParam.environment_variables"></a>

#### environment\_variables

<a id="qca.forward.types.session_event"></a>

# qca.forward.types.session\_event

<a id="qca.forward.types.session_event.SessionEvent"></a>

## SessionEvent

```python
class SessionEvent(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_event.py)

<a id="qca.forward.types.session_event.SessionEvent.id"></a>

#### id

<a id="qca.forward.types.session_event.SessionEvent.type"></a>

#### type

<a id="qca.forward.types.session_event.SessionEvent.session_id"></a>

#### session\_id

<a id="qca.forward.types.session_event.SessionEvent.content"></a>

#### content

<a id="qca.forward.types.session_event.SessionEvent.processed_at"></a>

#### processed\_at

<a id="qca.forward.types.session_event.SessionEvent.session_thread_id"></a>

#### session\_thread\_id

<a id="qca.forward.types.session_event.SessionEvent.thinking"></a>

#### thinking

<a id="qca.forward.types.session_event.SessionEvent.text"></a>

#### text

<a id="qca.forward.types.session_event.SessionEvent.tool_use_id"></a>

#### tool\_use\_id

<a id="qca.forward.types.session_event.SessionEvent.custom_tool_use_id"></a>

#### custom\_tool\_use\_id

<a id="qca.forward.types.session_event.SessionEvent.mcp_tool_use_id"></a>

#### mcp\_tool\_use\_id

<a id="qca.forward.types.session_event.SessionEvent.name"></a>

#### name

<a id="qca.forward.types.session_event.SessionEvent.mcp_server_name"></a>

#### mcp\_server\_name

<a id="qca.forward.types.session_event.SessionEvent.input"></a>

#### input

<a id="qca.forward.types.session_event.SessionEvent.is_error"></a>

#### is\_error

<a id="qca.forward.types.session_event.SessionEvent.result"></a>

#### result

<a id="qca.forward.types.session_event.SessionEvent.deny_message"></a>

#### deny\_message

<a id="qca.forward.types.session_event.SessionEvent.description"></a>

#### description

<a id="qca.forward.types.session_event.SessionEvent.rubric"></a>

#### rubric

<a id="qca.forward.types.session_event.SessionEvent.outcome_id"></a>

#### outcome\_id

<a id="qca.forward.types.session_event.SessionEvent.max_iterations"></a>

#### max\_iterations

<a id="qca.forward.types.session_event.SessionEvent.message_id"></a>

#### message\_id

<a id="qca.forward.types.session_event.SessionEvent.message"></a>

#### message

<a id="qca.forward.types.session_event.SessionEvent.index"></a>

#### index

<a id="qca.forward.types.session_event.SessionEvent.content_block"></a>

#### content\_block

<a id="qca.forward.types.session_event.SessionEvent.delta"></a>

#### delta

<a id="qca.forward.types.session_event.SessionEvent.event"></a>

#### event

<a id="qca.forward.types.session_event.SessionEvent.event_id"></a>

#### event\_id

<a id="qca.forward.types.session_event.SessionEvent.usage"></a>

#### usage

<a id="qca.forward.types.session_event.SessionEvent.stop_reason"></a>

#### stop\_reason

<a id="qca.forward.types.session_event.SessionEvent.error"></a>

#### error

<a id="qca.forward.types.session_event.SessionEvent.evaluated_permission"></a>

#### evaluated\_permission

<a id="qca.forward.types.session_event.SessionEvent.file_id"></a>

#### file\_id

<a id="qca.forward.types.session_event.SessionEvent.original_filename"></a>

#### original\_filename

<a id="qca.forward.types.session_event.SessionEvent.size"></a>

#### size

<a id="qca.forward.types.session_event.SessionEvent.content_type"></a>

#### content\_type

<a id="qca.forward.types.session_event.SessionEvent.agent"></a>

#### agent

<a id="qca.forward.types.session_event.SessionEvent.metadata"></a>

#### metadata

<a id="qca.forward.types.session_event.SessionEvent.title"></a>

#### title

<a id="qca.forward.types.session_event.SessionEvent.model_request_start_id"></a>

#### model\_request\_start\_id

<a id="qca.forward.types.session_event.SessionEvent.model_usage"></a>

#### model\_usage

<a id="qca.forward.types.session_event_list_params"></a>

# qca.forward.types.session\_event\_list\_params

<a id="qca.forward.types.session_event_list_params.SessionEventListParams"></a>

## SessionEventListParams

```python
class SessionEventListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_event_list_params.py)

<a id="qca.forward.types.session_event_list_params.SessionEventListParams.limit"></a>

#### limit

<a id="qca.forward.types.session_event_list_params.SessionEventListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.session_event_list_params.SessionEventListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.session_event_list_params.SessionEventListParams.order"></a>

#### order

<a id="qca.forward.types.session_event_list_params.SessionEventListParams.type"></a>

#### type

<a id="qca.forward.types.session_event_list_params.SessionEventListParams.types"></a>

#### types

<a id="qca.forward.types.session_event_list_params.SessionEventListParams.include_tool_calls"></a>

#### include\_tool\_calls

<a id="qca.forward.types.session_event_list_params.SessionEventListParams.include_thinking"></a>

#### include\_thinking

<a id="qca.forward.types.session_event_param"></a>

# qca.forward.types.session\_event\_param

<a id="qca.forward.types.session_event_param.SessionEventParam"></a>

## SessionEventParam

```python
class SessionEventParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_event_param.py)

<a id="qca.forward.types.session_event_param.SessionEventParam.type"></a>

#### type

<a id="qca.forward.types.session_event_param.SessionEventParam.content"></a>

#### content

<a id="qca.forward.types.session_event_param.SessionEventParam.tool_use_id"></a>

#### tool\_use\_id

<a id="qca.forward.types.session_event_param.SessionEventParam.custom_tool_use_id"></a>

#### custom\_tool\_use\_id

<a id="qca.forward.types.session_event_param.SessionEventParam.result"></a>

#### result

<a id="qca.forward.types.session_event_param.SessionEventParam.deny_message"></a>

#### deny\_message

<a id="qca.forward.types.session_event_param.SessionEventParam.is_error"></a>

#### is\_error

<a id="qca.forward.types.session_event_param.SessionEventParam.description"></a>

#### description

<a id="qca.forward.types.session_event_param.SessionEventParam.rubric"></a>

#### rubric

<a id="qca.forward.types.session_event_param.SessionEventParam.outcome_id"></a>

#### outcome\_id

<a id="qca.forward.types.session_event_param.SessionEventParam.max_iterations"></a>

#### max\_iterations

<a id="qca.forward.types.session_event_send_params"></a>

# qca.forward.types.session\_event\_send\_params

<a id="qca.forward.types.session_event_send_params.SessionEventSendParams"></a>

## SessionEventSendParams

```python
class SessionEventSendParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_event_send_params.py)

<a id="qca.forward.types.session_event_send_params.SessionEventSendParams.events"></a>

#### events

<a id="qca.forward.types.session_event_send_params.SessionEventSendParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.session_event_send_response"></a>

# qca.forward.types.session\_event\_send\_response

<a id="qca.forward.types.session_event_send_response.SessionEventSendResponse"></a>

## SessionEventSendResponse

```python
class SessionEventSendResponse(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_event_send_response.py)

<a id="qca.forward.types.session_event_send_response.SessionEventSendResponse.data"></a>

#### data

<a id="qca.forward.types.session_event_stream_params"></a>

# qca.forward.types.session\_event\_stream\_params

<a id="qca.forward.types.session_event_stream_params.SessionEventStreamParams"></a>

## SessionEventStreamParams

```python
class SessionEventStreamParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_event_stream_params.py)

<a id="qca.forward.types.session_event_stream_params.SessionEventStreamParams.event_deltas"></a>

#### event\_deltas

<a id="qca.forward.types.session_event_stream_params.SessionEventStreamParams.include_tool_calls"></a>

#### include\_tool\_calls

<a id="qca.forward.types.session_event_stream_params.SessionEventStreamParams.include_thinking"></a>

#### include\_thinking

<a id="qca.forward.types.session_event_stream_params.SessionEventStreamParams.last_event_id"></a>

#### last\_event\_id

<a id="qca.forward.types.session_list_params"></a>

# qca.forward.types.session\_list\_params

<a id="qca.forward.types.session_list_params.SessionListParams"></a>

## SessionListParams

```python
class SessionListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_list_params.py)

<a id="qca.forward.types.session_list_params.SessionListParams.identity_i_ds"></a>

#### identity\_i\_ds

<a id="qca.forward.types.session_list_params.SessionListParams.template_id"></a>

#### template\_id

<a id="qca.forward.types.session_list_params.SessionListParams.source_type"></a>

#### source\_type

<a id="qca.forward.types.session_list_params.SessionListParams.created_at_gt"></a>

#### created\_at\_gt

<a id="qca.forward.types.session_list_params.SessionListParams.created_at_gte"></a>

#### created\_at\_gte

<a id="qca.forward.types.session_list_params.SessionListParams.created_at_lt"></a>

#### created\_at\_lt

<a id="qca.forward.types.session_list_params.SessionListParams.created_at_lte"></a>

#### created\_at\_lte

<a id="qca.forward.types.session_list_params.SessionListParams.updated_at_gt"></a>

#### updated\_at\_gt

<a id="qca.forward.types.session_list_params.SessionListParams.updated_at_gte"></a>

#### updated\_at\_gte

<a id="qca.forward.types.session_list_params.SessionListParams.updated_at_lt"></a>

#### updated\_at\_lt

<a id="qca.forward.types.session_list_params.SessionListParams.updated_at_lte"></a>

#### updated\_at\_lte

<a id="qca.forward.types.session_list_params.SessionListParams.limit"></a>

#### limit

<a id="qca.forward.types.session_list_params.SessionListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.session_list_params.SessionListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.session_list_params.SessionListParams.order"></a>

#### order

<a id="qca.forward.types.session_list_params.SessionListParams.include_archived"></a>

#### include\_archived

<a id="qca.forward.types.session_resource"></a>

# qca.forward.types.session\_resource

<a id="qca.forward.types.session_resource.SessionResource"></a>

## SessionResource

```python
class SessionResource(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_resource.py)

<a id="qca.forward.types.session_resource.SessionResource.id"></a>

#### id

<a id="qca.forward.types.session_resource.SessionResource.type"></a>

#### type

<a id="qca.forward.types.session_resource.SessionResource.file_id"></a>

#### file\_id

<a id="qca.forward.types.session_resource.SessionResource.mount_path"></a>

#### mount\_path

<a id="qca.forward.types.session_resource.SessionResource.created_at"></a>

#### created\_at

<a id="qca.forward.types.session_resource.SessionResource.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.session_resource_add_params"></a>

# qca.forward.types.session\_resource\_add\_params

<a id="qca.forward.types.session_resource_add_params.SessionResourceAddParams"></a>

## SessionResourceAddParams

```python
class SessionResourceAddParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_resource_add_params.py)

<a id="qca.forward.types.session_resource_add_params.SessionResourceAddParams.type"></a>

#### type

<a id="qca.forward.types.session_resource_add_params.SessionResourceAddParams.file_id"></a>

#### file\_id

<a id="qca.forward.types.session_resource_add_params.SessionResourceAddParams.mount_path"></a>

#### mount\_path

<a id="qca.forward.types.session_resource_spec_param"></a>

# qca.forward.types.session\_resource\_spec\_param

<a id="qca.forward.types.session_resource_spec_param.SessionResourceSpecParam"></a>

## SessionResourceSpecParam

```python
class SessionResourceSpecParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_resource_spec_param.py)

<a id="qca.forward.types.session_resource_spec_param.SessionResourceSpecParam.type"></a>

#### type

<a id="qca.forward.types.session_resource_spec_param.SessionResourceSpecParam.file_id"></a>

#### file\_id

<a id="qca.forward.types.session_resource_spec_param.SessionResourceSpecParam.mount_path"></a>

#### mount\_path

<a id="qca.forward.types.session_stats"></a>

# qca.forward.types.session\_stats

<a id="qca.forward.types.session_stats.SessionStats"></a>

## SessionStats

```python
class SessionStats(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_stats.py)

<a id="qca.forward.types.session_stats.SessionStats.active_seconds"></a>

#### active\_seconds

<a id="qca.forward.types.session_stats.SessionStats.duration_seconds"></a>

#### duration\_seconds

<a id="qca.forward.types.session_template"></a>

# qca.forward.types.session\_template

<a id="qca.forward.types.session_template.SessionTemplate"></a>

## SessionTemplate

```python
class SessionTemplate(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_template.py)

<a id="qca.forward.types.session_template.SessionTemplate.id"></a>

#### id

<a id="qca.forward.types.session_template.SessionTemplate.type"></a>

#### type

<a id="qca.forward.types.session_template.SessionTemplate.name"></a>

#### name

<a id="qca.forward.types.session_template.SessionTemplate.model"></a>

#### model

<a id="qca.forward.types.session_template.SessionTemplate.version"></a>

#### version

<a id="qca.forward.types.session_thread"></a>

# qca.forward.types.session\_thread

<a id="qca.forward.types.session_thread.SessionThread"></a>

## SessionThread

```python
class SessionThread(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_thread.py)

<a id="qca.forward.types.session_thread.SessionThread.id"></a>

#### id

<a id="qca.forward.types.session_thread.SessionThread.type"></a>

#### type

<a id="qca.forward.types.session_thread.SessionThread.session_id"></a>

#### session\_id

<a id="qca.forward.types.session_thread.SessionThread.template_id"></a>

#### template\_id

<a id="qca.forward.types.session_thread.SessionThread.role"></a>

#### role

<a id="qca.forward.types.session_thread.SessionThread.status"></a>

#### status

<a id="qca.forward.types.session_thread.SessionThread.stop_reason"></a>

#### stop\_reason

<a id="qca.forward.types.session_thread.SessionThread.created_at"></a>

#### created\_at

<a id="qca.forward.types.session_thread.SessionThread.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.session_thread.SessionThread.parent_thread_id"></a>

#### parent\_thread\_id

<a id="qca.forward.types.session_thread.SessionThread.name"></a>

#### name

<a id="qca.forward.types.session_thread.SessionThread.created_by_tool_use_id"></a>

#### created\_by\_tool\_use\_id

<a id="qca.forward.types.session_thread.SessionThread.archived_at"></a>

#### archived\_at

<a id="qca.forward.types.session_thread_archive_params"></a>

# qca.forward.types.session\_thread\_archive\_params

<a id="qca.forward.types.session_thread_archive_params.SessionThreadArchiveParams"></a>

## SessionThreadArchiveParams

```python
class SessionThreadArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_thread_archive_params.py)

<a id="qca.forward.types.session_thread_archive_params.SessionThreadArchiveParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.session_thread_event_list_params"></a>

# qca.forward.types.session\_thread\_event\_list\_params

<a id="qca.forward.types.session_thread_event_list_params.SessionThreadEventListParams"></a>

## SessionThreadEventListParams

```python
class SessionThreadEventListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_thread_event_list_params.py)

<a id="qca.forward.types.session_thread_event_list_params.SessionThreadEventListParams.limit"></a>

#### limit

<a id="qca.forward.types.session_thread_event_list_params.SessionThreadEventListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.session_thread_event_list_params.SessionThreadEventListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.session_thread_event_stream_params"></a>

# qca.forward.types.session\_thread\_event\_stream\_params

<a id="qca.forward.types.session_thread_event_stream_params.SessionThreadEventStreamParams"></a>

## SessionThreadEventStreamParams

```python
class SessionThreadEventStreamParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_thread_event_stream_params.py)

<a id="qca.forward.types.session_thread_event_stream_params.SessionThreadEventStreamParams.last_event_id"></a>

#### last\_event\_id

<a id="qca.forward.types.session_thread_list_params"></a>

# qca.forward.types.session\_thread\_list\_params

<a id="qca.forward.types.session_thread_list_params.SessionThreadListParams"></a>

## SessionThreadListParams

```python
class SessionThreadListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_thread_list_params.py)

<a id="qca.forward.types.session_thread_list_params.SessionThreadListParams.limit"></a>

#### limit

<a id="qca.forward.types.session_thread_list_params.SessionThreadListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.session_thread_list_params.SessionThreadListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.session_thread_stop_reason"></a>

# qca.forward.types.session\_thread\_stop\_reason

<a id="qca.forward.types.session_thread_stop_reason.SessionThreadStopReason"></a>

## SessionThreadStopReason

```python
class SessionThreadStopReason(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_thread_stop_reason.py)

<a id="qca.forward.types.session_thread_stop_reason.SessionThreadStopReason.type"></a>

#### type

<a id="qca.forward.types.session_update_params"></a>

# qca.forward.types.session\_update\_params

<a id="qca.forward.types.session_update_params.SessionUpdateParams"></a>

## SessionUpdateParams

```python
class SessionUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_update_params.py)

<a id="qca.forward.types.session_update_params.SessionUpdateParams.title"></a>

#### title

<a id="qca.forward.types.session_update_params.SessionUpdateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.session_update_params.SessionUpdateParams.config"></a>

#### config

<a id="qca.forward.types.session_update_params.SessionUpdateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.session_update_params_config_param"></a>

# qca.forward.types.session\_update\_params\_config\_param

<a id="qca.forward.types.session_update_params_config_param.SessionUpdateParamsConfigParam"></a>

## SessionUpdateParamsConfigParam

```python
class SessionUpdateParamsConfigParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_update_params_config_param.py)

<a id="qca.forward.types.session_update_params_config_param.SessionUpdateParamsConfigParam.environment_variables"></a>

#### environment\_variables

<a id="qca.forward.types.session_usage"></a>

# qca.forward.types.session\_usage

<a id="qca.forward.types.session_usage.SessionUsage"></a>

## SessionUsage

```python
class SessionUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/session_usage.py)

<a id="qca.forward.types.session_usage.SessionUsage.total_credits"></a>

#### total\_credits

<a id="qca.forward.types.skill"></a>

# qca.forward.types.skill

<a id="qca.forward.types.skill.Skill"></a>

## Skill

```python
class Skill(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill.py)

<a id="qca.forward.types.skill.Skill.id"></a>

#### id

<a id="qca.forward.types.skill.Skill.type"></a>

#### type

<a id="qca.forward.types.skill.Skill.display_title"></a>

#### display\_title

<a id="qca.forward.types.skill.Skill.description"></a>

#### description

<a id="qca.forward.types.skill.Skill.source"></a>

#### source

<a id="qca.forward.types.skill.Skill.latest_version"></a>

#### latest\_version

<a id="qca.forward.types.skill.Skill.metadata"></a>

#### metadata

<a id="qca.forward.types.skill.Skill.created_at"></a>

#### created\_at

<a id="qca.forward.types.skill.Skill.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.skill.Skill.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.skill.Skill.icon_url"></a>

#### icon\_url

<a id="qca.forward.types.skill.Skill.binding_info"></a>

#### binding\_info

<a id="qca.forward.types.skill_binding"></a>

# qca.forward.types.skill\_binding

<a id="qca.forward.types.skill_binding.SkillBinding"></a>

## SkillBinding

```python
class SkillBinding(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill_binding.py)

<a id="qca.forward.types.skill_binding.SkillBinding.type"></a>

#### type

<a id="qca.forward.types.skill_binding.SkillBinding.skill_id"></a>

#### skill\_id

<a id="qca.forward.types.skill_binding.SkillBinding.version"></a>

#### version

<a id="qca.forward.types.skill_binding.SkillBinding.enabled"></a>

#### enabled

<a id="qca.forward.types.skill_binding_param"></a>

# qca.forward.types.skill\_binding\_param

<a id="qca.forward.types.skill_binding_param.SkillBindingParam"></a>

## SkillBindingParam

```python
class SkillBindingParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill_binding_param.py)

<a id="qca.forward.types.skill_binding_param.SkillBindingParam.type"></a>

#### type

<a id="qca.forward.types.skill_binding_param.SkillBindingParam.skill_id"></a>

#### skill\_id

<a id="qca.forward.types.skill_binding_param.SkillBindingParam.version"></a>

#### version

<a id="qca.forward.types.skill_binding_param.SkillBindingParam.enabled"></a>

#### enabled

<a id="qca.forward.types.skill_create_params"></a>

# qca.forward.types.skill\_create\_params

<a id="qca.forward.types.skill_create_params.SkillCreateParams"></a>

## SkillCreateParams

```python
class SkillCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill_create_params.py)

<a id="qca.forward.types.skill_create_params.SkillCreateParams.files"></a>

#### files

<a id="qca.forward.types.skill_create_params.SkillCreateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.skill_create_params.SkillCreateParams.icon_id"></a>

#### icon\_id

<a id="qca.forward.types.skill_create_params.SkillCreateParams.file"></a>

#### file

<a id="qca.forward.types.skill_create_params.SkillCreateParams.name"></a>

#### name

<a id="qca.forward.types.skill_create_params.SkillCreateParams.description"></a>

#### description

<a id="qca.forward.types.skill_create_params.SkillCreateParams.type"></a>

#### type

<a id="qca.forward.types.skill_create_params.SkillCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.skill_list_params"></a>

# qca.forward.types.skill\_list\_params

<a id="qca.forward.types.skill_list_params.SkillListParams"></a>

## SkillListParams

```python
class SkillListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill_list_params.py)

<a id="qca.forward.types.skill_list_params.SkillListParams.limit"></a>

#### limit

<a id="qca.forward.types.skill_list_params.SkillListParams.page"></a>

#### page

<a id="qca.forward.types.skill_list_params.SkillListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.skill_list_params.SkillListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.skill_list_params.SkillListParams.display_title"></a>

#### display\_title

<a id="qca.forward.types.skill_list_params.SkillListParams.source"></a>

#### source

<a id="qca.forward.types.skill_list_params.SkillListParams.name"></a>

#### name

<a id="qca.forward.types.skill_override"></a>

# qca.forward.types.skill\_override

<a id="qca.forward.types.skill_override.SkillOverride"></a>

## SkillOverride

```python
class SkillOverride(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill_override.py)

<a id="qca.forward.types.skill_override.SkillOverride.enabled"></a>

#### enabled

<a id="qca.forward.types.skill_override.SkillOverride.type"></a>

#### type

<a id="qca.forward.types.skill_override.SkillOverride.version"></a>

#### version

<a id="qca.forward.types.skill_override_param"></a>

# qca.forward.types.skill\_override\_param

<a id="qca.forward.types.skill_override_param.SkillOverrideParam"></a>

## SkillOverrideParam

```python
class SkillOverrideParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill_override_param.py)

<a id="qca.forward.types.skill_override_param.SkillOverrideParam.enabled"></a>

#### enabled

<a id="qca.forward.types.skill_override_param.SkillOverrideParam.type"></a>

#### type

<a id="qca.forward.types.skill_override_param.SkillOverrideParam.version"></a>

#### version

<a id="qca.forward.types.skill_retrieve_params"></a>

# qca.forward.types.skill\_retrieve\_params

<a id="qca.forward.types.skill_retrieve_params.SkillRetrieveParams"></a>

## SkillRetrieveParams

```python
class SkillRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill_retrieve_params.py)

<a id="qca.forward.types.skill_retrieve_params.SkillRetrieveParams.include_content"></a>

#### include\_content

<a id="qca.forward.types.skill_update_params"></a>

# qca.forward.types.skill\_update\_params

<a id="qca.forward.types.skill_update_params.SkillUpdateParams"></a>

## SkillUpdateParams

```python
class SkillUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill_update_params.py)

<a id="qca.forward.types.skill_update_params.SkillUpdateParams.description"></a>

#### description

<a id="qca.forward.types.skill_update_params.SkillUpdateParams.content"></a>

#### content

<a id="qca.forward.types.skill_update_params.SkillUpdateParams.content_encoding"></a>

#### content\_encoding

<a id="qca.forward.types.skill_update_params.SkillUpdateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.skill_update_params.SkillUpdateParams.icon_id"></a>

#### icon\_id

<a id="qca.forward.types.skill_update_params.SkillUpdateParams.name"></a>

#### name

<a id="qca.forward.types.skill_version"></a>

# qca.forward.types.skill\_version

<a id="qca.forward.types.skill_version.SkillVersion"></a>

## SkillVersion

```python
class SkillVersion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill_version.py)

<a id="qca.forward.types.skill_version.SkillVersion.id"></a>

#### id

<a id="qca.forward.types.skill_version.SkillVersion.skill_id"></a>

#### skill\_id

<a id="qca.forward.types.skill_version.SkillVersion.version"></a>

#### version

<a id="qca.forward.types.skill_version.SkillVersion.name"></a>

#### name

<a id="qca.forward.types.skill_version.SkillVersion.description"></a>

#### description

<a id="qca.forward.types.skill_version.SkillVersion.directory"></a>

#### directory

<a id="qca.forward.types.skill_version.SkillVersion.content_size"></a>

#### content\_size

<a id="qca.forward.types.skill_version.SkillVersion.content_sha256"></a>

#### content\_sha256

<a id="qca.forward.types.skill_version.SkillVersion.status"></a>

#### status

<a id="qca.forward.types.skill_version.SkillVersion.created_at"></a>

#### created\_at

<a id="qca.forward.types.skill_version.SkillVersion.metadata"></a>

#### metadata

<a id="qca.forward.types.skill_version_create_params"></a>

# qca.forward.types.skill\_version\_create\_params

<a id="qca.forward.types.skill_version_create_params.SkillVersionCreateParams"></a>

## SkillVersionCreateParams

```python
class SkillVersionCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill_version_create_params.py)

<a id="qca.forward.types.skill_version_create_params.SkillVersionCreateParams.files"></a>

#### files

<a id="qca.forward.types.skill_version_list_params"></a>

# qca.forward.types.skill\_version\_list\_params

<a id="qca.forward.types.skill_version_list_params.SkillVersionListParams"></a>

## SkillVersionListParams

```python
class SkillVersionListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/skill_version_list_params.py)

<a id="qca.forward.types.skill_version_list_params.SkillVersionListParams.limit"></a>

#### limit

<a id="qca.forward.types.skill_version_list_params.SkillVersionListParams.page"></a>

#### page

<a id="qca.forward.types.system_override"></a>

# qca.forward.types.system\_override

<a id="qca.forward.types.system_override.SystemOverride"></a>

## SystemOverride

```python
class SystemOverride(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/system_override.py)

<a id="qca.forward.types.system_override.SystemOverride.mode"></a>

#### mode

<a id="qca.forward.types.system_override.SystemOverride.content"></a>

#### content

<a id="qca.forward.types.system_override_param"></a>

# qca.forward.types.system\_override\_param

<a id="qca.forward.types.system_override_param.SystemOverrideParam"></a>

## SystemOverrideParam

```python
class SystemOverrideParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/system_override_param.py)

<a id="qca.forward.types.system_override_param.SystemOverrideParam.mode"></a>

#### mode

<a id="qca.forward.types.system_override_param.SystemOverrideParam.content"></a>

#### content

<a id="qca.forward.types.template"></a>

# qca.forward.types.template

<a id="qca.forward.types.template.Template"></a>

## Template

```python
class Template(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/template.py)

<a id="qca.forward.types.template.Template.type"></a>

#### type

<a id="qca.forward.types.template.Template.id"></a>

#### id

<a id="qca.forward.types.template.Template.name"></a>

#### name

<a id="qca.forward.types.template.Template.description"></a>

#### description

<a id="qca.forward.types.template.Template.status"></a>

#### status

<a id="qca.forward.types.template.Template.created_at"></a>

#### created\_at

<a id="qca.forward.types.template.Template.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.template.Template.model"></a>

#### model

<a id="qca.forward.types.template.Template.multiagent"></a>

#### multiagent

<a id="qca.forward.types.template.Template.environment_id"></a>

#### environment\_id

<a id="qca.forward.types.template.Template.vaults"></a>

#### vaults

<a id="qca.forward.types.template.Template.files"></a>

#### files

<a id="qca.forward.types.template.Template.github_repositories"></a>

#### github\_repositories

<a id="qca.forward.types.template.Template.system"></a>

#### system

<a id="qca.forward.types.template.Template.tools"></a>

#### tools

<a id="qca.forward.types.template.Template.mcp_servers"></a>

#### mcp\_servers

<a id="qca.forward.types.template.Template.skills"></a>

#### skills

<a id="qca.forward.types.template.Template.environment_variables"></a>

#### environment\_variables

<a id="qca.forward.types.template.Template.metadata"></a>

#### metadata

<a id="qca.forward.types.template_archive_params"></a>

# qca.forward.types.template\_archive\_params

<a id="qca.forward.types.template_archive_params.TemplateArchiveParams"></a>

## TemplateArchiveParams

```python
class TemplateArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/template_archive_params.py)

<a id="qca.forward.types.template_archive_params.TemplateArchiveParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.template_clone_params"></a>

# qca.forward.types.template\_clone\_params

<a id="qca.forward.types.template_clone_params.TemplateCloneParams"></a>

## TemplateCloneParams

```python
class TemplateCloneParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/template_clone_params.py)

<a id="qca.forward.types.template_clone_params.TemplateCloneParams.name"></a>

#### name

<a id="qca.forward.types.template_clone_params.TemplateCloneParams.description"></a>

#### description

<a id="qca.forward.types.template_clone_params.TemplateCloneParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.template_create_params"></a>

# qca.forward.types.template\_create\_params

<a id="qca.forward.types.template_create_params.TemplateCreateParams"></a>

## TemplateCreateParams

```python
class TemplateCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/template_create_params.py)

<a id="qca.forward.types.template_create_params.TemplateCreateParams.name"></a>

#### name

<a id="qca.forward.types.template_create_params.TemplateCreateParams.model"></a>

#### model

<a id="qca.forward.types.template_create_params.TemplateCreateParams.environment_id"></a>

#### environment\_id

<a id="qca.forward.types.template_create_params.TemplateCreateParams.description"></a>

#### description

<a id="qca.forward.types.template_create_params.TemplateCreateParams.system"></a>

#### system

<a id="qca.forward.types.template_create_params.TemplateCreateParams.tools"></a>

#### tools

<a id="qca.forward.types.template_create_params.TemplateCreateParams.mcp_servers"></a>

#### mcp\_servers

<a id="qca.forward.types.template_create_params.TemplateCreateParams.skills"></a>

#### skills

<a id="qca.forward.types.template_create_params.TemplateCreateParams.multiagent"></a>

#### multiagent

<a id="qca.forward.types.template_create_params.TemplateCreateParams.vaults"></a>

#### vaults

<a id="qca.forward.types.template_create_params.TemplateCreateParams.files"></a>

#### files

<a id="qca.forward.types.template_create_params.TemplateCreateParams.github_repositories"></a>

#### github\_repositories

<a id="qca.forward.types.template_create_params.TemplateCreateParams.environment_variables"></a>

#### environment\_variables

<a id="qca.forward.types.template_create_params.TemplateCreateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.template_create_params.TemplateCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.template_create_params.TemplateCreateParams.beta"></a>

#### beta

<a id="qca.forward.types.template_list_params"></a>

# qca.forward.types.template\_list\_params

<a id="qca.forward.types.template_list_params.TemplateListParams"></a>

## TemplateListParams

```python
class TemplateListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/template_list_params.py)

<a id="qca.forward.types.template_list_params.TemplateListParams.status"></a>

#### status

<a id="qca.forward.types.template_list_params.TemplateListParams.limit"></a>

#### limit

<a id="qca.forward.types.template_list_params.TemplateListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.template_list_params.TemplateListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.template_update_params"></a>

# qca.forward.types.template\_update\_params

<a id="qca.forward.types.template_update_params.TemplateUpdateParams"></a>

## TemplateUpdateParams

```python
class TemplateUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/template_update_params.py)

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.name"></a>

#### name

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.description"></a>

#### description

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.model"></a>

#### model

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.system"></a>

#### system

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.tools"></a>

#### tools

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.mcp_servers"></a>

#### mcp\_servers

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.skills"></a>

#### skills

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.multiagent"></a>

#### multiagent

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.environment_id"></a>

#### environment\_id

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.vaults"></a>

#### vaults

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.files"></a>

#### files

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.github_repositories"></a>

#### github\_repositories

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.environment_variables"></a>

#### environment\_variables

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.template_update_params.TemplateUpdateParams.beta"></a>

#### beta

<a id="qca.forward.types.tool"></a>

# qca.forward.types.tool

<a id="qca.forward.types.tool.Tool"></a>

## Tool

```python
class Tool(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/tool.py)

<a id="qca.forward.types.tool.Tool.type"></a>

#### type

<a id="qca.forward.types.tool.Tool.enabled_tools"></a>

#### enabled\_tools

<a id="qca.forward.types.tool.Tool.disallowed_tools"></a>

#### disallowed\_tools

<a id="qca.forward.types.tool.Tool.configs"></a>

#### configs

<a id="qca.forward.types.tool.Tool.mcp_server_name"></a>

#### mcp\_server\_name

<a id="qca.forward.types.tool.Tool.name"></a>

#### name

<a id="qca.forward.types.tool.Tool.description"></a>

#### description

<a id="qca.forward.types.tool.Tool.input_schema"></a>

#### input\_schema

<a id="qca.forward.types.tool_config"></a>

# qca.forward.types.tool\_config

<a id="qca.forward.types.tool_config.ToolConfig"></a>

## ToolConfig

```python
class ToolConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/tool_config.py)

<a id="qca.forward.types.tool_config.ToolConfig.name"></a>

#### name

<a id="qca.forward.types.tool_config.ToolConfig.enabled"></a>

#### enabled

<a id="qca.forward.types.tool_config.ToolConfig.permission_policy"></a>

#### permission\_policy

<a id="qca.forward.types.tool_config_param"></a>

# qca.forward.types.tool\_config\_param

<a id="qca.forward.types.tool_config_param.ToolConfigParam"></a>

## ToolConfigParam

```python
class ToolConfigParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/tool_config_param.py)

<a id="qca.forward.types.tool_config_param.ToolConfigParam.name"></a>

#### name

<a id="qca.forward.types.tool_config_param.ToolConfigParam.enabled"></a>

#### enabled

<a id="qca.forward.types.tool_config_param.ToolConfigParam.permission_policy"></a>

#### permission\_policy

<a id="qca.forward.types.tool_override"></a>

# qca.forward.types.tool\_override

<a id="qca.forward.types.tool_override.ToolOverride"></a>

## ToolOverride

```python
class ToolOverride(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/tool_override.py)

<a id="qca.forward.types.tool_override.ToolOverride.enabled"></a>

#### enabled

<a id="qca.forward.types.tool_override.ToolOverride.permission_policy"></a>

#### permission\_policy

<a id="qca.forward.types.tool_override_param"></a>

# qca.forward.types.tool\_override\_param

<a id="qca.forward.types.tool_override_param.ToolOverrideParam"></a>

## ToolOverrideParam

```python
class ToolOverrideParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/tool_override_param.py)

<a id="qca.forward.types.tool_override_param.ToolOverrideParam.enabled"></a>

#### enabled

<a id="qca.forward.types.tool_override_param.ToolOverrideParam.permission_policy"></a>

#### permission\_policy

<a id="qca.forward.types.tool_param"></a>

# qca.forward.types.tool\_param

<a id="qca.forward.types.tool_param.ToolParam"></a>

## ToolParam

```python
class ToolParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/tool_param.py)

<a id="qca.forward.types.tool_param.ToolParam.type"></a>

#### type

<a id="qca.forward.types.tool_param.ToolParam.enabled_tools"></a>

#### enabled\_tools

<a id="qca.forward.types.tool_param.ToolParam.disallowed_tools"></a>

#### disallowed\_tools

<a id="qca.forward.types.tool_param.ToolParam.configs"></a>

#### configs

<a id="qca.forward.types.tool_param.ToolParam.mcp_server_name"></a>

#### mcp\_server\_name

<a id="qca.forward.types.tool_param.ToolParam.name"></a>

#### name

<a id="qca.forward.types.tool_param.ToolParam.description"></a>

#### description

<a id="qca.forward.types.tool_param.ToolParam.input_schema"></a>

#### input\_schema

<a id="qca.forward.types.vault"></a>

# qca.forward.types.vault

<a id="qca.forward.types.vault.Vault"></a>

## Vault

```python
class Vault(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/vault.py)

<a id="qca.forward.types.vault.Vault.id"></a>

#### id

<a id="qca.forward.types.vault.Vault.type"></a>

#### type

<a id="qca.forward.types.vault.Vault.display_name"></a>

#### display\_name

<a id="qca.forward.types.vault.Vault.metadata"></a>

#### metadata

<a id="qca.forward.types.vault.Vault.created_at"></a>

#### created\_at

<a id="qca.forward.types.vault.Vault.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.vault.Vault.identity_id"></a>

#### identity\_id

<a id="qca.forward.types.vault_create_params"></a>

# qca.forward.types.vault\_create\_params

<a id="qca.forward.types.vault_create_params.VaultCreateParams"></a>

## VaultCreateParams

```python
class VaultCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/vault_create_params.py)

<a id="qca.forward.types.vault_create_params.VaultCreateParams.display_name"></a>

#### display\_name

<a id="qca.forward.types.vault_create_params.VaultCreateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.vault_create_params.VaultCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.vault_credential"></a>

# qca.forward.types.vault\_credential

<a id="qca.forward.types.vault_credential.VaultCredential"></a>

## VaultCredential

```python
class VaultCredential(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/vault_credential.py)

<a id="qca.forward.types.vault_credential.VaultCredential.id"></a>

#### id

<a id="qca.forward.types.vault_credential.VaultCredential.type"></a>

#### type

<a id="qca.forward.types.vault_credential.VaultCredential.vault_id"></a>

#### vault\_id

<a id="qca.forward.types.vault_credential.VaultCredential.auth"></a>

#### auth

<a id="qca.forward.types.vault_credential.VaultCredential.display_name"></a>

#### display\_name

<a id="qca.forward.types.vault_credential.VaultCredential.metadata"></a>

#### metadata

<a id="qca.forward.types.vault_credential.VaultCredential.created_at"></a>

#### created\_at

<a id="qca.forward.types.vault_credential.VaultCredential.updated_at"></a>

#### updated\_at

<a id="qca.forward.types.vault_credential_auth"></a>

# qca.forward.types.vault\_credential\_auth

<a id="qca.forward.types.vault_credential_auth.VaultCredentialAuth"></a>

## VaultCredentialAuth

```python
class VaultCredentialAuth(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/vault_credential_auth.py)

<a id="qca.forward.types.vault_credential_auth.VaultCredentialAuth.type"></a>

#### type

<a id="qca.forward.types.vault_credential_auth.VaultCredentialAuth.mcp_server_url"></a>

#### mcp\_server\_url

<a id="qca.forward.types.vault_credential_create_params"></a>

# qca.forward.types.vault\_credential\_create\_params

<a id="qca.forward.types.vault_credential_create_params.VaultCredentialCreateParams"></a>

## VaultCredentialCreateParams

```python
class VaultCredentialCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/vault_credential_create_params.py)

<a id="qca.forward.types.vault_credential_create_params.VaultCredentialCreateParams.auth"></a>

#### auth

<a id="qca.forward.types.vault_credential_create_params.VaultCredentialCreateParams.display_name"></a>

#### display\_name

<a id="qca.forward.types.vault_credential_create_params.VaultCredentialCreateParams.metadata"></a>

#### metadata

<a id="qca.forward.types.vault_credential_create_params.VaultCredentialCreateParams.idempotency_key"></a>

#### idempotency\_key

<a id="qca.forward.types.vault_credential_list_params"></a>

# qca.forward.types.vault\_credential\_list\_params

<a id="qca.forward.types.vault_credential_list_params.VaultCredentialListParams"></a>

## VaultCredentialListParams

```python
class VaultCredentialListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/vault_credential_list_params.py)

<a id="qca.forward.types.vault_credential_list_params.VaultCredentialListParams.limit"></a>

#### limit

<a id="qca.forward.types.vault_credential_list_params.VaultCredentialListParams.page"></a>

#### page

<a id="qca.forward.types.vault_credential_list_params.VaultCredentialListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.vault_credential_list_params.VaultCredentialListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.vault_credential_list_params.VaultCredentialListParams.name"></a>

#### name

<a id="qca.forward.types.vault_list_params"></a>

# qca.forward.types.vault\_list\_params

<a id="qca.forward.types.vault_list_params.VaultListParams"></a>

## VaultListParams

```python
class VaultListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/forward/types/vault_list_params.py)

<a id="qca.forward.types.vault_list_params.VaultListParams.limit"></a>

#### limit

<a id="qca.forward.types.vault_list_params.VaultListParams.page"></a>

#### page

<a id="qca.forward.types.vault_list_params.VaultListParams.after_id"></a>

#### after\_id

<a id="qca.forward.types.vault_list_params.VaultListParams.before_id"></a>

#### before\_id

<a id="qca.forward.types.vault_list_params.VaultListParams.name"></a>

#### name

<a id="qca.managed"></a>

# qca.managed

<a id="qca.managed.Client"></a>

#### Client

<a id="qca.managed.AsyncClient"></a>

#### AsyncClient

<a id="qca.managed.ManagedClient"></a>

#### ManagedClient

<a id="qca.managed.AsyncManagedClient"></a>

#### AsyncManagedClient

<a id="qca.managed._client"></a>

# qca.managed.\_client

<a id="qca.managed._client.Managed"></a>

## Managed

```python
class Managed(SyncAPIClient)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.Managed.agents"></a>

#### agents

```python
@cached_property
def agents() -> Agents
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.Managed.sessions"></a>

#### sessions

```python
@cached_property
def sessions() -> Sessions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.Managed.deployments"></a>

#### deployments

```python
@cached_property
def deployments() -> Deployments
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.Managed.deployment_runs"></a>

#### deployment\_runs

```python
@cached_property
def deployment_runs() -> DeploymentRuns
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.Managed.dreams"></a>

#### dreams

```python
@cached_property
def dreams() -> Dreams
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.Managed.environments"></a>

#### environments

```python
@cached_property
def environments() -> Environments
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.Managed.skills"></a>

#### skills

```python
@cached_property
def skills() -> Skills
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.Managed.vaults"></a>

#### vaults

```python
@cached_property
def vaults() -> Vaults
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.Managed.files"></a>

#### files

```python
@cached_property
def files() -> Files
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.Managed.memory_stores"></a>

#### memory\_stores

```python
@cached_property
def memory_stores() -> MemoryStores
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.Managed.models"></a>

#### models

```python
@cached_property
def models() -> Models
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged"></a>

## AsyncManaged

```python
class AsyncManaged(AsyncAPIClient)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged.agents"></a>

#### agents

```python
@cached_property
def agents() -> AsyncAgents
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged.sessions"></a>

#### sessions

```python
@cached_property
def sessions() -> AsyncSessions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged.deployments"></a>

#### deployments

```python
@cached_property
def deployments() -> AsyncDeployments
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged.deployment_runs"></a>

#### deployment\_runs

```python
@cached_property
def deployment_runs() -> AsyncDeploymentRuns
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged.dreams"></a>

#### dreams

```python
@cached_property
def dreams() -> AsyncDreams
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged.environments"></a>

#### environments

```python
@cached_property
def environments() -> AsyncEnvironments
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged.skills"></a>

#### skills

```python
@cached_property
def skills() -> AsyncSkills
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged.vaults"></a>

#### vaults

```python
@cached_property
def vaults() -> AsyncVaults
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged.files"></a>

#### files

```python
@cached_property
def files() -> AsyncFiles
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged.memory_stores"></a>

#### memory\_stores

```python
@cached_property
def memory_stores() -> AsyncMemoryStores
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed._client.AsyncManaged.models"></a>

#### models

```python
@cached_property
def models() -> AsyncModels
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/_client.py)

<a id="qca.managed.resources.agents.agents"></a>

# qca.managed.resources.agents.agents

<a id="qca.managed.resources.agents.agents.Agents"></a>

## Agents

```python
class Agents(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

<a id="qca.managed.resources.agents.agents.Agents.versions"></a>

#### versions

```python
@cached_property
def versions() -> Versions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

<a id="qca.managed.resources.agents.agents.Agents.create"></a>

#### create

```python
def create(
        *,
        model: Union[str, ModelConfigParams],
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[URLMCPServerParams], None,
                           NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentParams, None, NotGiven] = NOT_GIVEN,
        skills: Union[List[Union[QoderSkillParams, CustomSkillParams]], None,
                      NotGiven] = NOT_GIVEN,
        tools: Union[List[Union[AgentToolset20260401Params, MCPToolsetParams,
                                CustomToolParams]], None,
                     NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Agent
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

POST /agents.

<a id="qca.managed.resources.agents.agents.Agents.retrieve"></a>

#### retrieve

```python
def retrieve(
        agent_id: str,
        *,
        version: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Agent
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

GET /agents/{agent_id}.

<a id="qca.managed.resources.agents.agents.Agents.update"></a>

#### update

```python
def update(
        agent_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        version: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[URLMCPServerParams], None,
                           NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[Union[QoderSkillParams, CustomSkillParams]], None,
                      NotGiven] = NOT_GIVEN,
        tools: Union[List[Union[AgentToolset20260401Params, MCPToolsetParams,
                                CustomToolParams]], None,
                     NotGiven] = NOT_GIVEN,
        model: Union[Union[str, ModelConfigParams], None,
                     NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentParams, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Agent
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

POST /agents/{agent_id}.

<a id="qca.managed.resources.agents.agents.Agents.list"></a>

#### list

```python
def list(
    *,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Agent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

GET /agents.

<a id="qca.managed.resources.agents.agents.Agents.archive"></a>

#### archive

```python
def archive(
        agent_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Agent
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

POST /agents/{agent_id}/archive.

<a id="qca.managed.resources.agents.agents.AsyncAgents"></a>

## AsyncAgents

```python
class AsyncAgents(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

<a id="qca.managed.resources.agents.agents.AsyncAgents.versions"></a>

#### versions

```python
@cached_property
def versions() -> AsyncVersions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

<a id="qca.managed.resources.agents.agents.AsyncAgents.create"></a>

#### create

```python
async def create(
        *,
        model: Union[str, ModelConfigParams],
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[URLMCPServerParams], None,
                           NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentParams, None, NotGiven] = NOT_GIVEN,
        skills: Union[List[Union[QoderSkillParams, CustomSkillParams]], None,
                      NotGiven] = NOT_GIVEN,
        tools: Union[List[Union[AgentToolset20260401Params, MCPToolsetParams,
                                CustomToolParams]], None,
                     NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Agent
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

POST /agents.

<a id="qca.managed.resources.agents.agents.AsyncAgents.retrieve"></a>

#### retrieve

```python
async def retrieve(
        agent_id: str,
        *,
        version: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Agent
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

GET /agents/{agent_id}.

<a id="qca.managed.resources.agents.agents.AsyncAgents.update"></a>

#### update

```python
async def update(
        agent_id: str,
        *,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        system: Union[str, None, NotGiven] = NOT_GIVEN,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        version: Union[int, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        mcp_servers: Union[List[URLMCPServerParams], None,
                           NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        skills: Union[List[Union[QoderSkillParams, CustomSkillParams]], None,
                      NotGiven] = NOT_GIVEN,
        tools: Union[List[Union[AgentToolset20260401Params, MCPToolsetParams,
                                CustomToolParams]], None,
                     NotGiven] = NOT_GIVEN,
        model: Union[Union[str, ModelConfigParams], None,
                     NotGiven] = NOT_GIVEN,
        multiagent: Union[MultiagentParams, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Agent
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

POST /agents/{agent_id}.

<a id="qca.managed.resources.agents.agents.AsyncAgents.list"></a>

#### list

```python
def list(
    *,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Agent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

GET /agents.

<a id="qca.managed.resources.agents.agents.AsyncAgents.archive"></a>

#### archive

```python
async def archive(
        agent_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Agent
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/agents.py)

POST /agents/{agent_id}/archive.

<a id="qca.managed.resources.agents.versions"></a>

# qca.managed.resources.agents.versions

<a id="qca.managed.resources.agents.versions.Versions"></a>

## Versions

```python
class Versions(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/versions.py)

<a id="qca.managed.resources.agents.versions.Versions.list"></a>

#### list

```python
def list(
    agent_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Agent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/versions.py)

GET /agents/{agent_id}/versions.

<a id="qca.managed.resources.agents.versions.AsyncVersions"></a>

## AsyncVersions

```python
class AsyncVersions(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/versions.py)

<a id="qca.managed.resources.agents.versions.AsyncVersions.list"></a>

#### list

```python
def list(
    agent_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Agent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/agents/versions.py)

GET /agents/{agent_id}/versions.

<a id="qca.managed.resources.deployment_runs"></a>

# qca.managed.resources.deployment\_runs

<a id="qca.managed.resources.deployment_runs.DeploymentRuns"></a>

## DeploymentRuns

```python
class DeploymentRuns(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployment_runs.py)

<a id="qca.managed.resources.deployment_runs.DeploymentRuns.retrieve"></a>

#### retrieve

```python
def retrieve(
    deployment_run_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeploymentRun
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployment_runs.py)

GET /deployment_runs/{deployment_run_id}.

<a id="qca.managed.resources.deployment_runs.DeploymentRuns.list"></a>

#### list

```python
def list(
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    deployment_id: Union[str, None, NotGiven] = NOT_GIVEN,
    has_error: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    trigger_type: Union[Literal["schedule", "manual"], None,
                        NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[DeploymentRun]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployment_runs.py)

GET /deployment_runs.

<a id="qca.managed.resources.deployment_runs.AsyncDeploymentRuns"></a>

## AsyncDeploymentRuns

```python
class AsyncDeploymentRuns(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployment_runs.py)

<a id="qca.managed.resources.deployment_runs.AsyncDeploymentRuns.retrieve"></a>

#### retrieve

```python
async def retrieve(
    deployment_run_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeploymentRun
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployment_runs.py)

GET /deployment_runs/{deployment_run_id}.

<a id="qca.managed.resources.deployment_runs.AsyncDeploymentRuns.list"></a>

#### list

```python
def list(
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    deployment_id: Union[str, None, NotGiven] = NOT_GIVEN,
    has_error: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    trigger_type: Union[Literal["schedule", "manual"], None,
                        NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[DeploymentRun]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployment_runs.py)

GET /deployment_runs.

<a id="qca.managed.resources.deployments"></a>

# qca.managed.resources.deployments

<a id="qca.managed.resources.deployments.Deployments"></a>

## Deployments

```python
class Deployments(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

<a id="qca.managed.resources.deployments.Deployments.create"></a>

#### create

```python
def create(
    *,
    agent: Union[str, AgentParams],
    environment_id: str,
    initial_events: List[Union[UserMessageEventParams,
                               UserDefineOutcomeEventParams,
                               SystemMessageEventParams]],
    name: str,
    environment_variables: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    resources: Union[List[Union[GitHubRepositoryResourceParams,
                                FileResourceParams, MemoryStoreResourceParam]],
                     None, NotGiven] = NOT_GIVEN,
    schedule: Union[ScheduleParams, None, NotGiven] = NOT_GIVEN,
    vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments.

<a id="qca.managed.resources.deployments.Deployments.retrieve"></a>

#### retrieve

```python
def retrieve(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

GET /deployments/{deployment_id}.

<a id="qca.managed.resources.deployments.Deployments.update"></a>

#### update

```python
def update(
    deployment_id: str,
    *,
    environment_variables: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    resources: Union[List[Union[GitHubRepositoryResourceParams,
                                FileResourceParams, MemoryStoreResourceParam]],
                     None, NotGiven] = NOT_GIVEN,
    vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
    agent: Union[Union[str, AgentParams], None, NotGiven] = NOT_GIVEN,
    budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
    initial_events: Union[List[Union[UserMessageEventParams,
                                     UserDefineOutcomeEventParams,
                                     SystemMessageEventParams]], None,
                          NotGiven] = NOT_GIVEN,
    schedule: Union[ScheduleParams, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments/{deployment_id}.

<a id="qca.managed.resources.deployments.Deployments.list"></a>

#### list

```python
def list(
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    agent_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[Literal["active", "paused"], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Deployment]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

GET /deployments.

<a id="qca.managed.resources.deployments.Deployments.archive"></a>

#### archive

```python
def archive(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments/{deployment_id}/archive.

<a id="qca.managed.resources.deployments.Deployments.pause"></a>

#### pause

```python
def pause(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments/{deployment_id}/pause.

<a id="qca.managed.resources.deployments.Deployments.run"></a>

#### run

```python
def run(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeploymentRun
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments/{deployment_id}/run.

<a id="qca.managed.resources.deployments.Deployments.unpause"></a>

#### unpause

```python
def unpause(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments/{deployment_id}/unpause.

<a id="qca.managed.resources.deployments.AsyncDeployments"></a>

## AsyncDeployments

```python
class AsyncDeployments(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

<a id="qca.managed.resources.deployments.AsyncDeployments.create"></a>

#### create

```python
async def create(
    *,
    agent: Union[str, AgentParams],
    environment_id: str,
    initial_events: List[Union[UserMessageEventParams,
                               UserDefineOutcomeEventParams,
                               SystemMessageEventParams]],
    name: str,
    environment_variables: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    resources: Union[List[Union[GitHubRepositoryResourceParams,
                                FileResourceParams, MemoryStoreResourceParam]],
                     None, NotGiven] = NOT_GIVEN,
    schedule: Union[ScheduleParams, None, NotGiven] = NOT_GIVEN,
    vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments.

<a id="qca.managed.resources.deployments.AsyncDeployments.retrieve"></a>

#### retrieve

```python
async def retrieve(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

GET /deployments/{deployment_id}.

<a id="qca.managed.resources.deployments.AsyncDeployments.update"></a>

#### update

```python
async def update(
    deployment_id: str,
    *,
    environment_variables: Union[str, None, NotGiven] = NOT_GIVEN,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    environment_id: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    resources: Union[List[Union[GitHubRepositoryResourceParams,
                                FileResourceParams, MemoryStoreResourceParam]],
                     None, NotGiven] = NOT_GIVEN,
    vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
    agent: Union[Union[str, AgentParams], None, NotGiven] = NOT_GIVEN,
    budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
    initial_events: Union[List[Union[UserMessageEventParams,
                                     UserDefineOutcomeEventParams,
                                     SystemMessageEventParams]], None,
                          NotGiven] = NOT_GIVEN,
    schedule: Union[ScheduleParams, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments/{deployment_id}.

<a id="qca.managed.resources.deployments.AsyncDeployments.list"></a>

#### list

```python
def list(
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    agent_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    status: Union[Literal["active", "paused"], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Deployment]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

GET /deployments.

<a id="qca.managed.resources.deployments.AsyncDeployments.archive"></a>

#### archive

```python
async def archive(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments/{deployment_id}/archive.

<a id="qca.managed.resources.deployments.AsyncDeployments.pause"></a>

#### pause

```python
async def pause(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments/{deployment_id}/pause.

<a id="qca.managed.resources.deployments.AsyncDeployments.run"></a>

#### run

```python
async def run(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeploymentRun
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments/{deployment_id}/run.

<a id="qca.managed.resources.deployments.AsyncDeployments.unpause"></a>

#### unpause

```python
async def unpause(
    deployment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Deployment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/deployments.py)

POST /deployments/{deployment_id}/unpause.

<a id="qca.managed.resources.dreams"></a>

# qca.managed.resources.dreams

<a id="qca.managed.resources.dreams.Dreams"></a>

## Dreams

```python
class Dreams(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

<a id="qca.managed.resources.dreams.Dreams.create"></a>

#### create

```python
def create(
        *,
        inputs: List[Union[DreamMemoryStoreInputParam,
                           DreamSessionsInputParam]],
        model: Union[str, DreamModelConfigParam],
        instructions: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        output_behavior: Union[Union[OutputBehaviorCreateNewParam,
                                     OutputBehaviorUpdateExistingParam], None,
                               NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Dream
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

POST /dreams.

<a id="qca.managed.resources.dreams.Dreams.retrieve"></a>

#### retrieve

```python
def retrieve(
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Dream
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

GET /dreams/{dream_id}.

<a id="qca.managed.resources.dreams.Dreams.list"></a>

#### list

```python
def list(
    *,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    statuses: Union[List[Literal["pending", "running", "completed", "failed",
                                 "canceled"]], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Dream]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

GET /dreams.

<a id="qca.managed.resources.dreams.Dreams.archive"></a>

#### archive

```python
def archive(
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Dream
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

POST /dreams/{dream_id}/archive.

<a id="qca.managed.resources.dreams.Dreams.cancel"></a>

#### cancel

```python
def cancel(
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Dream
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

POST /dreams/{dream_id}/cancel.

<a id="qca.managed.resources.dreams.AsyncDreams"></a>

## AsyncDreams

```python
class AsyncDreams(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

<a id="qca.managed.resources.dreams.AsyncDreams.create"></a>

#### create

```python
async def create(
        *,
        inputs: List[Union[DreamMemoryStoreInputParam,
                           DreamSessionsInputParam]],
        model: Union[str, DreamModelConfigParam],
        instructions: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        output_behavior: Union[Union[OutputBehaviorCreateNewParam,
                                     OutputBehaviorUpdateExistingParam], None,
                               NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Dream
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

POST /dreams.

<a id="qca.managed.resources.dreams.AsyncDreams.retrieve"></a>

#### retrieve

```python
async def retrieve(
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Dream
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

GET /dreams/{dream_id}.

<a id="qca.managed.resources.dreams.AsyncDreams.list"></a>

#### list

```python
def list(
    *,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    statuses: Union[List[Literal["pending", "running", "completed", "failed",
                                 "canceled"]], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Dream]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

GET /dreams.

<a id="qca.managed.resources.dreams.AsyncDreams.archive"></a>

#### archive

```python
async def archive(
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Dream
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

POST /dreams/{dream_id}/archive.

<a id="qca.managed.resources.dreams.AsyncDreams.cancel"></a>

#### cancel

```python
async def cancel(
        dream_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Dream
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/dreams.py)

POST /dreams/{dream_id}/cancel.

<a id="qca.managed.resources.environments.environments"></a>

# qca.managed.resources.environments.environments

<a id="qca.managed.resources.environments.environments.Environments"></a>

## Environments

```python
class Environments(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

<a id="qca.managed.resources.environments.environments.Environments.work"></a>

#### work

```python
@cached_property
def work() -> Work
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

<a id="qca.managed.resources.environments.environments.Environments.create"></a>

#### create

```python
def create(
    *,
    name: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Union[CloudConfigParams, SelfHostedConfigParams], None,
                  NotGiven] = NOT_GIVEN,
    scope: Union[Literal["organization", "account"], None,
                 NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

POST /environments.

<a id="qca.managed.resources.environments.environments.Environments.retrieve"></a>

#### retrieve

```python
def retrieve(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

GET /environments/{environment_id}.

<a id="qca.managed.resources.environments.environments.Environments.update"></a>

#### update

```python
def update(
    environment_id: str,
    *,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Union[CloudConfigParams, SelfHostedConfigParams], None,
                  NotGiven] = NOT_GIVEN,
    scope: Union[Literal["organization", "account"], None,
                 NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

POST /environments/{environment_id}.

<a id="qca.managed.resources.environments.environments.Environments.list"></a>

#### list

```python
def list(
    *,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Environment]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

GET /environments.

<a id="qca.managed.resources.environments.environments.Environments.delete"></a>

#### delete

```python
def delete(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> EnvironmentDeleteResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

DELETE /environments/{environment_id}.

<a id="qca.managed.resources.environments.environments.Environments.archive"></a>

#### archive

```python
def archive(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

POST /environments/{environment_id}/archive.

<a id="qca.managed.resources.environments.environments.AsyncEnvironments"></a>

## AsyncEnvironments

```python
class AsyncEnvironments(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

<a id="qca.managed.resources.environments.environments.AsyncEnvironments.work"></a>

#### work

```python
@cached_property
def work() -> AsyncWork
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

<a id="qca.managed.resources.environments.environments.AsyncEnvironments.create"></a>

#### create

```python
async def create(
    *,
    name: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Union[CloudConfigParams, SelfHostedConfigParams], None,
                  NotGiven] = NOT_GIVEN,
    scope: Union[Literal["organization", "account"], None,
                 NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

POST /environments.

<a id="qca.managed.resources.environments.environments.AsyncEnvironments.retrieve"></a>

#### retrieve

```python
async def retrieve(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

GET /environments/{environment_id}.

<a id="qca.managed.resources.environments.environments.AsyncEnvironments.update"></a>

#### update

```python
async def update(
    environment_id: str,
    *,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    config: Union[Union[CloudConfigParams, SelfHostedConfigParams], None,
                  NotGiven] = NOT_GIVEN,
    scope: Union[Literal["organization", "account"], None,
                 NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

POST /environments/{environment_id}.

<a id="qca.managed.resources.environments.environments.AsyncEnvironments.list"></a>

#### list

```python
def list(
    *,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Environment]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

GET /environments.

<a id="qca.managed.resources.environments.environments.AsyncEnvironments.delete"></a>

#### delete

```python
async def delete(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> EnvironmentDeleteResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

DELETE /environments/{environment_id}.

<a id="qca.managed.resources.environments.environments.AsyncEnvironments.archive"></a>

#### archive

```python
async def archive(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Environment
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/environments.py)

POST /environments/{environment_id}/archive.

<a id="qca.managed.resources.environments.work"></a>

# qca.managed.resources.environments.work

<a id="qca.managed.resources.environments.work.Work"></a>

## Work

```python
class Work(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

<a id="qca.managed.resources.environments.work.Work.retrieve"></a>

#### retrieve

```python
def retrieve(
    work_id: str,
    *,
    environment_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWork
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

GET /environments/{environment_id}/work/{work_id}.

<a id="qca.managed.resources.environments.work.Work.update"></a>

#### update

```python
def update(
    work_id: str,
    *,
    environment_id: str,
    metadata: Dict[str, Any],
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWork
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

POST /environments/{environment_id}/work/{work_id}.

<a id="qca.managed.resources.environments.work.Work.list"></a>

#### list

```python
def list(
    environment_id: str,
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[SelfHostedWork]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

GET /environments/{environment_id}/work.

<a id="qca.managed.resources.environments.work.Work.ack"></a>

#### ack

```python
def ack(
    work_id: str,
    *,
    environment_id: str,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWork
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

POST /environments/{environment_id}/work/{work_id}/ack.

<a id="qca.managed.resources.environments.work.Work.heartbeat"></a>

#### heartbeat

```python
def heartbeat(
    work_id: str,
    *,
    environment_id: str,
    desired_ttl_seconds: Union[int, None, NotGiven] = NOT_GIVEN,
    expected_last_heartbeat: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWorkHeartbeatResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

POST /environments/{environment_id}/work/{work_id}/heartbeat.

<a id="qca.managed.resources.environments.work.Work.poll"></a>

#### poll

```python
def poll(
    environment_id: str,
    *,
    block_ms: Union[int, None, NotGiven] = NOT_GIVEN,
    reclaim_older_than_ms: Union[int, None, NotGiven] = NOT_GIVEN,
    worker_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Optional[SelfHostedWork]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

GET /environments/{environment_id}/work/poll.

<a id="qca.managed.resources.environments.work.Work.stats"></a>

#### stats

```python
def stats(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWorkQueueStats
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

GET /environments/{environment_id}/work/stats.

<a id="qca.managed.resources.environments.work.Work.stop"></a>

#### stop

```python
def stop(
    work_id: str,
    *,
    environment_id: str,
    force: Union[bool, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWork
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

POST /environments/{environment_id}/work/{work_id}/stop.

<a id="qca.managed.resources.environments.work.AsyncWork"></a>

## AsyncWork

```python
class AsyncWork(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

<a id="qca.managed.resources.environments.work.AsyncWork.retrieve"></a>

#### retrieve

```python
async def retrieve(
    work_id: str,
    *,
    environment_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWork
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

GET /environments/{environment_id}/work/{work_id}.

<a id="qca.managed.resources.environments.work.AsyncWork.update"></a>

#### update

```python
async def update(
    work_id: str,
    *,
    environment_id: str,
    metadata: Dict[str, Any],
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWork
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

POST /environments/{environment_id}/work/{work_id}.

<a id="qca.managed.resources.environments.work.AsyncWork.list"></a>

#### list

```python
def list(
    environment_id: str,
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[SelfHostedWork]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

GET /environments/{environment_id}/work.

<a id="qca.managed.resources.environments.work.AsyncWork.ack"></a>

#### ack

```python
async def ack(
    work_id: str,
    *,
    environment_id: str,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWork
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

POST /environments/{environment_id}/work/{work_id}/ack.

<a id="qca.managed.resources.environments.work.AsyncWork.heartbeat"></a>

#### heartbeat

```python
async def heartbeat(
    work_id: str,
    *,
    environment_id: str,
    desired_ttl_seconds: Union[int, None, NotGiven] = NOT_GIVEN,
    expected_last_heartbeat: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWorkHeartbeatResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

POST /environments/{environment_id}/work/{work_id}/heartbeat.

<a id="qca.managed.resources.environments.work.AsyncWork.poll"></a>

#### poll

```python
async def poll(
    environment_id: str,
    *,
    block_ms: Union[int, None, NotGiven] = NOT_GIVEN,
    reclaim_older_than_ms: Union[int, None, NotGiven] = NOT_GIVEN,
    worker_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Optional[SelfHostedWork]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

GET /environments/{environment_id}/work/poll.

<a id="qca.managed.resources.environments.work.AsyncWork.stats"></a>

#### stats

```python
async def stats(
    environment_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWorkQueueStats
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

GET /environments/{environment_id}/work/stats.

<a id="qca.managed.resources.environments.work.AsyncWork.stop"></a>

#### stop

```python
async def stop(
    work_id: str,
    *,
    environment_id: str,
    force: Union[bool, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SelfHostedWork
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/environments/work.py)

POST /environments/{environment_id}/work/{work_id}/stop.

<a id="qca.managed.resources.files"></a>

# qca.managed.resources.files

<a id="qca.managed.resources.files.Files"></a>

## Files

```python
class Files(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

<a id="qca.managed.resources.files.Files.list"></a>

#### list

```python
def list(
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    scope_id: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[FileMetadata]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

GET /files.

<a id="qca.managed.resources.files.Files.delete"></a>

#### delete

```python
def delete(
    file_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedFile
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

DELETE /files/{file_id}.

<a id="qca.managed.resources.files.Files.download"></a>

#### download

```python
def download(
    file_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> BinaryAPIResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

GET /files/{file_id}/content.

<a id="qca.managed.resources.files.Files.retrieve_metadata"></a>

#### retrieve\_metadata

```python
def retrieve_metadata(
    file_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> FileMetadata
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

GET /files/{file_id}.

<a id="qca.managed.resources.files.Files.upload"></a>

#### upload

```python
def upload(
    *,
    file: FileTypes,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    expires_in_seconds: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> FileMetadata
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

POST /files.

<a id="qca.managed.resources.files.AsyncFiles"></a>

## AsyncFiles

```python
class AsyncFiles(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

<a id="qca.managed.resources.files.AsyncFiles.list"></a>

#### list

```python
def list(
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    scope_id: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    i_ds: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[FileMetadata]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

GET /files.

<a id="qca.managed.resources.files.AsyncFiles.delete"></a>

#### delete

```python
async def delete(
    file_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedFile
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

DELETE /files/{file_id}.

<a id="qca.managed.resources.files.AsyncFiles.download"></a>

#### download

```python
async def download(
    file_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncBinaryAPIResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

GET /files/{file_id}/content.

<a id="qca.managed.resources.files.AsyncFiles.retrieve_metadata"></a>

#### retrieve\_metadata

```python
async def retrieve_metadata(
    file_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> FileMetadata
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

GET /files/{file_id}.

<a id="qca.managed.resources.files.AsyncFiles.upload"></a>

#### upload

```python
async def upload(
    *,
    file: FileTypes,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    expires_in_seconds: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> FileMetadata
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/files.py)

POST /files.

<a id="qca.managed.resources.memory_stores.memories"></a>

# qca.managed.resources.memory\_stores.memories

<a id="qca.managed.resources.memory_stores.memories.Memories"></a>

## Memories

```python
class Memories(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

<a id="qca.managed.resources.memory_stores.memories.Memories.create"></a>

#### create

```python
def create(
        memory_store_id: str,
        *,
        content: str,
        path: str,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

POST /memory_stores/{memory_store_id}/memories.

<a id="qca.managed.resources.memory_stores.memories.Memories.retrieve"></a>

#### retrieve

```python
def retrieve(
        memory_id: str,
        *,
        memory_store_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

GET /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.managed.resources.memory_stores.memories.Memories.update"></a>

#### update

```python
def update(
        memory_id: str,
        *,
        memory_store_id: str,
        content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        content: Union[str, None, NotGiven] = NOT_GIVEN,
        path: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        precondition: Union[PreconditionParam, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

POST /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.managed.resources.memory_stores.memories.Memories.list"></a>

#### list

```python
def list(
    memory_store_id: str,
    *,
    depth: Union[int, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    path_prefix: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[MemoryListItemUnion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

GET /memory_stores/{memory_store_id}/memories.

<a id="qca.managed.resources.memory_stores.memories.Memories.delete"></a>

#### delete

```python
def delete(
    memory_id: str,
    *,
    memory_store_id: str,
    expected_content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedMemory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

DELETE /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.managed.resources.memory_stores.memories.AsyncMemories"></a>

## AsyncMemories

```python
class AsyncMemories(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

<a id="qca.managed.resources.memory_stores.memories.AsyncMemories.create"></a>

#### create

```python
async def create(
        memory_store_id: str,
        *,
        content: str,
        path: str,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

POST /memory_stores/{memory_store_id}/memories.

<a id="qca.managed.resources.memory_stores.memories.AsyncMemories.retrieve"></a>

#### retrieve

```python
async def retrieve(
        memory_id: str,
        *,
        memory_store_id: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

GET /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.managed.resources.memory_stores.memories.AsyncMemories.update"></a>

#### update

```python
async def update(
        memory_id: str,
        *,
        memory_store_id: str,
        content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        content: Union[str, None, NotGiven] = NOT_GIVEN,
        path: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
        precondition: Union[PreconditionParam, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Memory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

POST /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.managed.resources.memory_stores.memories.AsyncMemories.list"></a>

#### list

```python
def list(
    memory_store_id: str,
    *,
    depth: Union[int, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    path_prefix: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[MemoryListItemUnion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

GET /memory_stores/{memory_store_id}/memories.

<a id="qca.managed.resources.memory_stores.memories.AsyncMemories.delete"></a>

#### delete

```python
async def delete(
    memory_id: str,
    *,
    memory_store_id: str,
    expected_content_sha256: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedMemory
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memories.py)

DELETE /memory_stores/{memory_store_id}/memories/{memory_id}.

<a id="qca.managed.resources.memory_stores.memory_stores"></a>

# qca.managed.resources.memory\_stores.memory\_stores

<a id="qca.managed.resources.memory_stores.memory_stores.MemoryStores"></a>

## MemoryStores

```python
class MemoryStores(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

<a id="qca.managed.resources.memory_stores.memory_stores.MemoryStores.memories"></a>

#### memories

```python
@cached_property
def memories() -> Memories
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

<a id="qca.managed.resources.memory_stores.memory_stores.MemoryStores.memory_versions"></a>

#### memory\_versions

```python
@cached_property
def memory_versions() -> MemoryVersions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

<a id="qca.managed.resources.memory_stores.memory_stores.MemoryStores.create"></a>

#### create

```python
def create(
    *,
    name: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

POST /memory_stores.

<a id="qca.managed.resources.memory_stores.memory_stores.MemoryStores.retrieve"></a>

#### retrieve

```python
def retrieve(
    memory_store_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

GET /memory_stores/{memory_store_id}.

<a id="qca.managed.resources.memory_stores.memory_stores.MemoryStores.update"></a>

#### update

```python
def update(
    memory_store_id: str,
    *,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

POST /memory_stores/{memory_store_id}.

<a id="qca.managed.resources.memory_stores.memory_stores.MemoryStores.list"></a>

#### list

```python
def list(
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[MemoryStore]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

GET /memory_stores.

<a id="qca.managed.resources.memory_stores.memory_stores.MemoryStores.delete"></a>

#### delete

```python
def delete(
    memory_store_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedMemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

DELETE /memory_stores/{memory_store_id}.

<a id="qca.managed.resources.memory_stores.memory_stores.MemoryStores.archive"></a>

#### archive

```python
def archive(
    memory_store_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

POST /memory_stores/{memory_store_id}/archive.

<a id="qca.managed.resources.memory_stores.memory_stores.AsyncMemoryStores"></a>

## AsyncMemoryStores

```python
class AsyncMemoryStores(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

<a id="qca.managed.resources.memory_stores.memory_stores.AsyncMemoryStores.memories"></a>

#### memories

```python
@cached_property
def memories() -> AsyncMemories
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

<a id="qca.managed.resources.memory_stores.memory_stores.AsyncMemoryStores.memory_versions"></a>

#### memory\_versions

```python
@cached_property
def memory_versions() -> AsyncMemoryVersions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

<a id="qca.managed.resources.memory_stores.memory_stores.AsyncMemoryStores.create"></a>

#### create

```python
async def create(
    *,
    name: str,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

POST /memory_stores.

<a id="qca.managed.resources.memory_stores.memory_stores.AsyncMemoryStores.retrieve"></a>

#### retrieve

```python
async def retrieve(
    memory_store_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

GET /memory_stores/{memory_store_id}.

<a id="qca.managed.resources.memory_stores.memory_stores.AsyncMemoryStores.update"></a>

#### update

```python
async def update(
    memory_store_id: str,
    *,
    description: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

POST /memory_stores/{memory_store_id}.

<a id="qca.managed.resources.memory_stores.memory_stores.AsyncMemoryStores.list"></a>

#### list

```python
def list(
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[MemoryStore]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

GET /memory_stores.

<a id="qca.managed.resources.memory_stores.memory_stores.AsyncMemoryStores.delete"></a>

#### delete

```python
async def delete(
    memory_store_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedMemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

DELETE /memory_stores/{memory_store_id}.

<a id="qca.managed.resources.memory_stores.memory_stores.AsyncMemoryStores.archive"></a>

#### archive

```python
async def archive(
    memory_store_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryStore
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_stores.py)

POST /memory_stores/{memory_store_id}/archive.

<a id="qca.managed.resources.memory_stores.memory_versions"></a>

# qca.managed.resources.memory\_stores.memory\_versions

<a id="qca.managed.resources.memory_stores.memory_versions.MemoryVersions"></a>

## MemoryVersions

```python
class MemoryVersions(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_versions.py)

<a id="qca.managed.resources.memory_stores.memory_versions.MemoryVersions.retrieve"></a>

#### retrieve

```python
def retrieve(
    memory_version_id: str,
    *,
    memory_store_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_versions.py)

GET /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}.

<a id="qca.managed.resources.memory_stores.memory_versions.MemoryVersions.list"></a>

#### list

```python
def list(
    memory_store_id: str,
    *,
    api_key_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    memory_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    service_account_id: Union[str, None, NotGiven] = NOT_GIVEN,
    session_id: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    operation: Union[Literal["created", "modified", "deleted"], None,
                     NotGiven] = NOT_GIVEN,
    view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[MemoryVersion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_versions.py)

GET /memory_stores/{memory_store_id}/memory_versions.

<a id="qca.managed.resources.memory_stores.memory_versions.MemoryVersions.redact"></a>

#### redact

```python
def redact(
    memory_version_id: str,
    *,
    memory_store_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_versions.py)

POST /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact.

<a id="qca.managed.resources.memory_stores.memory_versions.AsyncMemoryVersions"></a>

## AsyncMemoryVersions

```python
class AsyncMemoryVersions(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_versions.py)

<a id="qca.managed.resources.memory_stores.memory_versions.AsyncMemoryVersions.retrieve"></a>

#### retrieve

```python
async def retrieve(
    memory_version_id: str,
    *,
    memory_store_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_versions.py)

GET /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}.

<a id="qca.managed.resources.memory_stores.memory_versions.AsyncMemoryVersions.list"></a>

#### list

```python
def list(
    memory_store_id: str,
    *,
    api_key_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    memory_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    service_account_id: Union[str, None, NotGiven] = NOT_GIVEN,
    session_id: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    operation: Union[Literal["created", "modified", "deleted"], None,
                     NotGiven] = NOT_GIVEN,
    view: Union[Literal["basic", "full"], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[MemoryVersion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_versions.py)

GET /memory_stores/{memory_store_id}/memory_versions.

<a id="qca.managed.resources.memory_stores.memory_versions.AsyncMemoryVersions.redact"></a>

#### redact

```python
async def redact(
    memory_version_id: str,
    *,
    memory_store_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> MemoryVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/memory_stores/memory_versions.py)

POST /memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact.

<a id="qca.managed.resources.models"></a>

# qca.managed.resources.models

<a id="qca.managed.resources.models.Models"></a>

## Models

```python
class Models(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/models.py)

<a id="qca.managed.resources.models.Models.list"></a>

#### list

```python
def list(
    *,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[ModelInfo]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/models.py)

GET /models.

<a id="qca.managed.resources.models.AsyncModels"></a>

## AsyncModels

```python
class AsyncModels(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/models.py)

<a id="qca.managed.resources.models.AsyncModels.list"></a>

#### list

```python
def list(
    *,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[ModelInfo]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/models.py)

GET /models.

<a id="qca.managed.resources.sessions.events"></a>

# qca.managed.resources.sessions.events

<a id="qca.managed.resources.sessions.events.Events"></a>

## Events

```python
class Events(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/events.py)

<a id="qca.managed.resources.sessions.events.Events.list"></a>

#### list

```python
def list(
    session_id: str,
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[Literal["asc", "desc"], None, NotGiven] = NOT_GIVEN,
    types: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/events.py)

GET /sessions/{session_id}/events.

<a id="qca.managed.resources.sessions.events.Events.send"></a>

#### send

```python
def send(
    session_id: str,
    *,
    events: List[Union[
        UserMessageEventParams,
        UserInterruptEventParams,
        UserToolConfirmationEventParams,
        UserCustomToolResultEventParams,
        UserDefineOutcomeEventParams,
        UserToolResultEventParams,
        SystemMessageEventParams,
    ]],
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SendSessionEvents
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/events.py)

POST /sessions/{session_id}/events.

<a id="qca.managed.resources.sessions.events.Events.stream"></a>

#### stream

```python
def stream(
    session_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None,
                        NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Stream[SessionStreamEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/events.py)

GET /sessions/{session_id}/events/stream.

<a id="qca.managed.resources.sessions.events.Events.resumable_stream"></a>

#### resumable\_stream

```python
def resumable_stream(
    session_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None,
                        NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> ResumableStream[SessionStreamEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/events.py)

Continuously reconnect GET /sessions/{session_id}/events/stream.

<a id="qca.managed.resources.sessions.events.AsyncEvents"></a>

## AsyncEvents

```python
class AsyncEvents(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/events.py)

<a id="qca.managed.resources.sessions.events.AsyncEvents.list"></a>

#### list

```python
def list(
    session_id: str,
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[Literal["asc", "desc"], None, NotGiven] = NOT_GIVEN,
    types: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/events.py)

GET /sessions/{session_id}/events.

<a id="qca.managed.resources.sessions.events.AsyncEvents.send"></a>

#### send

```python
async def send(
    session_id: str,
    *,
    events: List[Union[
        UserMessageEventParams,
        UserInterruptEventParams,
        UserToolConfirmationEventParams,
        UserCustomToolResultEventParams,
        UserDefineOutcomeEventParams,
        UserToolResultEventParams,
        SystemMessageEventParams,
    ]],
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SendSessionEvents
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/events.py)

POST /sessions/{session_id}/events.

<a id="qca.managed.resources.sessions.events.AsyncEvents.stream"></a>

#### stream

```python
async def stream(
    session_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None,
                        NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncStream[SessionStreamEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/events.py)

GET /sessions/{session_id}/events/stream.

<a id="qca.managed.resources.sessions.events.AsyncEvents.resumable_stream"></a>

#### resumable\_stream

```python
def resumable_stream(
    session_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None,
                        NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    last_event_id: Union[str, None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncResumableStream[SessionStreamEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/events.py)

Continuously reconnect GET /sessions/{session_id}/events/stream.

<a id="qca.managed.resources.sessions.resources"></a>

# qca.managed.resources.sessions.resources

<a id="qca.managed.resources.sessions.resources.Resources"></a>

## Resources

```python
class Resources(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

<a id="qca.managed.resources.sessions.resources.Resources.retrieve"></a>

#### retrieve

```python
def retrieve(
    resource_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionResourceGetResponseUnion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

GET /sessions/{session_id}/resources/{resource_id}.

<a id="qca.managed.resources.sessions.resources.Resources.update"></a>

#### update

```python
def update(
    resource_id: str,
    *,
    session_id: str,
    password: Union[str, None, NotGiven] = NOT_GIVEN,
    authorization_token: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionResourceUpdateResponseUnion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

POST /sessions/{session_id}/resources/{resource_id}.

<a id="qca.managed.resources.sessions.resources.Resources.list"></a>

#### list

```python
def list(
    session_id: str,
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[SessionResourceUnion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

GET /sessions/{session_id}/resources.

<a id="qca.managed.resources.sessions.resources.Resources.delete"></a>

#### delete

```python
def delete(
    resource_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeleteSessionResource
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

DELETE /sessions/{session_id}/resources/{resource_id}.

<a id="qca.managed.resources.sessions.resources.Resources.add"></a>

#### add

```python
def add(
    session_id: str,
    *,
    file_id: str,
    type: Literal["file"],
    mount_path: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> FileResource
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

POST /sessions/{session_id}/resources.

<a id="qca.managed.resources.sessions.resources.AsyncResources"></a>

## AsyncResources

```python
class AsyncResources(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

<a id="qca.managed.resources.sessions.resources.AsyncResources.retrieve"></a>

#### retrieve

```python
async def retrieve(
    resource_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionResourceGetResponseUnion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

GET /sessions/{session_id}/resources/{resource_id}.

<a id="qca.managed.resources.sessions.resources.AsyncResources.update"></a>

#### update

```python
async def update(
    resource_id: str,
    *,
    session_id: str,
    password: Union[str, None, NotGiven] = NOT_GIVEN,
    authorization_token: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionResourceUpdateResponseUnion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

POST /sessions/{session_id}/resources/{resource_id}.

<a id="qca.managed.resources.sessions.resources.AsyncResources.list"></a>

#### list

```python
def list(
    session_id: str,
    *,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[SessionResourceUnion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

GET /sessions/{session_id}/resources.

<a id="qca.managed.resources.sessions.resources.AsyncResources.delete"></a>

#### delete

```python
async def delete(
    resource_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeleteSessionResource
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

DELETE /sessions/{session_id}/resources/{resource_id}.

<a id="qca.managed.resources.sessions.resources.AsyncResources.add"></a>

#### add

```python
async def add(
    session_id: str,
    *,
    file_id: str,
    type: Literal["file"],
    mount_path: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> FileResource
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/resources.py)

POST /sessions/{session_id}/resources.

<a id="qca.managed.resources.sessions.sessions"></a>

# qca.managed.resources.sessions.sessions

<a id="qca.managed.resources.sessions.sessions.Sessions"></a>

## Sessions

```python
class Sessions(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

<a id="qca.managed.resources.sessions.sessions.Sessions.events"></a>

#### events

```python
@cached_property
def events() -> Events
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

<a id="qca.managed.resources.sessions.sessions.Sessions.resources"></a>

#### resources

```python
@cached_property
def resources() -> Resources
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

<a id="qca.managed.resources.sessions.sessions.Sessions.threads"></a>

#### threads

```python
@cached_property
def threads() -> Threads
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

<a id="qca.managed.resources.sessions.sessions.Sessions.create"></a>

#### create

```python
def create(
        *,
        agent: Union[str, AgentParams, AgentWithOverridesParams],
        environment_id: str,
        environment_variables: Union[Dict[str, str], None,
                                     NotGiven] = NOT_GIVEN,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        initial_events: Union[List[Union[UserMessageEventParams,
                                         UserDefineOutcomeEventParams]], None,
                              NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        resources: Union[List[Union[GitHubRepositoryResourceParams,
                                    FileResourceParams,
                                    MemoryStoreResourceParam]], None,
                         NotGiven] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

POST /sessions.

<a id="qca.managed.resources.sessions.sessions.Sessions.retrieve"></a>

#### retrieve

```python
def retrieve(
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

GET /sessions/{session_id}.

<a id="qca.managed.resources.sessions.sessions.Sessions.update"></a>

#### update

```python
def update(
        session_id: str,
        *,
        environment_variables: Union[Dict[str, str], None,
                                     NotGiven] = NOT_GIVEN,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        agent: Union[SessionAgentUpdateParam, None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

POST /sessions/{session_id}.

<a id="qca.managed.resources.sessions.sessions.Sessions.list"></a>

#### list

```python
def list(
    *,
    agent_id: Union[str, None, NotGiven] = NOT_GIVEN,
    agent_version: Union[int, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    deployment_id: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    memory_store_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[Literal["asc", "desc"], None, NotGiven] = NOT_GIVEN,
    statuses: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Session]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

GET /sessions.

<a id="qca.managed.resources.sessions.sessions.Sessions.delete"></a>

#### delete

```python
def delete(
    session_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedSession
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

DELETE /sessions/{session_id}.

<a id="qca.managed.resources.sessions.sessions.Sessions.archive"></a>

#### archive

```python
def archive(
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

POST /sessions/{session_id}/archive.

<a id="qca.managed.resources.sessions.sessions.AsyncSessions"></a>

## AsyncSessions

```python
class AsyncSessions(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

<a id="qca.managed.resources.sessions.sessions.AsyncSessions.events"></a>

#### events

```python
@cached_property
def events() -> AsyncEvents
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

<a id="qca.managed.resources.sessions.sessions.AsyncSessions.resources"></a>

#### resources

```python
@cached_property
def resources() -> AsyncResources
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

<a id="qca.managed.resources.sessions.sessions.AsyncSessions.threads"></a>

#### threads

```python
@cached_property
def threads() -> AsyncThreads
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

<a id="qca.managed.resources.sessions.sessions.AsyncSessions.create"></a>

#### create

```python
async def create(
        *,
        agent: Union[str, AgentParams, AgentWithOverridesParams],
        environment_id: str,
        environment_variables: Union[Dict[str, str], None,
                                     NotGiven] = NOT_GIVEN,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        initial_events: Union[List[Union[UserMessageEventParams,
                                         UserDefineOutcomeEventParams]], None,
                              NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        resources: Union[List[Union[GitHubRepositoryResourceParams,
                                    FileResourceParams,
                                    MemoryStoreResourceParam]], None,
                         NotGiven] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

POST /sessions.

<a id="qca.managed.resources.sessions.sessions.AsyncSessions.retrieve"></a>

#### retrieve

```python
async def retrieve(
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

GET /sessions/{session_id}.

<a id="qca.managed.resources.sessions.sessions.AsyncSessions.update"></a>

#### update

```python
async def update(
        session_id: str,
        *,
        environment_variables: Union[Dict[str, str], None,
                                     NotGiven] = NOT_GIVEN,
        title: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
        agent: Union[SessionAgentUpdateParam, None, NotGiven] = NOT_GIVEN,
        budget: Union[BudgetLimitParam, None, NotGiven] = NOT_GIVEN,
        vault_ids: Union[List[str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

POST /sessions/{session_id}.

<a id="qca.managed.resources.sessions.sessions.AsyncSessions.list"></a>

#### list

```python
def list(
    *,
    agent_id: Union[str, None, NotGiven] = NOT_GIVEN,
    agent_version: Union[int, None, NotGiven] = NOT_GIVEN,
    created_at_gt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_gte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lt: Union[datetime, None, NotGiven] = NOT_GIVEN,
    created_at_lte: Union[datetime, None, NotGiven] = NOT_GIVEN,
    deployment_id: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    memory_store_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    order: Union[Literal["asc", "desc"], None, NotGiven] = NOT_GIVEN,
    statuses: Union[List[str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Session]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

GET /sessions.

<a id="qca.managed.resources.sessions.sessions.AsyncSessions.delete"></a>

#### delete

```python
async def delete(
    session_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedSession
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

DELETE /sessions/{session_id}.

<a id="qca.managed.resources.sessions.sessions.AsyncSessions.archive"></a>

#### archive

```python
async def archive(
        session_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Session
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/sessions.py)

POST /sessions/{session_id}/archive.

<a id="qca.managed.resources.sessions.threads.events"></a>

# qca.managed.resources.sessions.threads.events

<a id="qca.managed.resources.sessions.threads.events.Events"></a>

## Events

```python
class Events(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/events.py)

<a id="qca.managed.resources.sessions.threads.events.Events.list"></a>

#### list

```python
def list(
    thread_id: str,
    *,
    session_id: str,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/events.py)

GET /sessions/{session_id}/threads/{thread_id}/events.

<a id="qca.managed.resources.sessions.threads.events.Events.stream"></a>

#### stream

```python
def stream(
    thread_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None,
                        NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Stream[StreamSessionThreadEventsUnion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/events.py)

GET /sessions/{session_id}/threads/{thread_id}/stream.

<a id="qca.managed.resources.sessions.threads.events.AsyncEvents"></a>

## AsyncEvents

```python
class AsyncEvents(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/events.py)

<a id="qca.managed.resources.sessions.threads.events.AsyncEvents.list"></a>

#### list

```python
def list(
    thread_id: str,
    *,
    session_id: str,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[SessionEvent]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/events.py)

GET /sessions/{session_id}/threads/{thread_id}/events.

<a id="qca.managed.resources.sessions.threads.events.AsyncEvents.stream"></a>

#### stream

```python
async def stream(
    thread_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    event_deltas: Union[List[Literal["agent.message", "agent.thinking"]], None,
                        NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncStream[StreamSessionThreadEventsUnion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/events.py)

GET /sessions/{session_id}/threads/{thread_id}/stream.

<a id="qca.managed.resources.sessions.threads.threads"></a>

# qca.managed.resources.sessions.threads.threads

<a id="qca.managed.resources.sessions.threads.threads.Threads"></a>

## Threads

```python
class Threads(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/threads.py)

<a id="qca.managed.resources.sessions.threads.threads.Threads.events"></a>

#### events

```python
@cached_property
def events() -> Events
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/threads.py)

<a id="qca.managed.resources.sessions.threads.threads.Threads.retrieve"></a>

#### retrieve

```python
def retrieve(
    thread_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionThread
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/threads.py)

GET /sessions/{session_id}/threads/{thread_id}.

<a id="qca.managed.resources.sessions.threads.threads.Threads.list"></a>

#### list

```python
def list(
    session_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[SessionThread]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/threads.py)

GET /sessions/{session_id}/threads.

<a id="qca.managed.resources.sessions.threads.threads.Threads.archive"></a>

#### archive

```python
def archive(
    thread_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionThread
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/threads.py)

POST /sessions/{session_id}/threads/{thread_id}/archive.

<a id="qca.managed.resources.sessions.threads.threads.AsyncThreads"></a>

## AsyncThreads

```python
class AsyncThreads(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/threads.py)

<a id="qca.managed.resources.sessions.threads.threads.AsyncThreads.events"></a>

#### events

```python
@cached_property
def events() -> AsyncEvents
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/threads.py)

<a id="qca.managed.resources.sessions.threads.threads.AsyncThreads.retrieve"></a>

#### retrieve

```python
async def retrieve(
    thread_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionThread
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/threads.py)

GET /sessions/{session_id}/threads/{thread_id}.

<a id="qca.managed.resources.sessions.threads.threads.AsyncThreads.list"></a>

#### list

```python
def list(
    session_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[SessionThread]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/threads.py)

GET /sessions/{session_id}/threads.

<a id="qca.managed.resources.sessions.threads.threads.AsyncThreads.archive"></a>

#### archive

```python
async def archive(
    thread_id: str,
    *,
    session_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SessionThread
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/sessions/threads/threads.py)

POST /sessions/{session_id}/threads/{thread_id}/archive.

<a id="qca.managed.resources.skills.skills"></a>

# qca.managed.resources.skills.skills

<a id="qca.managed.resources.skills.skills.Skills"></a>

## Skills

```python
class Skills(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

<a id="qca.managed.resources.skills.skills.Skills.versions"></a>

#### versions

```python
@cached_property
def versions() -> Versions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

<a id="qca.managed.resources.skills.skills.Skills.create"></a>

#### create

```python
def create(
        *,
        files: List[FileTypes],
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        display_title: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Skill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

POST /skills.

<a id="qca.managed.resources.skills.skills.Skills.retrieve"></a>

#### retrieve

```python
def retrieve(
        skill_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Skill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

GET /skills/{skill_id}.

<a id="qca.managed.resources.skills.skills.Skills.list"></a>

#### list

```python
def list(
    *,
    display_name: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    source: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Skill]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

GET /skills.

<a id="qca.managed.resources.skills.skills.Skills.delete"></a>

#### delete

```python
def delete(
    skill_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedSkill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

DELETE /skills/{skill_id}.

<a id="qca.managed.resources.skills.skills.AsyncSkills"></a>

## AsyncSkills

```python
class AsyncSkills(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

<a id="qca.managed.resources.skills.skills.AsyncSkills.versions"></a>

#### versions

```python
@cached_property
def versions() -> AsyncVersions
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

<a id="qca.managed.resources.skills.skills.AsyncSkills.create"></a>

#### create

```python
async def create(
        *,
        files: List[FileTypes],
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        display_title: Union[str, None, NotGiven] = NOT_GIVEN,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Skill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

POST /skills.

<a id="qca.managed.resources.skills.skills.AsyncSkills.retrieve"></a>

#### retrieve

```python
async def retrieve(
        skill_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Skill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

GET /skills/{skill_id}.

<a id="qca.managed.resources.skills.skills.AsyncSkills.list"></a>

#### list

```python
def list(
    *,
    display_name: Union[str, None, NotGiven] = NOT_GIVEN,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    source: Union[str, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Skill]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

GET /skills.

<a id="qca.managed.resources.skills.skills.AsyncSkills.delete"></a>

#### delete

```python
async def delete(
    skill_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedSkill
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/skills.py)

DELETE /skills/{skill_id}.

<a id="qca.managed.resources.skills.versions"></a>

# qca.managed.resources.skills.versions

<a id="qca.managed.resources.skills.versions.Versions"></a>

## Versions

```python
class Versions(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

<a id="qca.managed.resources.skills.versions.Versions.create"></a>

#### create

```python
def create(
    skill_id: str,
    *,
    files: List[FileTypes],
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

POST /skills/{skill_id}/versions.

<a id="qca.managed.resources.skills.versions.Versions.retrieve"></a>

#### retrieve

```python
def retrieve(
    version: str,
    *,
    skill_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

GET /skills/{skill_id}/versions/{version}.

<a id="qca.managed.resources.skills.versions.Versions.list"></a>

#### list

```python
def list(
    skill_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[SkillVersion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

GET /skills/{skill_id}/versions.

<a id="qca.managed.resources.skills.versions.Versions.delete"></a>

#### delete

```python
def delete(
    version: str,
    *,
    skill_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedSkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

DELETE /skills/{skill_id}/versions/{version}.

<a id="qca.managed.resources.skills.versions.Versions.download"></a>

#### download

```python
def download(
    version: str,
    *,
    skill_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> BinaryAPIResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

GET /skills/{skill_id}/versions/{version}/content.

<a id="qca.managed.resources.skills.versions.AsyncVersions"></a>

## AsyncVersions

```python
class AsyncVersions(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

<a id="qca.managed.resources.skills.versions.AsyncVersions.create"></a>

#### create

```python
async def create(
    skill_id: str,
    *,
    files: List[FileTypes],
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

POST /skills/{skill_id}/versions.

<a id="qca.managed.resources.skills.versions.AsyncVersions.retrieve"></a>

#### retrieve

```python
async def retrieve(
    version: str,
    *,
    skill_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

GET /skills/{skill_id}/versions/{version}.

<a id="qca.managed.resources.skills.versions.AsyncVersions.list"></a>

#### list

```python
def list(
    skill_id: str,
    *,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[SkillVersion]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

GET /skills/{skill_id}/versions.

<a id="qca.managed.resources.skills.versions.AsyncVersions.delete"></a>

#### delete

```python
async def delete(
    version: str,
    *,
    skill_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedSkillVersion
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

DELETE /skills/{skill_id}/versions/{version}.

<a id="qca.managed.resources.skills.versions.AsyncVersions.download"></a>

#### download

```python
async def download(
    version: str,
    *,
    skill_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncBinaryAPIResponse
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/skills/versions.py)

GET /skills/{skill_id}/versions/{version}/content.

<a id="qca.managed.resources.vaults.credentials"></a>

# qca.managed.resources.vaults.credentials

<a id="qca.managed.resources.vaults.credentials.Credentials"></a>

## Credentials

```python
class Credentials(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

<a id="qca.managed.resources.vaults.credentials.Credentials.create"></a>

#### create

```python
def create(
    vault_id: str,
    *,
    auth: Union[MCPOAuthCreateParams, StaticBearerCreateParams,
                EnvironmentVariableCreateParams],
    display_name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Credential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

POST /vaults/{vault_id}/credentials.

<a id="qca.managed.resources.vaults.credentials.Credentials.retrieve"></a>

#### retrieve

```python
def retrieve(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Credential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

GET /vaults/{vault_id}/credentials/{credential_id}.

<a id="qca.managed.resources.vaults.credentials.Credentials.update"></a>

#### update

```python
def update(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    auth: Union[Union[MCPOAuthUpdateParams, StaticBearerUpdateParams,
                      EnvironmentVariableUpdateParams], None,
                NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Credential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

POST /vaults/{vault_id}/credentials/{credential_id}. Updates authentication information or metadata.

<a id="qca.managed.resources.vaults.credentials.Credentials.list"></a>

#### list

```python
def list(
    vault_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Credential]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

GET /vaults/{vault_id}/credentials.

<a id="qca.managed.resources.vaults.credentials.Credentials.delete"></a>

#### delete

```python
def delete(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedCredential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

DELETE /vaults/{vault_id}/credentials/{credential_id}.

<a id="qca.managed.resources.vaults.credentials.Credentials.archive"></a>

#### archive

```python
def archive(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Credential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

POST /vaults/{vault_id}/credentials/{credential_id}/archive.

<a id="qca.managed.resources.vaults.credentials.Credentials.mcp_oauth_validate"></a>

#### mcp\_oauth\_validate

```python
def mcp_oauth_validate(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> CredentialValidation
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

POST /vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate.

<a id="qca.managed.resources.vaults.credentials.AsyncCredentials"></a>

## AsyncCredentials

```python
class AsyncCredentials(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

<a id="qca.managed.resources.vaults.credentials.AsyncCredentials.create"></a>

#### create

```python
async def create(
    vault_id: str,
    *,
    auth: Union[MCPOAuthCreateParams, StaticBearerCreateParams,
                EnvironmentVariableCreateParams],
    display_name: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Credential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

POST /vaults/{vault_id}/credentials.

<a id="qca.managed.resources.vaults.credentials.AsyncCredentials.retrieve"></a>

#### retrieve

```python
async def retrieve(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Credential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

GET /vaults/{vault_id}/credentials/{credential_id}.

<a id="qca.managed.resources.vaults.credentials.AsyncCredentials.update"></a>

#### update

```python
async def update(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    metadata: Union[Dict[str, Any], None, NotGiven] = NOT_GIVEN,
    auth: Union[Union[MCPOAuthUpdateParams, StaticBearerUpdateParams,
                      EnvironmentVariableUpdateParams], None,
                NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Credential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

POST /vaults/{vault_id}/credentials/{credential_id}. Updates authentication information or metadata.

<a id="qca.managed.resources.vaults.credentials.AsyncCredentials.list"></a>

#### list

```python
def list(
    vault_id: str,
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Credential]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

GET /vaults/{vault_id}/credentials.

<a id="qca.managed.resources.vaults.credentials.AsyncCredentials.delete"></a>

#### delete

```python
async def delete(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedCredential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

DELETE /vaults/{vault_id}/credentials/{credential_id}.

<a id="qca.managed.resources.vaults.credentials.AsyncCredentials.archive"></a>

#### archive

```python
async def archive(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> Credential
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

POST /vaults/{vault_id}/credentials/{credential_id}/archive.

<a id="qca.managed.resources.vaults.credentials.AsyncCredentials.mcp_oauth_validate"></a>

#### mcp\_oauth\_validate

```python
async def mcp_oauth_validate(
    credential_id: str,
    *,
    vault_id: str,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> CredentialValidation
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/credentials.py)

POST /vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate.

<a id="qca.managed.resources.vaults.vaults"></a>

# qca.managed.resources.vaults.vaults

<a id="qca.managed.resources.vaults.vaults.Vaults"></a>

## Vaults

```python
class Vaults(SyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

<a id="qca.managed.resources.vaults.vaults.Vaults.credentials"></a>

#### credentials

```python
@cached_property
def credentials() -> Credentials
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

<a id="qca.managed.resources.vaults.vaults.Vaults.create"></a>

#### create

```python
def create(
        *,
        display_name: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Vault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

POST /vaults.

<a id="qca.managed.resources.vaults.vaults.Vaults.retrieve"></a>

#### retrieve

```python
def retrieve(
        vault_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Vault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

GET /vaults/{vault_id}.

<a id="qca.managed.resources.vaults.vaults.Vaults.list"></a>

#### list

```python
def list(
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> SyncPage[Vault]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

GET /vaults.

<a id="qca.managed.resources.vaults.vaults.Vaults.delete"></a>

#### delete

```python
def delete(
    vault_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedVault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

DELETE /vaults/{vault_id}.

<a id="qca.managed.resources.vaults.vaults.Vaults.archive"></a>

#### archive

```python
def archive(
        vault_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Vault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

POST /vaults/{vault_id}/archive.

<a id="qca.managed.resources.vaults.vaults.AsyncVaults"></a>

## AsyncVaults

```python
class AsyncVaults(AsyncAPIResource)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

<a id="qca.managed.resources.vaults.vaults.AsyncVaults.credentials"></a>

#### credentials

```python
@cached_property
def credentials() -> AsyncCredentials
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

<a id="qca.managed.resources.vaults.vaults.AsyncVaults.create"></a>

#### create

```python
async def create(
        *,
        display_name: str,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Union[Dict[str, str], None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Vault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

POST /vaults.

<a id="qca.managed.resources.vaults.vaults.AsyncVaults.retrieve"></a>

#### retrieve

```python
async def retrieve(
        vault_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Vault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

GET /vaults/{vault_id}.

<a id="qca.managed.resources.vaults.vaults.AsyncVaults.list"></a>

#### list

```python
def list(
    *,
    name: Union[str, None, NotGiven] = NOT_GIVEN,
    before_id: Union[str, None, NotGiven] = NOT_GIVEN,
    after_id: Union[str, None, NotGiven] = NOT_GIVEN,
    include_archived: Union[bool, None, NotGiven] = NOT_GIVEN,
    limit: Union[int, None, NotGiven] = NOT_GIVEN,
    page: Union[str, None, NotGiven] = NOT_GIVEN,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> AsyncPaginator[Vault]
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

GET /vaults.

<a id="qca.managed.resources.vaults.vaults.AsyncVaults.delete"></a>

#### delete

```python
async def delete(
    vault_id: str,
    *,
    workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
    betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
    extra_headers: Dict[str, str] | None = None,
    extra_query: Dict[str, Any] | None = None,
    extra_body: Dict[str, Any] | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN
) -> DeletedVault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

DELETE /vaults/{vault_id}.

<a id="qca.managed.resources.vaults.vaults.AsyncVaults.archive"></a>

#### archive

```python
async def archive(
        vault_id: str,
        *,
        workspace_id: Union[str, None, NotGiven] = NOT_GIVEN,
        betas: Union[List[str], None, NotGiven] = NOT_GIVEN,
        extra_headers: Dict[str, str] | None = None,
        extra_query: Dict[str, Any] | None = None,
        extra_body: Dict[str, Any] | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN) -> Vault
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/resources/vaults/vaults.py)

POST /vaults/{vault_id}/archive.

<a id="qca.managed.types.actor_union"></a>

# qca.managed.types.actor\_union

<a id="qca.managed.types.actor_union.ActorUnion"></a>

## ActorUnion

```python
class ActorUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/actor_union.py)

<a id="qca.managed.types.actor_union.ActorUnion.session_id"></a>

#### session\_id

<a id="qca.managed.types.actor_union.ActorUnion.type"></a>

#### type

<a id="qca.managed.types.actor_union.ActorUnion.api_key_id"></a>

#### api\_key\_id

<a id="qca.managed.types.actor_union.ActorUnion.user_id"></a>

#### user\_id

<a id="qca.managed.types.actor_union.ActorUnion.service_account_id"></a>

#### service\_account\_id

<a id="qca.managed.types.advisor_params"></a>

# qca.managed.types.advisor\_params

<a id="qca.managed.types.advisor_params.AdvisorParams"></a>

## AdvisorParams

```python
class AdvisorParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/advisor_params.py)

<a id="qca.managed.types.advisor_params.AdvisorParams.model"></a>

#### model

<a id="qca.managed.types.advisor_params.AdvisorParams.type"></a>

#### type

<a id="qca.managed.types.agent"></a>

# qca.managed.types.agent

<a id="qca.managed.types.agent.Agent"></a>

## Agent

```python
class Agent(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent.py)

<a id="qca.managed.types.agent.Agent.id"></a>

#### id

<a id="qca.managed.types.agent.Agent.archived_at"></a>

#### archived\_at

<a id="qca.managed.types.agent.Agent.created_at"></a>

#### created\_at

<a id="qca.managed.types.agent.Agent.description"></a>

#### description

<a id="qca.managed.types.agent.Agent.mcp_servers"></a>

#### mcp\_servers

<a id="qca.managed.types.agent.Agent.metadata"></a>

#### metadata

<a id="qca.managed.types.agent.Agent.model"></a>

#### model

<a id="qca.managed.types.agent.Agent.multiagent"></a>

#### multiagent

<a id="qca.managed.types.agent.Agent.name"></a>

#### name

<a id="qca.managed.types.agent.Agent.skills"></a>

#### skills

<a id="qca.managed.types.agent.Agent.system"></a>

#### system

<a id="qca.managed.types.agent.Agent.tools"></a>

#### tools

<a id="qca.managed.types.agent.Agent.type"></a>

#### type

<a id="qca.managed.types.agent.Agent.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.agent.Agent.version"></a>

#### version

<a id="qca.managed.types.agent_archive_params"></a>

# qca.managed.types.agent\_archive\_params

<a id="qca.managed.types.agent_archive_params.AgentArchiveParams"></a>

## AgentArchiveParams

```python
class AgentArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_archive_params.py)

<a id="qca.managed.types.agent_archive_params.AgentArchiveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.agent_archive_params.AgentArchiveParams.betas"></a>

#### betas

<a id="qca.managed.types.agent_create_params"></a>

# qca.managed.types.agent\_create\_params

<a id="qca.managed.types.agent_create_params.AgentCreateParams"></a>

## AgentCreateParams

```python
class AgentCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_create_params.py)

<a id="qca.managed.types.agent_create_params.AgentCreateParams.model"></a>

#### model

<a id="qca.managed.types.agent_create_params.AgentCreateParams.name"></a>

#### name

<a id="qca.managed.types.agent_create_params.AgentCreateParams.description"></a>

#### description

<a id="qca.managed.types.agent_create_params.AgentCreateParams.system"></a>

#### system

<a id="qca.managed.types.agent_create_params.AgentCreateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.agent_create_params.AgentCreateParams.mcp_servers"></a>

#### mcp\_servers

<a id="qca.managed.types.agent_create_params.AgentCreateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.agent_create_params.AgentCreateParams.multiagent"></a>

#### multiagent

<a id="qca.managed.types.agent_create_params.AgentCreateParams.skills"></a>

#### skills

<a id="qca.managed.types.agent_create_params.AgentCreateParams.tools"></a>

#### tools

<a id="qca.managed.types.agent_create_params.AgentCreateParams.betas"></a>

#### betas

<a id="qca.managed.types.agent_list_params"></a>

# qca.managed.types.agent\_list\_params

<a id="qca.managed.types.agent_list_params.AgentListParams"></a>

## AgentListParams

```python
class AgentListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_list_params.py)

<a id="qca.managed.types.agent_list_params.AgentListParams.created_at_gte"></a>

#### created\_at\_gte

<a id="qca.managed.types.agent_list_params.AgentListParams.created_at_lte"></a>

#### created\_at\_lte

<a id="qca.managed.types.agent_list_params.AgentListParams.include_archived"></a>

#### include\_archived

<a id="qca.managed.types.agent_list_params.AgentListParams.limit"></a>

#### limit

<a id="qca.managed.types.agent_list_params.AgentListParams.page"></a>

#### page

<a id="qca.managed.types.agent_list_params.AgentListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.agent_list_params.AgentListParams.betas"></a>

#### betas

<a id="qca.managed.types.agent_mcp_tool_result_event_content_union"></a>

# qca.managed.types.agent\_mcp\_tool\_result\_event\_content\_union

<a id="qca.managed.types.agent_mcp_tool_result_event_content_union.AgentMCPToolResultEventContentUnion"></a>

## AgentMCPToolResultEventContentUnion

```python
class AgentMCPToolResultEventContentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_mcp_tool_result_event_content_union.py)

<a id="qca.managed.types.agent_mcp_tool_result_event_content_union.AgentMCPToolResultEventContentUnion.text"></a>

#### text

<a id="qca.managed.types.agent_mcp_tool_result_event_content_union.AgentMCPToolResultEventContentUnion.type"></a>

#### type

<a id="qca.managed.types.agent_mcp_tool_result_event_content_union.AgentMCPToolResultEventContentUnion.source"></a>

#### source

<a id="qca.managed.types.agent_mcp_tool_result_event_content_union.AgentMCPToolResultEventContentUnion.context"></a>

#### context

<a id="qca.managed.types.agent_mcp_tool_result_event_content_union.AgentMCPToolResultEventContentUnion.title"></a>

#### title

<a id="qca.managed.types.agent_mcp_tool_result_event_content_union.AgentMCPToolResultEventContentUnion.citations"></a>

#### citations

<a id="qca.managed.types.agent_mcp_tool_result_event_content_union.AgentMCPToolResultEventContentUnion.content"></a>

#### content

<a id="qca.managed.types.agent_message_event_content_union"></a>

# qca.managed.types.agent\_message\_event\_content\_union

<a id="qca.managed.types.agent_message_event_content_union.AgentMessageEventContentUnion"></a>

## AgentMessageEventContentUnion

```python
class AgentMessageEventContentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_message_event_content_union.py)

<a id="qca.managed.types.agent_message_event_content_union.AgentMessageEventContentUnion.text"></a>

#### text

<a id="qca.managed.types.agent_message_event_content_union.AgentMessageEventContentUnion.type"></a>

#### type

<a id="qca.managed.types.agent_params"></a>

# qca.managed.types.agent\_params

<a id="qca.managed.types.agent_params.AgentParams"></a>

## AgentParams

```python
class AgentParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_params.py)

<a id="qca.managed.types.agent_params.AgentParams.id"></a>

#### id

<a id="qca.managed.types.agent_params.AgentParams.type"></a>

#### type

<a id="qca.managed.types.agent_params.AgentParams.version"></a>

#### version

<a id="qca.managed.types.agent_reference"></a>

# qca.managed.types.agent\_reference

<a id="qca.managed.types.agent_reference.AgentReference"></a>

## AgentReference

```python
class AgentReference(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_reference.py)

<a id="qca.managed.types.agent_reference.AgentReference.id"></a>

#### id

<a id="qca.managed.types.agent_reference.AgentReference.type"></a>

#### type

<a id="qca.managed.types.agent_reference.AgentReference.version"></a>

#### version

<a id="qca.managed.types.agent_retrieve_params"></a>

# qca.managed.types.agent\_retrieve\_params

<a id="qca.managed.types.agent_retrieve_params.AgentRetrieveParams"></a>

## AgentRetrieveParams

```python
class AgentRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_retrieve_params.py)

<a id="qca.managed.types.agent_retrieve_params.AgentRetrieveParams.version"></a>

#### version

<a id="qca.managed.types.agent_retrieve_params.AgentRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.agent_retrieve_params.AgentRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.agent_skill_union"></a>

# qca.managed.types.agent\_skill\_union

<a id="qca.managed.types.agent_skill_union.AgentSkillUnion"></a>

## AgentSkillUnion

```python
class AgentSkillUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_skill_union.py)

<a id="qca.managed.types.agent_skill_union.AgentSkillUnion.skill_id"></a>

#### skill\_id

<a id="qca.managed.types.agent_skill_union.AgentSkillUnion.type"></a>

#### type

<a id="qca.managed.types.agent_skill_union.AgentSkillUnion.version"></a>

#### version

<a id="qca.managed.types.agent_thread_message_received_event_content_union"></a>

# qca.managed.types.agent\_thread\_message\_received\_event\_content\_union

<a id="qca.managed.types.agent_thread_message_received_event_content_union.AgentThreadMessageReceivedEventContentUnion"></a>

## AgentThreadMessageReceivedEventContentUnion

```python
class AgentThreadMessageReceivedEventContentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_thread_message_received_event_content_union.py)

<a id="qca.managed.types.agent_thread_message_received_event_content_union.AgentThreadMessageReceivedEventContentUnion.text"></a>

#### text

<a id="qca.managed.types.agent_thread_message_received_event_content_union.AgentThreadMessageReceivedEventContentUnion.type"></a>

#### type

<a id="qca.managed.types.agent_thread_message_received_event_content_union.AgentThreadMessageReceivedEventContentUnion.source"></a>

#### source

<a id="qca.managed.types.agent_thread_message_received_event_content_union.AgentThreadMessageReceivedEventContentUnion.context"></a>

#### context

<a id="qca.managed.types.agent_thread_message_received_event_content_union.AgentThreadMessageReceivedEventContentUnion.title"></a>

#### title

<a id="qca.managed.types.agent_thread_message_received_event_content_union_source"></a>

# qca.managed.types.agent\_thread\_message\_received\_event\_content\_union\_source

<a id="qca.managed.types.agent_thread_message_received_event_content_union_source.AgentThreadMessageReceivedEventContentUnionSource"></a>

## AgentThreadMessageReceivedEventContentUnionSource

```python
class AgentThreadMessageReceivedEventContentUnionSource(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_thread_message_received_event_content_union_source.py)

<a id="qca.managed.types.agent_thread_message_received_event_content_union_source.AgentThreadMessageReceivedEventContentUnionSource.data"></a>

#### data

<a id="qca.managed.types.agent_thread_message_received_event_content_union_source.AgentThreadMessageReceivedEventContentUnionSource.media_type"></a>

#### media\_type

<a id="qca.managed.types.agent_thread_message_received_event_content_union_source.AgentThreadMessageReceivedEventContentUnionSource.type"></a>

#### type

<a id="qca.managed.types.agent_thread_message_received_event_content_union_source.AgentThreadMessageReceivedEventContentUnionSource.url"></a>

#### url

<a id="qca.managed.types.agent_thread_message_received_event_content_union_source.AgentThreadMessageReceivedEventContentUnionSource.file_id"></a>

#### file\_id

<a id="qca.managed.types.agent_thread_message_sent_event_content_union"></a>

# qca.managed.types.agent\_thread\_message\_sent\_event\_content\_union

<a id="qca.managed.types.agent_thread_message_sent_event_content_union.AgentThreadMessageSentEventContentUnion"></a>

## AgentThreadMessageSentEventContentUnion

```python
class AgentThreadMessageSentEventContentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_thread_message_sent_event_content_union.py)

<a id="qca.managed.types.agent_thread_message_sent_event_content_union.AgentThreadMessageSentEventContentUnion.text"></a>

#### text

<a id="qca.managed.types.agent_thread_message_sent_event_content_union.AgentThreadMessageSentEventContentUnion.type"></a>

#### type

<a id="qca.managed.types.agent_thread_message_sent_event_content_union.AgentThreadMessageSentEventContentUnion.source"></a>

#### source

<a id="qca.managed.types.agent_thread_message_sent_event_content_union.AgentThreadMessageSentEventContentUnion.context"></a>

#### context

<a id="qca.managed.types.agent_thread_message_sent_event_content_union.AgentThreadMessageSentEventContentUnion.title"></a>

#### title

<a id="qca.managed.types.agent_thread_message_sent_event_content_union_source"></a>

# qca.managed.types.agent\_thread\_message\_sent\_event\_content\_union\_source

<a id="qca.managed.types.agent_thread_message_sent_event_content_union_source.AgentThreadMessageSentEventContentUnionSource"></a>

## AgentThreadMessageSentEventContentUnionSource

```python
class AgentThreadMessageSentEventContentUnionSource(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_thread_message_sent_event_content_union_source.py)

<a id="qca.managed.types.agent_thread_message_sent_event_content_union_source.AgentThreadMessageSentEventContentUnionSource.data"></a>

#### data

<a id="qca.managed.types.agent_thread_message_sent_event_content_union_source.AgentThreadMessageSentEventContentUnionSource.media_type"></a>

#### media\_type

<a id="qca.managed.types.agent_thread_message_sent_event_content_union_source.AgentThreadMessageSentEventContentUnionSource.type"></a>

#### type

<a id="qca.managed.types.agent_thread_message_sent_event_content_union_source.AgentThreadMessageSentEventContentUnionSource.url"></a>

#### url

<a id="qca.managed.types.agent_thread_message_sent_event_content_union_source.AgentThreadMessageSentEventContentUnionSource.file_id"></a>

#### file\_id

<a id="qca.managed.types.agent_tool_config_union"></a>

# qca.managed.types.agent\_tool\_config\_union

<a id="qca.managed.types.agent_tool_config_union.AgentToolConfigUnion"></a>

## AgentToolConfigUnion

```python
class AgentToolConfigUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_tool_config_union.py)

<a id="qca.managed.types.agent_tool_config_union.AgentToolConfigUnion.enabled"></a>

#### enabled

<a id="qca.managed.types.agent_tool_config_union.AgentToolConfigUnion.name"></a>

#### name

<a id="qca.managed.types.agent_tool_config_union.AgentToolConfigUnion.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.agent_tool_config_union.AgentToolConfigUnion.type"></a>

#### type

<a id="qca.managed.types.agent_tool_config_union.AgentToolConfigUnion.allowed_domains"></a>

#### allowed\_domains

<a id="qca.managed.types.agent_tool_config_union.AgentToolConfigUnion.blocked_domains"></a>

#### blocked\_domains

<a id="qca.managed.types.agent_tool_config_union.AgentToolConfigUnion.max_content_tokens"></a>

#### max\_content\_tokens

<a id="qca.managed.types.agent_tool_config_union.AgentToolConfigUnion.user_location"></a>

#### user\_location

<a id="qca.managed.types.agent_tool_config_union_permission_policy"></a>

# qca.managed.types.agent\_tool\_config\_union\_permission\_policy

<a id="qca.managed.types.agent_tool_config_union_permission_policy.AgentToolConfigUnionPermissionPolicy"></a>

## AgentToolConfigUnionPermissionPolicy

```python
class AgentToolConfigUnionPermissionPolicy(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_tool_config_union_permission_policy.py)

<a id="qca.managed.types.agent_tool_config_union_permission_policy.AgentToolConfigUnionPermissionPolicy.type"></a>

#### type

<a id="qca.managed.types.agent_tool_result_event_content_union"></a>

# qca.managed.types.agent\_tool\_result\_event\_content\_union

<a id="qca.managed.types.agent_tool_result_event_content_union.AgentToolResultEventContentUnion"></a>

## AgentToolResultEventContentUnion

```python
class AgentToolResultEventContentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_tool_result_event_content_union.py)

<a id="qca.managed.types.agent_tool_result_event_content_union.AgentToolResultEventContentUnion.text"></a>

#### text

<a id="qca.managed.types.agent_tool_result_event_content_union.AgentToolResultEventContentUnion.type"></a>

#### type

<a id="qca.managed.types.agent_tool_result_event_content_union.AgentToolResultEventContentUnion.source"></a>

#### source

<a id="qca.managed.types.agent_tool_result_event_content_union.AgentToolResultEventContentUnion.context"></a>

#### context

<a id="qca.managed.types.agent_tool_result_event_content_union.AgentToolResultEventContentUnion.title"></a>

#### title

<a id="qca.managed.types.agent_tool_result_event_content_union.AgentToolResultEventContentUnion.citations"></a>

#### citations

<a id="qca.managed.types.agent_tool_result_event_content_union.AgentToolResultEventContentUnion.content"></a>

#### content

<a id="qca.managed.types.agent_tool_union"></a>

# qca.managed.types.agent\_tool\_union

<a id="qca.managed.types.agent_tool_union.AgentToolUnion"></a>

## AgentToolUnion

```python
class AgentToolUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_tool_union.py)

<a id="qca.managed.types.agent_tool_union.AgentToolUnion.enabled_tools"></a>

#### enabled\_tools

<a id="qca.managed.types.agent_tool_union.AgentToolUnion.disallowed_tools"></a>

#### disallowed\_tools

<a id="qca.managed.types.agent_tool_union.AgentToolUnion.configs"></a>

#### configs

<a id="qca.managed.types.agent_tool_union.AgentToolUnion.default_config"></a>

#### default\_config

<a id="qca.managed.types.agent_tool_union.AgentToolUnion.type"></a>

#### type

<a id="qca.managed.types.agent_tool_union.AgentToolUnion.mcp_server_name"></a>

#### mcp\_server\_name

<a id="qca.managed.types.agent_tool_union.AgentToolUnion.description"></a>

#### description

<a id="qca.managed.types.agent_tool_union.AgentToolUnion.input_schema"></a>

#### input\_schema

<a id="qca.managed.types.agent_tool_union.AgentToolUnion.name"></a>

#### name

<a id="qca.managed.types.agent_tool_union_default_config"></a>

# qca.managed.types.agent\_tool\_union\_default\_config

<a id="qca.managed.types.agent_tool_union_default_config.AgentToolUnionDefaultConfig"></a>

## AgentToolUnionDefaultConfig

```python
class AgentToolUnionDefaultConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_tool_union_default_config.py)

<a id="qca.managed.types.agent_tool_union_default_config.AgentToolUnionDefaultConfig.enabled"></a>

#### enabled

<a id="qca.managed.types.agent_tool_union_default_config.AgentToolUnionDefaultConfig.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.agent_tool_union_default_config_permission_policy"></a>

# qca.managed.types.agent\_tool\_union\_default\_config\_permission\_policy

<a id="qca.managed.types.agent_tool_union_default_config_permission_policy.AgentToolUnionDefaultConfigPermissionPolicy"></a>

## AgentToolUnionDefaultConfigPermissionPolicy

```python
class AgentToolUnionDefaultConfigPermissionPolicy(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_tool_union_default_config_permission_policy.py)

<a id="qca.managed.types.agent_tool_union_default_config_permission_policy.AgentToolUnionDefaultConfigPermissionPolicy.type"></a>

#### type

<a id="qca.managed.types.agent_toolset20260401_params"></a>

# qca.managed.types.agent\_toolset20260401\_params

<a id="qca.managed.types.agent_toolset20260401_params.AgentToolset20260401Params"></a>

## AgentToolset20260401Params

```python
class AgentToolset20260401Params(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_toolset20260401_params.py)

<a id="qca.managed.types.agent_toolset20260401_params.AgentToolset20260401Params.disallowed_tools"></a>

#### disallowed\_tools

<a id="qca.managed.types.agent_toolset20260401_params.AgentToolset20260401Params.enabled_tools"></a>

#### enabled\_tools

<a id="qca.managed.types.agent_toolset20260401_params.AgentToolset20260401Params.type"></a>

#### type

<a id="qca.managed.types.agent_toolset20260401_params.AgentToolset20260401Params.configs"></a>

#### configs

<a id="qca.managed.types.agent_toolset20260401_params.AgentToolset20260401Params.default_config"></a>

#### default\_config

<a id="qca.managed.types.agent_toolset_default_config_params"></a>

# qca.managed.types.agent\_toolset\_default\_config\_params

<a id="qca.managed.types.agent_toolset_default_config_params.AgentToolsetDefaultConfigParams"></a>

## AgentToolsetDefaultConfigParams

```python
class AgentToolsetDefaultConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_toolset_default_config_params.py)

<a id="qca.managed.types.agent_toolset_default_config_params.AgentToolsetDefaultConfigParams.enabled"></a>

#### enabled

<a id="qca.managed.types.agent_toolset_default_config_params.AgentToolsetDefaultConfigParams.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.agent_update_params"></a>

# qca.managed.types.agent\_update\_params

<a id="qca.managed.types.agent_update_params.AgentUpdateParams"></a>

## AgentUpdateParams

```python
class AgentUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_update_params.py)

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.description"></a>

#### description

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.system"></a>

#### system

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.name"></a>

#### name

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.version"></a>

#### version

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.mcp_servers"></a>

#### mcp\_servers

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.skills"></a>

#### skills

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.tools"></a>

#### tools

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.model"></a>

#### model

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.multiagent"></a>

#### multiagent

<a id="qca.managed.types.agent_update_params.AgentUpdateParams.betas"></a>

#### betas

<a id="qca.managed.types.agent_version_list_params"></a>

# qca.managed.types.agent\_version\_list\_params

<a id="qca.managed.types.agent_version_list_params.AgentVersionListParams"></a>

## AgentVersionListParams

```python
class AgentVersionListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_version_list_params.py)

<a id="qca.managed.types.agent_version_list_params.AgentVersionListParams.limit"></a>

#### limit

<a id="qca.managed.types.agent_version_list_params.AgentVersionListParams.page"></a>

#### page

<a id="qca.managed.types.agent_version_list_params.AgentVersionListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.agent_version_list_params.AgentVersionListParams.betas"></a>

#### betas

<a id="qca.managed.types.agent_with_overrides_params"></a>

# qca.managed.types.agent\_with\_overrides\_params

<a id="qca.managed.types.agent_with_overrides_params.AgentWithOverridesParams"></a>

## AgentWithOverridesParams

```python
class AgentWithOverridesParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/agent_with_overrides_params.py)

<a id="qca.managed.types.agent_with_overrides_params.AgentWithOverridesParams.id"></a>

#### id

<a id="qca.managed.types.agent_with_overrides_params.AgentWithOverridesParams.type"></a>

#### type

<a id="qca.managed.types.agent_with_overrides_params.AgentWithOverridesParams.system"></a>

#### system

<a id="qca.managed.types.agent_with_overrides_params.AgentWithOverridesParams.version"></a>

#### version

<a id="qca.managed.types.agent_with_overrides_params.AgentWithOverridesParams.mcp_servers"></a>

#### mcp\_servers

<a id="qca.managed.types.agent_with_overrides_params.AgentWithOverridesParams.model"></a>

#### model

<a id="qca.managed.types.agent_with_overrides_params.AgentWithOverridesParams.skills"></a>

#### skills

<a id="qca.managed.types.agent_with_overrides_params.AgentWithOverridesParams.tools"></a>

#### tools

<a id="qca.managed.types.always_allow_policy_param"></a>

# qca.managed.types.always\_allow\_policy\_param

<a id="qca.managed.types.always_allow_policy_param.AlwaysAllowPolicyParam"></a>

## AlwaysAllowPolicyParam

```python
class AlwaysAllowPolicyParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/always_allow_policy_param.py)

<a id="qca.managed.types.always_allow_policy_param.AlwaysAllowPolicyParam.type"></a>

#### type

<a id="qca.managed.types.always_ask_policy_param"></a>

# qca.managed.types.always\_ask\_policy\_param

<a id="qca.managed.types.always_ask_policy_param.AlwaysAskPolicyParam"></a>

## AlwaysAskPolicyParam

```python
class AlwaysAskPolicyParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/always_ask_policy_param.py)

<a id="qca.managed.types.always_ask_policy_param.AlwaysAskPolicyParam.type"></a>

#### type

<a id="qca.managed.types.base64_document_source_param"></a>

# qca.managed.types.base64\_document\_source\_param

<a id="qca.managed.types.base64_document_source_param.Base64DocumentSourceParam"></a>

## Base64DocumentSourceParam

```python
class Base64DocumentSourceParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/base64_document_source_param.py)

<a id="qca.managed.types.base64_document_source_param.Base64DocumentSourceParam.data"></a>

#### data

<a id="qca.managed.types.base64_document_source_param.Base64DocumentSourceParam.media_type"></a>

#### media\_type

<a id="qca.managed.types.base64_document_source_param.Base64DocumentSourceParam.type"></a>

#### type

<a id="qca.managed.types.base64_image_source_param"></a>

# qca.managed.types.base64\_image\_source\_param

<a id="qca.managed.types.base64_image_source_param.Base64ImageSourceParam"></a>

## Base64ImageSourceParam

```python
class Base64ImageSourceParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/base64_image_source_param.py)

<a id="qca.managed.types.base64_image_source_param.Base64ImageSourceParam.data"></a>

#### data

<a id="qca.managed.types.base64_image_source_param.Base64ImageSourceParam.media_type"></a>

#### media\_type

<a id="qca.managed.types.base64_image_source_param.Base64ImageSourceParam.type"></a>

#### type

<a id="qca.managed.types.bash_tool_config_params"></a>

# qca.managed.types.bash\_tool\_config\_params

<a id="qca.managed.types.bash_tool_config_params.BashToolConfigParams"></a>

## BashToolConfigParams

```python
class BashToolConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/bash_tool_config_params.py)

<a id="qca.managed.types.bash_tool_config_params.BashToolConfigParams.enabled"></a>

#### enabled

<a id="qca.managed.types.bash_tool_config_params.BashToolConfigParams.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.bash_tool_config_params.BashToolConfigParams.type"></a>

#### type

<a id="qca.managed.types.bash_tool_config_params.BashToolConfigParams.name"></a>

#### name

<a id="qca.managed.types.branch_checkout_param"></a>

# qca.managed.types.branch\_checkout\_param

<a id="qca.managed.types.branch_checkout_param.BranchCheckoutParam"></a>

## BranchCheckoutParam

```python
class BranchCheckoutParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/branch_checkout_param.py)

<a id="qca.managed.types.branch_checkout_param.BranchCheckoutParam.name"></a>

#### name

<a id="qca.managed.types.branch_checkout_param.BranchCheckoutParam.type"></a>

#### type

<a id="qca.managed.types.budget_limit"></a>

# qca.managed.types.budget\_limit

<a id="qca.managed.types.budget_limit.BudgetLimit"></a>

## BudgetLimit

```python
class BudgetLimit(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/budget_limit.py)

<a id="qca.managed.types.budget_limit.BudgetLimit.max_list_cost"></a>

#### max\_list\_cost

<a id="qca.managed.types.budget_limit.BudgetLimit.type"></a>

#### type

<a id="qca.managed.types.budget_limit_param"></a>

# qca.managed.types.budget\_limit\_param

<a id="qca.managed.types.budget_limit_param.BudgetLimitParam"></a>

## BudgetLimitParam

```python
class BudgetLimitParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/budget_limit_param.py)

<a id="qca.managed.types.budget_limit_param.BudgetLimitParam.max_list_cost"></a>

#### max\_list\_cost

<a id="qca.managed.types.budget_limit_param.BudgetLimitParam.type"></a>

#### type

<a id="qca.managed.types.cache_creation_usage"></a>

# qca.managed.types.cache\_creation\_usage

<a id="qca.managed.types.cache_creation_usage.CacheCreationUsage"></a>

## CacheCreationUsage

```python
class CacheCreationUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/cache_creation_usage.py)

<a id="qca.managed.types.cache_creation_usage.CacheCreationUsage.ephemeral_1h_input_tokens"></a>

#### ephemeral\_1h\_input\_tokens

<a id="qca.managed.types.cache_creation_usage.CacheCreationUsage.ephemeral_5m_input_tokens"></a>

#### ephemeral\_5m\_input\_tokens

<a id="qca.managed.types.capability_support"></a>

# qca.managed.types.capability\_support

<a id="qca.managed.types.capability_support.CapabilitySupport"></a>

## CapabilitySupport

```python
class CapabilitySupport(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/capability_support.py)

<a id="qca.managed.types.capability_support.CapabilitySupport.supported"></a>

#### supported

<a id="qca.managed.types.cloud_config_networking_union"></a>

# qca.managed.types.cloud\_config\_networking\_union

<a id="qca.managed.types.cloud_config_networking_union.CloudConfigNetworkingUnion"></a>

## CloudConfigNetworkingUnion

```python
class CloudConfigNetworkingUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/cloud_config_networking_union.py)

<a id="qca.managed.types.cloud_config_networking_union.CloudConfigNetworkingUnion.type"></a>

#### type

<a id="qca.managed.types.cloud_config_networking_union.CloudConfigNetworkingUnion.allow_mcp_servers"></a>

#### allow\_mcp\_servers

<a id="qca.managed.types.cloud_config_networking_union.CloudConfigNetworkingUnion.allow_package_managers"></a>

#### allow\_package\_managers

<a id="qca.managed.types.cloud_config_networking_union.CloudConfigNetworkingUnion.allowed_hosts"></a>

#### allowed\_hosts

<a id="qca.managed.types.cloud_config_params"></a>

# qca.managed.types.cloud\_config\_params

<a id="qca.managed.types.cloud_config_params.CloudConfigParams"></a>

## CloudConfigParams

```python
class CloudConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/cloud_config_params.py)

<a id="qca.managed.types.cloud_config_params.CloudConfigParams.setup_script"></a>

#### setup\_script

<a id="qca.managed.types.cloud_config_params.CloudConfigParams.networking"></a>

#### networking

<a id="qca.managed.types.cloud_config_params.CloudConfigParams.packages"></a>

#### packages

<a id="qca.managed.types.cloud_config_params.CloudConfigParams.type"></a>

#### type

<a id="qca.managed.types.commit_checkout_param"></a>

# qca.managed.types.commit\_checkout\_param

<a id="qca.managed.types.commit_checkout_param.CommitCheckoutParam"></a>

## CommitCheckoutParam

```python
class CommitCheckoutParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/commit_checkout_param.py)

<a id="qca.managed.types.commit_checkout_param.CommitCheckoutParam.sha"></a>

#### sha

<a id="qca.managed.types.commit_checkout_param.CommitCheckoutParam.type"></a>

#### type

<a id="qca.managed.types.context_management_capability"></a>

# qca.managed.types.context\_management\_capability

<a id="qca.managed.types.context_management_capability.ContextManagementCapability"></a>

## ContextManagementCapability

```python
class ContextManagementCapability(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/context_management_capability.py)

<a id="qca.managed.types.context_management_capability.ContextManagementCapability.clear_thinking_20251015"></a>

#### clear\_thinking\_20251015

<a id="qca.managed.types.context_management_capability.ContextManagementCapability.clear_tool_uses_20250919"></a>

#### clear\_tool\_uses\_20250919

<a id="qca.managed.types.context_management_capability.ContextManagementCapability.compact_20260112"></a>

#### compact\_20260112

<a id="qca.managed.types.context_management_capability.ContextManagementCapability.supported"></a>

#### supported

<a id="qca.managed.types.credential"></a>

# qca.managed.types.credential

<a id="qca.managed.types.credential.Credential"></a>

## Credential

```python
class Credential(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/credential.py)

<a id="qca.managed.types.credential.Credential.id"></a>

#### id

<a id="qca.managed.types.credential.Credential.archived_at"></a>

#### archived\_at

<a id="qca.managed.types.credential.Credential.auth"></a>

#### auth

<a id="qca.managed.types.credential.Credential.created_at"></a>

#### created\_at

<a id="qca.managed.types.credential.Credential.metadata"></a>

#### metadata

<a id="qca.managed.types.credential.Credential.type"></a>

#### type

<a id="qca.managed.types.credential.Credential.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.credential.Credential.vault_id"></a>

#### vault\_id

<a id="qca.managed.types.credential.Credential.display_name"></a>

#### display\_name

<a id="qca.managed.types.credential_auth_union"></a>

# qca.managed.types.credential\_auth\_union

<a id="qca.managed.types.credential_auth_union.CredentialAuthUnion"></a>

## CredentialAuthUnion

```python
class CredentialAuthUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/credential_auth_union.py)

<a id="qca.managed.types.credential_auth_union.CredentialAuthUnion.mcp_server_url"></a>

#### mcp\_server\_url

<a id="qca.managed.types.credential_auth_union.CredentialAuthUnion.type"></a>

#### type

<a id="qca.managed.types.credential_auth_union.CredentialAuthUnion.expires_at"></a>

#### expires\_at

<a id="qca.managed.types.credential_auth_union.CredentialAuthUnion.refresh"></a>

#### refresh

<a id="qca.managed.types.credential_auth_union.CredentialAuthUnion.injection_location"></a>

#### injection\_location

<a id="qca.managed.types.credential_auth_union.CredentialAuthUnion.networking"></a>

#### networking

<a id="qca.managed.types.credential_auth_union.CredentialAuthUnion.secret_name"></a>

#### secret\_name

<a id="qca.managed.types.credential_validation"></a>

# qca.managed.types.credential\_validation

<a id="qca.managed.types.credential_validation.CredentialValidation"></a>

## CredentialValidation

```python
class CredentialValidation(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/credential_validation.py)

<a id="qca.managed.types.credential_validation.CredentialValidation.credential_id"></a>

#### credential\_id

<a id="qca.managed.types.credential_validation.CredentialValidation.has_refresh_token"></a>

#### has\_refresh\_token

<a id="qca.managed.types.credential_validation.CredentialValidation.mcp_probe"></a>

#### mcp\_probe

<a id="qca.managed.types.credential_validation.CredentialValidation.refresh"></a>

#### refresh

<a id="qca.managed.types.credential_validation.CredentialValidation.status"></a>

#### status

<a id="qca.managed.types.credential_validation.CredentialValidation.type"></a>

#### type

<a id="qca.managed.types.credential_validation.CredentialValidation.validated_at"></a>

#### validated\_at

<a id="qca.managed.types.credential_validation.CredentialValidation.vault_id"></a>

#### vault\_id

<a id="qca.managed.types.custom_skill_params"></a>

# qca.managed.types.custom\_skill\_params

<a id="qca.managed.types.custom_skill_params.CustomSkillParams"></a>

## CustomSkillParams

```python
class CustomSkillParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/custom_skill_params.py)

<a id="qca.managed.types.custom_skill_params.CustomSkillParams.skill_id"></a>

#### skill\_id

<a id="qca.managed.types.custom_skill_params.CustomSkillParams.type"></a>

#### type

<a id="qca.managed.types.custom_skill_params.CustomSkillParams.version"></a>

#### version

<a id="qca.managed.types.custom_tool_input_schema"></a>

# qca.managed.types.custom\_tool\_input\_schema

<a id="qca.managed.types.custom_tool_input_schema.CustomToolInputSchema"></a>

## CustomToolInputSchema

```python
class CustomToolInputSchema(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/custom_tool_input_schema.py)

<a id="qca.managed.types.custom_tool_input_schema.CustomToolInputSchema.type"></a>

#### type

<a id="qca.managed.types.custom_tool_input_schema.CustomToolInputSchema.properties"></a>

#### properties

<a id="qca.managed.types.custom_tool_input_schema.CustomToolInputSchema.required"></a>

#### required

<a id="qca.managed.types.custom_tool_input_schema_param"></a>

# qca.managed.types.custom\_tool\_input\_schema\_param

<a id="qca.managed.types.custom_tool_input_schema_param.CustomToolInputSchemaParam"></a>

## CustomToolInputSchemaParam

```python
class CustomToolInputSchemaParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/custom_tool_input_schema_param.py)

<a id="qca.managed.types.custom_tool_input_schema_param.CustomToolInputSchemaParam.properties"></a>

#### properties

<a id="qca.managed.types.custom_tool_input_schema_param.CustomToolInputSchemaParam.required"></a>

#### required

<a id="qca.managed.types.custom_tool_input_schema_param.CustomToolInputSchemaParam.type"></a>

#### type

<a id="qca.managed.types.custom_tool_params"></a>

# qca.managed.types.custom\_tool\_params

<a id="qca.managed.types.custom_tool_params.CustomToolParams"></a>

## CustomToolParams

```python
class CustomToolParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/custom_tool_params.py)

<a id="qca.managed.types.custom_tool_params.CustomToolParams.description"></a>

#### description

<a id="qca.managed.types.custom_tool_params.CustomToolParams.input_schema"></a>

#### input\_schema

<a id="qca.managed.types.custom_tool_params.CustomToolParams.name"></a>

#### name

<a id="qca.managed.types.custom_tool_params.CustomToolParams.type"></a>

#### type

<a id="qca.managed.types.delete_session_resource"></a>

# qca.managed.types.delete\_session\_resource

<a id="qca.managed.types.delete_session_resource.DeleteSessionResource"></a>

## DeleteSessionResource

```python
class DeleteSessionResource(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/delete_session_resource.py)

<a id="qca.managed.types.delete_session_resource.DeleteSessionResource.id"></a>

#### id

<a id="qca.managed.types.delete_session_resource.DeleteSessionResource.type"></a>

#### type

<a id="qca.managed.types.deleted_credential"></a>

# qca.managed.types.deleted\_credential

<a id="qca.managed.types.deleted_credential.DeletedCredential"></a>

## DeletedCredential

```python
class DeletedCredential(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deleted_credential.py)

<a id="qca.managed.types.deleted_credential.DeletedCredential.id"></a>

#### id

<a id="qca.managed.types.deleted_credential.DeletedCredential.type"></a>

#### type

<a id="qca.managed.types.deleted_file"></a>

# qca.managed.types.deleted\_file

<a id="qca.managed.types.deleted_file.DeletedFile"></a>

## DeletedFile

```python
class DeletedFile(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deleted_file.py)

<a id="qca.managed.types.deleted_file.DeletedFile.id"></a>

#### id

<a id="qca.managed.types.deleted_file.DeletedFile.type"></a>

#### type

<a id="qca.managed.types.deleted_memory"></a>

# qca.managed.types.deleted\_memory

<a id="qca.managed.types.deleted_memory.DeletedMemory"></a>

## DeletedMemory

```python
class DeletedMemory(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deleted_memory.py)

<a id="qca.managed.types.deleted_memory.DeletedMemory.id"></a>

#### id

<a id="qca.managed.types.deleted_memory.DeletedMemory.type"></a>

#### type

<a id="qca.managed.types.deleted_memory_store"></a>

# qca.managed.types.deleted\_memory\_store

<a id="qca.managed.types.deleted_memory_store.DeletedMemoryStore"></a>

## DeletedMemoryStore

```python
class DeletedMemoryStore(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deleted_memory_store.py)

<a id="qca.managed.types.deleted_memory_store.DeletedMemoryStore.id"></a>

#### id

<a id="qca.managed.types.deleted_memory_store.DeletedMemoryStore.type"></a>

#### type

<a id="qca.managed.types.deleted_session"></a>

# qca.managed.types.deleted\_session

<a id="qca.managed.types.deleted_session.DeletedSession"></a>

## DeletedSession

```python
class DeletedSession(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deleted_session.py)

<a id="qca.managed.types.deleted_session.DeletedSession.id"></a>

#### id

<a id="qca.managed.types.deleted_session.DeletedSession.type"></a>

#### type

<a id="qca.managed.types.deleted_skill"></a>

# qca.managed.types.deleted\_skill

<a id="qca.managed.types.deleted_skill.DeletedSkill"></a>

## DeletedSkill

```python
class DeletedSkill(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deleted_skill.py)

<a id="qca.managed.types.deleted_skill.DeletedSkill.id"></a>

#### id

<a id="qca.managed.types.deleted_skill.DeletedSkill.type"></a>

#### type

<a id="qca.managed.types.deleted_skill_version"></a>

# qca.managed.types.deleted\_skill\_version

<a id="qca.managed.types.deleted_skill_version.DeletedSkillVersion"></a>

## DeletedSkillVersion

```python
class DeletedSkillVersion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deleted_skill_version.py)

<a id="qca.managed.types.deleted_skill_version.DeletedSkillVersion.id"></a>

#### id

<a id="qca.managed.types.deleted_skill_version.DeletedSkillVersion.type"></a>

#### type

<a id="qca.managed.types.deleted_vault"></a>

# qca.managed.types.deleted\_vault

<a id="qca.managed.types.deleted_vault.DeletedVault"></a>

## DeletedVault

```python
class DeletedVault(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deleted_vault.py)

<a id="qca.managed.types.deleted_vault.DeletedVault.id"></a>

#### id

<a id="qca.managed.types.deleted_vault.DeletedVault.type"></a>

#### type

<a id="qca.managed.types.delta_content"></a>

# qca.managed.types.delta\_content

<a id="qca.managed.types.delta_content.DeltaContent"></a>

## DeltaContent

```python
class DeltaContent(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/delta_content.py)

<a id="qca.managed.types.delta_content.DeltaContent.content"></a>

#### content

<a id="qca.managed.types.delta_content.DeltaContent.type"></a>

#### type

<a id="qca.managed.types.delta_content.DeltaContent.index"></a>

#### index

<a id="qca.managed.types.deployment"></a>

# qca.managed.types.deployment

<a id="qca.managed.types.deployment.Deployment"></a>

## Deployment

```python
class Deployment(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment.py)

<a id="qca.managed.types.deployment.Deployment.environment_variables"></a>

#### environment\_variables

<a id="qca.managed.types.deployment.Deployment.id"></a>

#### id

<a id="qca.managed.types.deployment.Deployment.agent"></a>

#### agent

<a id="qca.managed.types.deployment.Deployment.archived_at"></a>

#### archived\_at

<a id="qca.managed.types.deployment.Deployment.created_at"></a>

#### created\_at

<a id="qca.managed.types.deployment.Deployment.description"></a>

#### description

<a id="qca.managed.types.deployment.Deployment.environment_id"></a>

#### environment\_id

<a id="qca.managed.types.deployment.Deployment.initial_events"></a>

#### initial\_events

<a id="qca.managed.types.deployment.Deployment.metadata"></a>

#### metadata

<a id="qca.managed.types.deployment.Deployment.name"></a>

#### name

<a id="qca.managed.types.deployment.Deployment.paused_reason"></a>

#### paused\_reason

<a id="qca.managed.types.deployment.Deployment.resources"></a>

#### resources

<a id="qca.managed.types.deployment.Deployment.schedule"></a>

#### schedule

<a id="qca.managed.types.deployment.Deployment.status"></a>

#### status

<a id="qca.managed.types.deployment.Deployment.type"></a>

#### type

<a id="qca.managed.types.deployment.Deployment.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.deployment.Deployment.vault_ids"></a>

#### vault\_ids

<a id="qca.managed.types.deployment.Deployment.budget"></a>

#### budget

<a id="qca.managed.types.deployment_archive_params"></a>

# qca.managed.types.deployment\_archive\_params

<a id="qca.managed.types.deployment_archive_params.DeploymentArchiveParams"></a>

## DeploymentArchiveParams

```python
class DeploymentArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_archive_params.py)

<a id="qca.managed.types.deployment_archive_params.DeploymentArchiveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.deployment_archive_params.DeploymentArchiveParams.betas"></a>

#### betas

<a id="qca.managed.types.deployment_create_params"></a>

# qca.managed.types.deployment\_create\_params

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams"></a>

## DeploymentCreateParams

```python
class DeploymentCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_create_params.py)

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.environment_variables"></a>

#### environment\_variables

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.agent"></a>

#### agent

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.environment_id"></a>

#### environment\_id

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.initial_events"></a>

#### initial\_events

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.name"></a>

#### name

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.description"></a>

#### description

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.budget"></a>

#### budget

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.resources"></a>

#### resources

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.schedule"></a>

#### schedule

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.vault_ids"></a>

#### vault\_ids

<a id="qca.managed.types.deployment_create_params.DeploymentCreateParams.betas"></a>

#### betas

<a id="qca.managed.types.deployment_initial_event_union"></a>

# qca.managed.types.deployment\_initial\_event\_union

<a id="qca.managed.types.deployment_initial_event_union.DeploymentInitialEventUnion"></a>

## DeploymentInitialEventUnion

```python
class DeploymentInitialEventUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_initial_event_union.py)

<a id="qca.managed.types.deployment_initial_event_union.DeploymentInitialEventUnion.content"></a>

#### content

<a id="qca.managed.types.deployment_initial_event_union.DeploymentInitialEventUnion.type"></a>

#### type

<a id="qca.managed.types.deployment_initial_event_union.DeploymentInitialEventUnion.description"></a>

#### description

<a id="qca.managed.types.deployment_initial_event_union.DeploymentInitialEventUnion.rubric"></a>

#### rubric

<a id="qca.managed.types.deployment_initial_event_union.DeploymentInitialEventUnion.max_iterations"></a>

#### max\_iterations

<a id="qca.managed.types.deployment_list_params"></a>

# qca.managed.types.deployment\_list\_params

<a id="qca.managed.types.deployment_list_params.DeploymentListParams"></a>

## DeploymentListParams

```python
class DeploymentListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_list_params.py)

<a id="qca.managed.types.deployment_list_params.DeploymentListParams.before_id"></a>

#### before\_id

<a id="qca.managed.types.deployment_list_params.DeploymentListParams.after_id"></a>

#### after\_id

<a id="qca.managed.types.deployment_list_params.DeploymentListParams.agent_id"></a>

#### agent\_id

<a id="qca.managed.types.deployment_list_params.DeploymentListParams.created_at_gte"></a>

#### created\_at\_gte

<a id="qca.managed.types.deployment_list_params.DeploymentListParams.created_at_lte"></a>

#### created\_at\_lte

<a id="qca.managed.types.deployment_list_params.DeploymentListParams.include_archived"></a>

#### include\_archived

<a id="qca.managed.types.deployment_list_params.DeploymentListParams.limit"></a>

#### limit

<a id="qca.managed.types.deployment_list_params.DeploymentListParams.page"></a>

#### page

<a id="qca.managed.types.deployment_list_params.DeploymentListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.deployment_list_params.DeploymentListParams.status"></a>

#### status

<a id="qca.managed.types.deployment_list_params.DeploymentListParams.betas"></a>

#### betas

<a id="qca.managed.types.deployment_pause_params"></a>

# qca.managed.types.deployment\_pause\_params

<a id="qca.managed.types.deployment_pause_params.DeploymentPauseParams"></a>

## DeploymentPauseParams

```python
class DeploymentPauseParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_pause_params.py)

<a id="qca.managed.types.deployment_pause_params.DeploymentPauseParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.deployment_pause_params.DeploymentPauseParams.betas"></a>

#### betas

<a id="qca.managed.types.deployment_paused_reason_error_union"></a>

# qca.managed.types.deployment\_paused\_reason\_error\_union

<a id="qca.managed.types.deployment_paused_reason_error_union.DeploymentPausedReasonErrorUnion"></a>

## DeploymentPausedReasonErrorUnion

```python
class DeploymentPausedReasonErrorUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_paused_reason_error_union.py)

<a id="qca.managed.types.deployment_paused_reason_error_union.DeploymentPausedReasonErrorUnion.type"></a>

#### type

<a id="qca.managed.types.deployment_paused_reason_union"></a>

# qca.managed.types.deployment\_paused\_reason\_union

<a id="qca.managed.types.deployment_paused_reason_union.DeploymentPausedReasonUnion"></a>

## DeploymentPausedReasonUnion

```python
class DeploymentPausedReasonUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_paused_reason_union.py)

<a id="qca.managed.types.deployment_paused_reason_union.DeploymentPausedReasonUnion.type"></a>

#### type

<a id="qca.managed.types.deployment_paused_reason_union.DeploymentPausedReasonUnion.error"></a>

#### error

<a id="qca.managed.types.deployment_retrieve_params"></a>

# qca.managed.types.deployment\_retrieve\_params

<a id="qca.managed.types.deployment_retrieve_params.DeploymentRetrieveParams"></a>

## DeploymentRetrieveParams

```python
class DeploymentRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_retrieve_params.py)

<a id="qca.managed.types.deployment_retrieve_params.DeploymentRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.deployment_retrieve_params.DeploymentRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.deployment_run"></a>

# qca.managed.types.deployment\_run

<a id="qca.managed.types.deployment_run.DeploymentRun"></a>

## DeploymentRun

```python
class DeploymentRun(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_run.py)

<a id="qca.managed.types.deployment_run.DeploymentRun.id"></a>

#### id

<a id="qca.managed.types.deployment_run.DeploymentRun.agent"></a>

#### agent

<a id="qca.managed.types.deployment_run.DeploymentRun.created_at"></a>

#### created\_at

<a id="qca.managed.types.deployment_run.DeploymentRun.deployment_id"></a>

#### deployment\_id

<a id="qca.managed.types.deployment_run.DeploymentRun.error"></a>

#### error

<a id="qca.managed.types.deployment_run.DeploymentRun.session_id"></a>

#### session\_id

<a id="qca.managed.types.deployment_run.DeploymentRun.trigger_context"></a>

#### trigger\_context

<a id="qca.managed.types.deployment_run.DeploymentRun.type"></a>

#### type

<a id="qca.managed.types.deployment_run_error_union"></a>

# qca.managed.types.deployment\_run\_error\_union

<a id="qca.managed.types.deployment_run_error_union.DeploymentRunErrorUnion"></a>

## DeploymentRunErrorUnion

```python
class DeploymentRunErrorUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_run_error_union.py)

<a id="qca.managed.types.deployment_run_error_union.DeploymentRunErrorUnion.message"></a>

#### message

<a id="qca.managed.types.deployment_run_error_union.DeploymentRunErrorUnion.type"></a>

#### type

<a id="qca.managed.types.deployment_run_list_params"></a>

# qca.managed.types.deployment\_run\_list\_params

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams"></a>

## DeploymentRunListParams

```python
class DeploymentRunListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_run_list_params.py)

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.before_id"></a>

#### before\_id

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.after_id"></a>

#### after\_id

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.created_at_gt"></a>

#### created\_at\_gt

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.created_at_gte"></a>

#### created\_at\_gte

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.created_at_lt"></a>

#### created\_at\_lt

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.created_at_lte"></a>

#### created\_at\_lte

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.deployment_id"></a>

#### deployment\_id

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.has_error"></a>

#### has\_error

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.limit"></a>

#### limit

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.page"></a>

#### page

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.trigger_type"></a>

#### trigger\_type

<a id="qca.managed.types.deployment_run_list_params.DeploymentRunListParams.betas"></a>

#### betas

<a id="qca.managed.types.deployment_run_params"></a>

# qca.managed.types.deployment\_run\_params

<a id="qca.managed.types.deployment_run_params.DeploymentRunParams"></a>

## DeploymentRunParams

```python
class DeploymentRunParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_run_params.py)

<a id="qca.managed.types.deployment_run_params.DeploymentRunParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.deployment_run_params.DeploymentRunParams.betas"></a>

#### betas

<a id="qca.managed.types.deployment_run_retrieve_params"></a>

# qca.managed.types.deployment\_run\_retrieve\_params

<a id="qca.managed.types.deployment_run_retrieve_params.DeploymentRunRetrieveParams"></a>

## DeploymentRunRetrieveParams

```python
class DeploymentRunRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_run_retrieve_params.py)

<a id="qca.managed.types.deployment_run_retrieve_params.DeploymentRunRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.deployment_run_retrieve_params.DeploymentRunRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.deployment_unpause_params"></a>

# qca.managed.types.deployment\_unpause\_params

<a id="qca.managed.types.deployment_unpause_params.DeploymentUnpauseParams"></a>

## DeploymentUnpauseParams

```python
class DeploymentUnpauseParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_unpause_params.py)

<a id="qca.managed.types.deployment_unpause_params.DeploymentUnpauseParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.deployment_unpause_params.DeploymentUnpauseParams.betas"></a>

#### betas

<a id="qca.managed.types.deployment_update_params"></a>

# qca.managed.types.deployment\_update\_params

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams"></a>

## DeploymentUpdateParams

```python
class DeploymentUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_update_params.py)

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.environment_variables"></a>

#### environment\_variables

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.description"></a>

#### description

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.environment_id"></a>

#### environment\_id

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.name"></a>

#### name

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.resources"></a>

#### resources

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.vault_ids"></a>

#### vault\_ids

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.agent"></a>

#### agent

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.budget"></a>

#### budget

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.initial_events"></a>

#### initial\_events

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.schedule"></a>

#### schedule

<a id="qca.managed.types.deployment_update_params.DeploymentUpdateParams.betas"></a>

#### betas

<a id="qca.managed.types.deployment_user_define_outcome_event_rubric_union"></a>

# qca.managed.types.deployment\_user\_define\_outcome\_event\_rubric\_union

<a id="qca.managed.types.deployment_user_define_outcome_event_rubric_union.DeploymentUserDefineOutcomeEventRubricUnion"></a>

## DeploymentUserDefineOutcomeEventRubricUnion

```python
class DeploymentUserDefineOutcomeEventRubricUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_user_define_outcome_event_rubric_union.py)

<a id="qca.managed.types.deployment_user_define_outcome_event_rubric_union.DeploymentUserDefineOutcomeEventRubricUnion.file_id"></a>

#### file\_id

<a id="qca.managed.types.deployment_user_define_outcome_event_rubric_union.DeploymentUserDefineOutcomeEventRubricUnion.type"></a>

#### type

<a id="qca.managed.types.deployment_user_define_outcome_event_rubric_union.DeploymentUserDefineOutcomeEventRubricUnion.content"></a>

#### content

<a id="qca.managed.types.deployment_user_message_event_content_union"></a>

# qca.managed.types.deployment\_user\_message\_event\_content\_union

<a id="qca.managed.types.deployment_user_message_event_content_union.DeploymentUserMessageEventContentUnion"></a>

## DeploymentUserMessageEventContentUnion

```python
class DeploymentUserMessageEventContentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_user_message_event_content_union.py)

<a id="qca.managed.types.deployment_user_message_event_content_union.DeploymentUserMessageEventContentUnion.text"></a>

#### text

<a id="qca.managed.types.deployment_user_message_event_content_union.DeploymentUserMessageEventContentUnion.type"></a>

#### type

<a id="qca.managed.types.deployment_user_message_event_content_union.DeploymentUserMessageEventContentUnion.source"></a>

#### source

<a id="qca.managed.types.deployment_user_message_event_content_union.DeploymentUserMessageEventContentUnion.context"></a>

#### context

<a id="qca.managed.types.deployment_user_message_event_content_union.DeploymentUserMessageEventContentUnion.title"></a>

#### title

<a id="qca.managed.types.deployment_user_message_event_content_union_source"></a>

# qca.managed.types.deployment\_user\_message\_event\_content\_union\_source

<a id="qca.managed.types.deployment_user_message_event_content_union_source.DeploymentUserMessageEventContentUnionSource"></a>

## DeploymentUserMessageEventContentUnionSource

```python
class DeploymentUserMessageEventContentUnionSource(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/deployment_user_message_event_content_union_source.py)

<a id="qca.managed.types.deployment_user_message_event_content_union_source.DeploymentUserMessageEventContentUnionSource.data"></a>

#### data

<a id="qca.managed.types.deployment_user_message_event_content_union_source.DeploymentUserMessageEventContentUnionSource.media_type"></a>

#### media\_type

<a id="qca.managed.types.deployment_user_message_event_content_union_source.DeploymentUserMessageEventContentUnionSource.type"></a>

#### type

<a id="qca.managed.types.deployment_user_message_event_content_union_source.DeploymentUserMessageEventContentUnionSource.url"></a>

#### url

<a id="qca.managed.types.deployment_user_message_event_content_union_source.DeploymentUserMessageEventContentUnionSource.file_id"></a>

#### file\_id

<a id="qca.managed.types.document_block_param"></a>

# qca.managed.types.document\_block\_param

<a id="qca.managed.types.document_block_param.DocumentBlockParam"></a>

## DocumentBlockParam

```python
class DocumentBlockParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/document_block_param.py)

<a id="qca.managed.types.document_block_param.DocumentBlockParam.source"></a>

#### source

<a id="qca.managed.types.document_block_param.DocumentBlockParam.type"></a>

#### type

<a id="qca.managed.types.document_block_param.DocumentBlockParam.context"></a>

#### context

<a id="qca.managed.types.document_block_param.DocumentBlockParam.title"></a>

#### title

<a id="qca.managed.types.dream"></a>

# qca.managed.types.dream

<a id="qca.managed.types.dream.Dream"></a>

## Dream

```python
class Dream(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream.py)

<a id="qca.managed.types.dream.Dream.id"></a>

#### id

<a id="qca.managed.types.dream.Dream.archived_at"></a>

#### archived\_at

<a id="qca.managed.types.dream.Dream.created_at"></a>

#### created\_at

<a id="qca.managed.types.dream.Dream.ended_at"></a>

#### ended\_at

<a id="qca.managed.types.dream.Dream.error"></a>

#### error

<a id="qca.managed.types.dream.Dream.inputs"></a>

#### inputs

<a id="qca.managed.types.dream.Dream.instructions"></a>

#### instructions

<a id="qca.managed.types.dream.Dream.model"></a>

#### model

<a id="qca.managed.types.dream.Dream.output_behavior"></a>

#### output\_behavior

<a id="qca.managed.types.dream.Dream.outputs"></a>

#### outputs

<a id="qca.managed.types.dream.Dream.session_id"></a>

#### session\_id

<a id="qca.managed.types.dream.Dream.status"></a>

#### status

<a id="qca.managed.types.dream.Dream.type"></a>

#### type

<a id="qca.managed.types.dream.Dream.usage"></a>

#### usage

<a id="qca.managed.types.dream_archive_params"></a>

# qca.managed.types.dream\_archive\_params

<a id="qca.managed.types.dream_archive_params.DreamArchiveParams"></a>

## DreamArchiveParams

```python
class DreamArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_archive_params.py)

<a id="qca.managed.types.dream_archive_params.DreamArchiveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.dream_archive_params.DreamArchiveParams.betas"></a>

#### betas

<a id="qca.managed.types.dream_cancel_params"></a>

# qca.managed.types.dream\_cancel\_params

<a id="qca.managed.types.dream_cancel_params.DreamCancelParams"></a>

## DreamCancelParams

```python
class DreamCancelParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_cancel_params.py)

<a id="qca.managed.types.dream_cancel_params.DreamCancelParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.dream_cancel_params.DreamCancelParams.betas"></a>

#### betas

<a id="qca.managed.types.dream_create_params"></a>

# qca.managed.types.dream\_create\_params

<a id="qca.managed.types.dream_create_params.DreamCreateParams"></a>

## DreamCreateParams

```python
class DreamCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_create_params.py)

<a id="qca.managed.types.dream_create_params.DreamCreateParams.inputs"></a>

#### inputs

<a id="qca.managed.types.dream_create_params.DreamCreateParams.model"></a>

#### model

<a id="qca.managed.types.dream_create_params.DreamCreateParams.instructions"></a>

#### instructions

<a id="qca.managed.types.dream_create_params.DreamCreateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.dream_create_params.DreamCreateParams.output_behavior"></a>

#### output\_behavior

<a id="qca.managed.types.dream_create_params.DreamCreateParams.betas"></a>

#### betas

<a id="qca.managed.types.dream_error"></a>

# qca.managed.types.dream\_error

<a id="qca.managed.types.dream_error.DreamError"></a>

## DreamError

```python
class DreamError(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_error.py)

<a id="qca.managed.types.dream_error.DreamError.message"></a>

#### message

<a id="qca.managed.types.dream_error.DreamError.type"></a>

#### type

<a id="qca.managed.types.dream_input_union"></a>

# qca.managed.types.dream\_input\_union

<a id="qca.managed.types.dream_input_union.DreamInputUnion"></a>

## DreamInputUnion

```python
class DreamInputUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_input_union.py)

<a id="qca.managed.types.dream_input_union.DreamInputUnion.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.dream_input_union.DreamInputUnion.type"></a>

#### type

<a id="qca.managed.types.dream_input_union.DreamInputUnion.session_ids"></a>

#### session\_ids

<a id="qca.managed.types.dream_list_params"></a>

# qca.managed.types.dream\_list\_params

<a id="qca.managed.types.dream_list_params.DreamListParams"></a>

## DreamListParams

```python
class DreamListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_list_params.py)

<a id="qca.managed.types.dream_list_params.DreamListParams.created_at_gt"></a>

#### created\_at\_gt

<a id="qca.managed.types.dream_list_params.DreamListParams.created_at_lt"></a>

#### created\_at\_lt

<a id="qca.managed.types.dream_list_params.DreamListParams.include_archived"></a>

#### include\_archived

<a id="qca.managed.types.dream_list_params.DreamListParams.limit"></a>

#### limit

<a id="qca.managed.types.dream_list_params.DreamListParams.page"></a>

#### page

<a id="qca.managed.types.dream_list_params.DreamListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.dream_list_params.DreamListParams.statuses"></a>

#### statuses

<a id="qca.managed.types.dream_list_params.DreamListParams.betas"></a>

#### betas

<a id="qca.managed.types.dream_memory_store_input_param"></a>

# qca.managed.types.dream\_memory\_store\_input\_param

<a id="qca.managed.types.dream_memory_store_input_param.DreamMemoryStoreInputParam"></a>

## DreamMemoryStoreInputParam

```python
class DreamMemoryStoreInputParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_memory_store_input_param.py)

<a id="qca.managed.types.dream_memory_store_input_param.DreamMemoryStoreInputParam.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.dream_memory_store_input_param.DreamMemoryStoreInputParam.type"></a>

#### type

<a id="qca.managed.types.dream_model_config"></a>

# qca.managed.types.dream\_model\_config

<a id="qca.managed.types.dream_model_config.DreamModelConfig"></a>

## DreamModelConfig

```python
class DreamModelConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_model_config.py)

<a id="qca.managed.types.dream_model_config.DreamModelConfig.id"></a>

#### id

<a id="qca.managed.types.dream_model_config.DreamModelConfig.speed"></a>

#### speed

<a id="qca.managed.types.dream_model_config_param"></a>

# qca.managed.types.dream\_model\_config\_param

<a id="qca.managed.types.dream_model_config_param.DreamModelConfigParam"></a>

## DreamModelConfigParam

```python
class DreamModelConfigParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_model_config_param.py)

<a id="qca.managed.types.dream_model_config_param.DreamModelConfigParam.id"></a>

#### id

<a id="qca.managed.types.dream_model_config_param.DreamModelConfigParam.speed"></a>

#### speed

<a id="qca.managed.types.dream_output"></a>

# qca.managed.types.dream\_output

<a id="qca.managed.types.dream_output.DreamOutput"></a>

## DreamOutput

```python
class DreamOutput(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_output.py)

<a id="qca.managed.types.dream_output.DreamOutput.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.dream_output.DreamOutput.type"></a>

#### type

<a id="qca.managed.types.dream_retrieve_params"></a>

# qca.managed.types.dream\_retrieve\_params

<a id="qca.managed.types.dream_retrieve_params.DreamRetrieveParams"></a>

## DreamRetrieveParams

```python
class DreamRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_retrieve_params.py)

<a id="qca.managed.types.dream_retrieve_params.DreamRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.dream_retrieve_params.DreamRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.dream_sessions_input_param"></a>

# qca.managed.types.dream\_sessions\_input\_param

<a id="qca.managed.types.dream_sessions_input_param.DreamSessionsInputParam"></a>

## DreamSessionsInputParam

```python
class DreamSessionsInputParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_sessions_input_param.py)

<a id="qca.managed.types.dream_sessions_input_param.DreamSessionsInputParam.session_ids"></a>

#### session\_ids

<a id="qca.managed.types.dream_sessions_input_param.DreamSessionsInputParam.type"></a>

#### type

<a id="qca.managed.types.dream_usage"></a>

# qca.managed.types.dream\_usage

<a id="qca.managed.types.dream_usage.DreamUsage"></a>

## DreamUsage

```python
class DreamUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/dream_usage.py)

<a id="qca.managed.types.dream_usage.DreamUsage.cache_creation_input_tokens"></a>

#### cache\_creation\_input\_tokens

<a id="qca.managed.types.dream_usage.DreamUsage.cache_read_input_tokens"></a>

#### cache\_read\_input\_tokens

<a id="qca.managed.types.dream_usage.DreamUsage.input_tokens"></a>

#### input\_tokens

<a id="qca.managed.types.dream_usage.DreamUsage.output_tokens"></a>

#### output\_tokens

<a id="qca.managed.types.edit_tool_config_params"></a>

# qca.managed.types.edit\_tool\_config\_params

<a id="qca.managed.types.edit_tool_config_params.EditToolConfigParams"></a>

## EditToolConfigParams

```python
class EditToolConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/edit_tool_config_params.py)

<a id="qca.managed.types.edit_tool_config_params.EditToolConfigParams.enabled"></a>

#### enabled

<a id="qca.managed.types.edit_tool_config_params.EditToolConfigParams.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.edit_tool_config_params.EditToolConfigParams.type"></a>

#### type

<a id="qca.managed.types.edit_tool_config_params.EditToolConfigParams.name"></a>

#### name

<a id="qca.managed.types.effort_capability"></a>

# qca.managed.types.effort\_capability

<a id="qca.managed.types.effort_capability.EffortCapability"></a>

## EffortCapability

```python
class EffortCapability(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/effort_capability.py)

<a id="qca.managed.types.effort_capability.EffortCapability.high"></a>

#### high

<a id="qca.managed.types.effort_capability.EffortCapability.low"></a>

#### low

<a id="qca.managed.types.effort_capability.EffortCapability.max"></a>

#### max

<a id="qca.managed.types.effort_capability.EffortCapability.medium"></a>

#### medium

<a id="qca.managed.types.effort_capability.EffortCapability.supported"></a>

#### supported

<a id="qca.managed.types.effort_capability.EffortCapability.xhigh"></a>

#### xhigh

<a id="qca.managed.types.effort_high_param"></a>

# qca.managed.types.effort\_high\_param

<a id="qca.managed.types.effort_high_param.EffortHighParam"></a>

## EffortHighParam

```python
class EffortHighParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/effort_high_param.py)

<a id="qca.managed.types.effort_high_param.EffortHighParam.type"></a>

#### type

<a id="qca.managed.types.effort_low_param"></a>

# qca.managed.types.effort\_low\_param

<a id="qca.managed.types.effort_low_param.EffortLowParam"></a>

## EffortLowParam

```python
class EffortLowParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/effort_low_param.py)

<a id="qca.managed.types.effort_low_param.EffortLowParam.type"></a>

#### type

<a id="qca.managed.types.effort_max_param"></a>

# qca.managed.types.effort\_max\_param

<a id="qca.managed.types.effort_max_param.EffortMaxParam"></a>

## EffortMaxParam

```python
class EffortMaxParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/effort_max_param.py)

<a id="qca.managed.types.effort_max_param.EffortMaxParam.type"></a>

#### type

<a id="qca.managed.types.effort_medium_param"></a>

# qca.managed.types.effort\_medium\_param

<a id="qca.managed.types.effort_medium_param.EffortMediumParam"></a>

## EffortMediumParam

```python
class EffortMediumParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/effort_medium_param.py)

<a id="qca.managed.types.effort_medium_param.EffortMediumParam.type"></a>

#### type

<a id="qca.managed.types.effort_xhigh_param"></a>

# qca.managed.types.effort\_xhigh\_param

<a id="qca.managed.types.effort_xhigh_param.EffortXhighParam"></a>

## EffortXhighParam

```python
class EffortXhighParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/effort_xhigh_param.py)

<a id="qca.managed.types.effort_xhigh_param.EffortXhighParam.type"></a>

#### type

<a id="qca.managed.types.environment"></a>

# qca.managed.types.environment

<a id="qca.managed.types.environment.Environment"></a>

## Environment

```python
class Environment(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment.py)

<a id="qca.managed.types.environment.Environment.id"></a>

#### id

<a id="qca.managed.types.environment.Environment.archived_at"></a>

#### archived\_at

<a id="qca.managed.types.environment.Environment.config"></a>

#### config

<a id="qca.managed.types.environment.Environment.created_at"></a>

#### created\_at

<a id="qca.managed.types.environment.Environment.description"></a>

#### description

<a id="qca.managed.types.environment.Environment.metadata"></a>

#### metadata

<a id="qca.managed.types.environment.Environment.name"></a>

#### name

<a id="qca.managed.types.environment.Environment.type"></a>

#### type

<a id="qca.managed.types.environment.Environment.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.environment.Environment.scope"></a>

#### scope

<a id="qca.managed.types.environment_archive_params"></a>

# qca.managed.types.environment\_archive\_params

<a id="qca.managed.types.environment_archive_params.EnvironmentArchiveParams"></a>

## EnvironmentArchiveParams

```python
class EnvironmentArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_archive_params.py)

<a id="qca.managed.types.environment_archive_params.EnvironmentArchiveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.environment_archive_params.EnvironmentArchiveParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_config_union"></a>

# qca.managed.types.environment\_config\_union

<a id="qca.managed.types.environment_config_union.EnvironmentConfigUnion"></a>

## EnvironmentConfigUnion

```python
class EnvironmentConfigUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_config_union.py)

<a id="qca.managed.types.environment_config_union.EnvironmentConfigUnion.networking"></a>

#### networking

<a id="qca.managed.types.environment_config_union.EnvironmentConfigUnion.packages"></a>

#### packages

<a id="qca.managed.types.environment_config_union.EnvironmentConfigUnion.type"></a>

#### type

<a id="qca.managed.types.environment_create_params"></a>

# qca.managed.types.environment\_create\_params

<a id="qca.managed.types.environment_create_params.EnvironmentCreateParams"></a>

## EnvironmentCreateParams

```python
class EnvironmentCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_create_params.py)

<a id="qca.managed.types.environment_create_params.EnvironmentCreateParams.name"></a>

#### name

<a id="qca.managed.types.environment_create_params.EnvironmentCreateParams.description"></a>

#### description

<a id="qca.managed.types.environment_create_params.EnvironmentCreateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.environment_create_params.EnvironmentCreateParams.config"></a>

#### config

<a id="qca.managed.types.environment_create_params.EnvironmentCreateParams.scope"></a>

#### scope

<a id="qca.managed.types.environment_create_params.EnvironmentCreateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.environment_create_params.EnvironmentCreateParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_delete_params"></a>

# qca.managed.types.environment\_delete\_params

<a id="qca.managed.types.environment_delete_params.EnvironmentDeleteParams"></a>

## EnvironmentDeleteParams

```python
class EnvironmentDeleteParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_delete_params.py)

<a id="qca.managed.types.environment_delete_params.EnvironmentDeleteParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.environment_delete_params.EnvironmentDeleteParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_delete_response"></a>

# qca.managed.types.environment\_delete\_response

<a id="qca.managed.types.environment_delete_response.EnvironmentDeleteResponse"></a>

## EnvironmentDeleteResponse

```python
class EnvironmentDeleteResponse(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_delete_response.py)

<a id="qca.managed.types.environment_delete_response.EnvironmentDeleteResponse.id"></a>

#### id

<a id="qca.managed.types.environment_delete_response.EnvironmentDeleteResponse.type"></a>

#### type

<a id="qca.managed.types.environment_list_params"></a>

# qca.managed.types.environment\_list\_params

<a id="qca.managed.types.environment_list_params.EnvironmentListParams"></a>

## EnvironmentListParams

```python
class EnvironmentListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_list_params.py)

<a id="qca.managed.types.environment_list_params.EnvironmentListParams.created_at_gte"></a>

#### created\_at\_gte

<a id="qca.managed.types.environment_list_params.EnvironmentListParams.created_at_lte"></a>

#### created\_at\_lte

<a id="qca.managed.types.environment_list_params.EnvironmentListParams.page"></a>

#### page

<a id="qca.managed.types.environment_list_params.EnvironmentListParams.include_archived"></a>

#### include\_archived

<a id="qca.managed.types.environment_list_params.EnvironmentListParams.limit"></a>

#### limit

<a id="qca.managed.types.environment_list_params.EnvironmentListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.environment_list_params.EnvironmentListParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_retrieve_params"></a>

# qca.managed.types.environment\_retrieve\_params

<a id="qca.managed.types.environment_retrieve_params.EnvironmentRetrieveParams"></a>

## EnvironmentRetrieveParams

```python
class EnvironmentRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_retrieve_params.py)

<a id="qca.managed.types.environment_retrieve_params.EnvironmentRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.environment_retrieve_params.EnvironmentRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_update_params"></a>

# qca.managed.types.environment\_update\_params

<a id="qca.managed.types.environment_update_params.EnvironmentUpdateParams"></a>

## EnvironmentUpdateParams

```python
class EnvironmentUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_update_params.py)

<a id="qca.managed.types.environment_update_params.EnvironmentUpdateParams.description"></a>

#### description

<a id="qca.managed.types.environment_update_params.EnvironmentUpdateParams.name"></a>

#### name

<a id="qca.managed.types.environment_update_params.EnvironmentUpdateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.environment_update_params.EnvironmentUpdateParams.config"></a>

#### config

<a id="qca.managed.types.environment_update_params.EnvironmentUpdateParams.scope"></a>

#### scope

<a id="qca.managed.types.environment_update_params.EnvironmentUpdateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.environment_update_params.EnvironmentUpdateParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_variable_auth_response_networking_union"></a>

# qca.managed.types.environment\_variable\_auth\_response\_networking\_union

<a id="qca.managed.types.environment_variable_auth_response_networking_union.EnvironmentVariableAuthResponseNetworkingUnion"></a>

## EnvironmentVariableAuthResponseNetworkingUnion

```python
class EnvironmentVariableAuthResponseNetworkingUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_variable_auth_response_networking_union.py)

<a id="qca.managed.types.environment_variable_auth_response_networking_union.EnvironmentVariableAuthResponseNetworkingUnion.type"></a>

#### type

<a id="qca.managed.types.environment_variable_auth_response_networking_union.EnvironmentVariableAuthResponseNetworkingUnion.allowed_hosts"></a>

#### allowed\_hosts

<a id="qca.managed.types.environment_variable_create_params"></a>

# qca.managed.types.environment\_variable\_create\_params

<a id="qca.managed.types.environment_variable_create_params.EnvironmentVariableCreateParams"></a>

## EnvironmentVariableCreateParams

```python
class EnvironmentVariableCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_variable_create_params.py)

<a id="qca.managed.types.environment_variable_create_params.EnvironmentVariableCreateParams.networking"></a>

#### networking

<a id="qca.managed.types.environment_variable_create_params.EnvironmentVariableCreateParams.secret_name"></a>

#### secret\_name

<a id="qca.managed.types.environment_variable_create_params.EnvironmentVariableCreateParams.secret_value"></a>

#### secret\_value

<a id="qca.managed.types.environment_variable_create_params.EnvironmentVariableCreateParams.type"></a>

#### type

<a id="qca.managed.types.environment_variable_create_params.EnvironmentVariableCreateParams.injection_location"></a>

#### injection\_location

<a id="qca.managed.types.environment_variable_update_params"></a>

# qca.managed.types.environment\_variable\_update\_params

<a id="qca.managed.types.environment_variable_update_params.EnvironmentVariableUpdateParams"></a>

## EnvironmentVariableUpdateParams

```python
class EnvironmentVariableUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_variable_update_params.py)

<a id="qca.managed.types.environment_variable_update_params.EnvironmentVariableUpdateParams.type"></a>

#### type

<a id="qca.managed.types.environment_variable_update_params.EnvironmentVariableUpdateParams.secret_value"></a>

#### secret\_value

<a id="qca.managed.types.environment_variable_update_params.EnvironmentVariableUpdateParams.injection_location"></a>

#### injection\_location

<a id="qca.managed.types.environment_variable_update_params.EnvironmentVariableUpdateParams.networking"></a>

#### networking

<a id="qca.managed.types.environment_work_ack_params"></a>

# qca.managed.types.environment\_work\_ack\_params

<a id="qca.managed.types.environment_work_ack_params.EnvironmentWorkAckParams"></a>

## EnvironmentWorkAckParams

```python
class EnvironmentWorkAckParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_work_ack_params.py)

<a id="qca.managed.types.environment_work_ack_params.EnvironmentWorkAckParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_work_heartbeat_params"></a>

# qca.managed.types.environment\_work\_heartbeat\_params

<a id="qca.managed.types.environment_work_heartbeat_params.EnvironmentWorkHeartbeatParams"></a>

## EnvironmentWorkHeartbeatParams

```python
class EnvironmentWorkHeartbeatParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_work_heartbeat_params.py)

<a id="qca.managed.types.environment_work_heartbeat_params.EnvironmentWorkHeartbeatParams.desired_ttl_seconds"></a>

#### desired\_ttl\_seconds

<a id="qca.managed.types.environment_work_heartbeat_params.EnvironmentWorkHeartbeatParams.expected_last_heartbeat"></a>

#### expected\_last\_heartbeat

<a id="qca.managed.types.environment_work_heartbeat_params.EnvironmentWorkHeartbeatParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_work_list_params"></a>

# qca.managed.types.environment\_work\_list\_params

<a id="qca.managed.types.environment_work_list_params.EnvironmentWorkListParams"></a>

## EnvironmentWorkListParams

```python
class EnvironmentWorkListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_work_list_params.py)

<a id="qca.managed.types.environment_work_list_params.EnvironmentWorkListParams.before_id"></a>

#### before\_id

<a id="qca.managed.types.environment_work_list_params.EnvironmentWorkListParams.after_id"></a>

#### after\_id

<a id="qca.managed.types.environment_work_list_params.EnvironmentWorkListParams.page"></a>

#### page

<a id="qca.managed.types.environment_work_list_params.EnvironmentWorkListParams.limit"></a>

#### limit

<a id="qca.managed.types.environment_work_list_params.EnvironmentWorkListParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_work_poll_params"></a>

# qca.managed.types.environment\_work\_poll\_params

<a id="qca.managed.types.environment_work_poll_params.EnvironmentWorkPollParams"></a>

## EnvironmentWorkPollParams

```python
class EnvironmentWorkPollParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_work_poll_params.py)

<a id="qca.managed.types.environment_work_poll_params.EnvironmentWorkPollParams.block_ms"></a>

#### block\_ms

<a id="qca.managed.types.environment_work_poll_params.EnvironmentWorkPollParams.reclaim_older_than_ms"></a>

#### reclaim\_older\_than\_ms

<a id="qca.managed.types.environment_work_poll_params.EnvironmentWorkPollParams.worker_id"></a>

#### worker\_id

<a id="qca.managed.types.environment_work_poll_params.EnvironmentWorkPollParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_work_retrieve_params"></a>

# qca.managed.types.environment\_work\_retrieve\_params

<a id="qca.managed.types.environment_work_retrieve_params.EnvironmentWorkRetrieveParams"></a>

## EnvironmentWorkRetrieveParams

```python
class EnvironmentWorkRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_work_retrieve_params.py)

<a id="qca.managed.types.environment_work_retrieve_params.EnvironmentWorkRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.environment_work_retrieve_params.EnvironmentWorkRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_work_stats_params"></a>

# qca.managed.types.environment\_work\_stats\_params

<a id="qca.managed.types.environment_work_stats_params.EnvironmentWorkStatsParams"></a>

## EnvironmentWorkStatsParams

```python
class EnvironmentWorkStatsParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_work_stats_params.py)

<a id="qca.managed.types.environment_work_stats_params.EnvironmentWorkStatsParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.environment_work_stats_params.EnvironmentWorkStatsParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_work_stop_params"></a>

# qca.managed.types.environment\_work\_stop\_params

<a id="qca.managed.types.environment_work_stop_params.EnvironmentWorkStopParams"></a>

## EnvironmentWorkStopParams

```python
class EnvironmentWorkStopParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_work_stop_params.py)

<a id="qca.managed.types.environment_work_stop_params.EnvironmentWorkStopParams.force"></a>

#### force

<a id="qca.managed.types.environment_work_stop_params.EnvironmentWorkStopParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.environment_work_stop_params.EnvironmentWorkStopParams.betas"></a>

#### betas

<a id="qca.managed.types.environment_work_update_params"></a>

# qca.managed.types.environment\_work\_update\_params

<a id="qca.managed.types.environment_work_update_params.EnvironmentWorkUpdateParams"></a>

## EnvironmentWorkUpdateParams

```python
class EnvironmentWorkUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/environment_work_update_params.py)

<a id="qca.managed.types.environment_work_update_params.EnvironmentWorkUpdateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.environment_work_update_params.EnvironmentWorkUpdateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.environment_work_update_params.EnvironmentWorkUpdateParams.betas"></a>

#### betas

<a id="qca.managed.types.file_delete_params"></a>

# qca.managed.types.file\_delete\_params

<a id="qca.managed.types.file_delete_params.FileDeleteParams"></a>

## FileDeleteParams

```python
class FileDeleteParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_delete_params.py)

<a id="qca.managed.types.file_delete_params.FileDeleteParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.file_delete_params.FileDeleteParams.betas"></a>

#### betas

<a id="qca.managed.types.file_document_source_param"></a>

# qca.managed.types.file\_document\_source\_param

<a id="qca.managed.types.file_document_source_param.FileDocumentSourceParam"></a>

## FileDocumentSourceParam

```python
class FileDocumentSourceParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_document_source_param.py)

<a id="qca.managed.types.file_document_source_param.FileDocumentSourceParam.file_id"></a>

#### file\_id

<a id="qca.managed.types.file_document_source_param.FileDocumentSourceParam.type"></a>

#### type

<a id="qca.managed.types.file_download_params"></a>

# qca.managed.types.file\_download\_params

<a id="qca.managed.types.file_download_params.FileDownloadParams"></a>

## FileDownloadParams

```python
class FileDownloadParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_download_params.py)

<a id="qca.managed.types.file_download_params.FileDownloadParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.file_download_params.FileDownloadParams.betas"></a>

#### betas

<a id="qca.managed.types.file_get_metadata_params"></a>

# qca.managed.types.file\_get\_metadata\_params

<a id="qca.managed.types.file_get_metadata_params.FileGetMetadataParams"></a>

## FileGetMetadataParams

```python
class FileGetMetadataParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_get_metadata_params.py)

<a id="qca.managed.types.file_get_metadata_params.FileGetMetadataParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.file_get_metadata_params.FileGetMetadataParams.betas"></a>

#### betas

<a id="qca.managed.types.file_image_source_param"></a>

# qca.managed.types.file\_image\_source\_param

<a id="qca.managed.types.file_image_source_param.FileImageSourceParam"></a>

## FileImageSourceParam

```python
class FileImageSourceParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_image_source_param.py)

<a id="qca.managed.types.file_image_source_param.FileImageSourceParam.file_id"></a>

#### file\_id

<a id="qca.managed.types.file_image_source_param.FileImageSourceParam.type"></a>

#### type

<a id="qca.managed.types.file_list_params"></a>

# qca.managed.types.file\_list\_params

<a id="qca.managed.types.file_list_params.FileListParams"></a>

## FileListParams

```python
class FileListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_list_params.py)

<a id="qca.managed.types.file_list_params.FileListParams.name"></a>

#### name

<a id="qca.managed.types.file_list_params.FileListParams.before_id"></a>

#### before\_id

<a id="qca.managed.types.file_list_params.FileListParams.after_id"></a>

#### after\_id

<a id="qca.managed.types.file_list_params.FileListParams.page"></a>

#### page

<a id="qca.managed.types.file_list_params.FileListParams.limit"></a>

#### limit

<a id="qca.managed.types.file_list_params.FileListParams.scope_id"></a>

#### scope\_id

<a id="qca.managed.types.file_list_params.FileListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.file_list_params.FileListParams.i_ds"></a>

#### i\_ds

<a id="qca.managed.types.file_list_params.FileListParams.betas"></a>

#### betas

<a id="qca.managed.types.file_metadata"></a>

# qca.managed.types.file\_metadata

<a id="qca.managed.types.file_metadata.FileMetadata"></a>

## FileMetadata

```python
class FileMetadata(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_metadata.py)

<a id="qca.managed.types.file_metadata.FileMetadata.metadata"></a>

#### metadata

<a id="qca.managed.types.file_metadata.FileMetadata.status"></a>

#### status

<a id="qca.managed.types.file_metadata.FileMetadata.id"></a>

#### id

<a id="qca.managed.types.file_metadata.FileMetadata.created_at"></a>

#### created\_at

<a id="qca.managed.types.file_metadata.FileMetadata.filename"></a>

#### filename

<a id="qca.managed.types.file_metadata.FileMetadata.mime_type"></a>

#### mime\_type

<a id="qca.managed.types.file_metadata.FileMetadata.size_bytes"></a>

#### size\_bytes

<a id="qca.managed.types.file_metadata.FileMetadata.type"></a>

#### type

<a id="qca.managed.types.file_metadata.FileMetadata.downloadable"></a>

#### downloadable

<a id="qca.managed.types.file_metadata.FileMetadata.expires_at"></a>

#### expires\_at

<a id="qca.managed.types.file_metadata.FileMetadata.scope"></a>

#### scope

<a id="qca.managed.types.file_resource"></a>

# qca.managed.types.file\_resource

<a id="qca.managed.types.file_resource.FileResource"></a>

## FileResource

```python
class FileResource(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_resource.py)

<a id="qca.managed.types.file_resource.FileResource.id"></a>

#### id

<a id="qca.managed.types.file_resource.FileResource.created_at"></a>

#### created\_at

<a id="qca.managed.types.file_resource.FileResource.file_id"></a>

#### file\_id

<a id="qca.managed.types.file_resource.FileResource.mount_path"></a>

#### mount\_path

<a id="qca.managed.types.file_resource.FileResource.type"></a>

#### type

<a id="qca.managed.types.file_resource.FileResource.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.file_resource_params"></a>

# qca.managed.types.file\_resource\_params

<a id="qca.managed.types.file_resource_params.FileResourceParams"></a>

## FileResourceParams

```python
class FileResourceParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_resource_params.py)

<a id="qca.managed.types.file_resource_params.FileResourceParams.file_id"></a>

#### file\_id

<a id="qca.managed.types.file_resource_params.FileResourceParams.type"></a>

#### type

<a id="qca.managed.types.file_resource_params.FileResourceParams.mount_path"></a>

#### mount\_path

<a id="qca.managed.types.file_rubric_params"></a>

# qca.managed.types.file\_rubric\_params

<a id="qca.managed.types.file_rubric_params.FileRubricParams"></a>

## FileRubricParams

```python
class FileRubricParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_rubric_params.py)

<a id="qca.managed.types.file_rubric_params.FileRubricParams.file_id"></a>

#### file\_id

<a id="qca.managed.types.file_rubric_params.FileRubricParams.type"></a>

#### type

<a id="qca.managed.types.file_scope"></a>

# qca.managed.types.file\_scope

<a id="qca.managed.types.file_scope.FileScope"></a>

## FileScope

```python
class FileScope(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_scope.py)

<a id="qca.managed.types.file_scope.FileScope.id"></a>

#### id

<a id="qca.managed.types.file_scope.FileScope.type"></a>

#### type

<a id="qca.managed.types.file_upload_params"></a>

# qca.managed.types.file\_upload\_params

<a id="qca.managed.types.file_upload_params.FileUploadParams"></a>

## FileUploadParams

```python
class FileUploadParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/file_upload_params.py)

<a id="qca.managed.types.file_upload_params.FileUploadParams.name"></a>

#### name

<a id="qca.managed.types.file_upload_params.FileUploadParams.metadata"></a>

#### metadata

<a id="qca.managed.types.file_upload_params.FileUploadParams.file"></a>

#### file

<a id="qca.managed.types.file_upload_params.FileUploadParams.expires_in_seconds"></a>

#### expires\_in\_seconds

<a id="qca.managed.types.file_upload_params.FileUploadParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.file_upload_params.FileUploadParams.betas"></a>

#### betas

<a id="qca.managed.types.git_hub_repository_resource_checkout_union"></a>

# qca.managed.types.git\_hub\_repository\_resource\_checkout\_union

<a id="qca.managed.types.git_hub_repository_resource_checkout_union.GitHubRepositoryResourceCheckoutUnion"></a>

## GitHubRepositoryResourceCheckoutUnion

```python
class GitHubRepositoryResourceCheckoutUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/git_hub_repository_resource_checkout_union.py)

<a id="qca.managed.types.git_hub_repository_resource_checkout_union.GitHubRepositoryResourceCheckoutUnion.name"></a>

#### name

<a id="qca.managed.types.git_hub_repository_resource_checkout_union.GitHubRepositoryResourceCheckoutUnion.type"></a>

#### type

<a id="qca.managed.types.git_hub_repository_resource_checkout_union.GitHubRepositoryResourceCheckoutUnion.sha"></a>

#### sha

<a id="qca.managed.types.git_hub_repository_resource_config_checkout_union"></a>

# qca.managed.types.git\_hub\_repository\_resource\_config\_checkout\_union

<a id="qca.managed.types.git_hub_repository_resource_config_checkout_union.GitHubRepositoryResourceConfigCheckoutUnion"></a>

## GitHubRepositoryResourceConfigCheckoutUnion

```python
class GitHubRepositoryResourceConfigCheckoutUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/git_hub_repository_resource_config_checkout_union.py)

<a id="qca.managed.types.git_hub_repository_resource_config_checkout_union.GitHubRepositoryResourceConfigCheckoutUnion.name"></a>

#### name

<a id="qca.managed.types.git_hub_repository_resource_config_checkout_union.GitHubRepositoryResourceConfigCheckoutUnion.type"></a>

#### type

<a id="qca.managed.types.git_hub_repository_resource_config_checkout_union.GitHubRepositoryResourceConfigCheckoutUnion.sha"></a>

#### sha

<a id="qca.managed.types.git_hub_repository_resource_params"></a>

# qca.managed.types.git\_hub\_repository\_resource\_params

<a id="qca.managed.types.git_hub_repository_resource_params.GitHubRepositoryResourceParams"></a>

## GitHubRepositoryResourceParams

```python
class GitHubRepositoryResourceParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/git_hub_repository_resource_params.py)

<a id="qca.managed.types.git_hub_repository_resource_params.GitHubRepositoryResourceParams.authorization_token"></a>

#### authorization\_token

<a id="qca.managed.types.git_hub_repository_resource_params.GitHubRepositoryResourceParams.type"></a>

#### type

<a id="qca.managed.types.git_hub_repository_resource_params.GitHubRepositoryResourceParams.url"></a>

#### url

<a id="qca.managed.types.git_hub_repository_resource_params.GitHubRepositoryResourceParams.mount_path"></a>

#### mount\_path

<a id="qca.managed.types.git_hub_repository_resource_params.GitHubRepositoryResourceParams.checkout"></a>

#### checkout

<a id="qca.managed.types.glob_tool_config_params"></a>

# qca.managed.types.glob\_tool\_config\_params

<a id="qca.managed.types.glob_tool_config_params.GlobToolConfigParams"></a>

## GlobToolConfigParams

```python
class GlobToolConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/glob_tool_config_params.py)

<a id="qca.managed.types.glob_tool_config_params.GlobToolConfigParams.enabled"></a>

#### enabled

<a id="qca.managed.types.glob_tool_config_params.GlobToolConfigParams.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.glob_tool_config_params.GlobToolConfigParams.type"></a>

#### type

<a id="qca.managed.types.glob_tool_config_params.GlobToolConfigParams.name"></a>

#### name

<a id="qca.managed.types.grep_tool_config_params"></a>

# qca.managed.types.grep\_tool\_config\_params

<a id="qca.managed.types.grep_tool_config_params.GrepToolConfigParams"></a>

## GrepToolConfigParams

```python
class GrepToolConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/grep_tool_config_params.py)

<a id="qca.managed.types.grep_tool_config_params.GrepToolConfigParams.enabled"></a>

#### enabled

<a id="qca.managed.types.grep_tool_config_params.GrepToolConfigParams.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.grep_tool_config_params.GrepToolConfigParams.type"></a>

#### type

<a id="qca.managed.types.grep_tool_config_params.GrepToolConfigParams.name"></a>

#### name

<a id="qca.managed.types.image_block_param"></a>

# qca.managed.types.image\_block\_param

<a id="qca.managed.types.image_block_param.ImageBlockParam"></a>

## ImageBlockParam

```python
class ImageBlockParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/image_block_param.py)

<a id="qca.managed.types.image_block_param.ImageBlockParam.source"></a>

#### source

<a id="qca.managed.types.image_block_param.ImageBlockParam.type"></a>

#### type

<a id="qca.managed.types.injection_location_params"></a>

# qca.managed.types.injection\_location\_params

<a id="qca.managed.types.injection_location_params.InjectionLocationParams"></a>

## InjectionLocationParams

```python
class InjectionLocationParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/injection_location_params.py)

<a id="qca.managed.types.injection_location_params.InjectionLocationParams.body"></a>

#### body

<a id="qca.managed.types.injection_location_params.InjectionLocationParams.header"></a>

#### header

<a id="qca.managed.types.injection_location_response"></a>

# qca.managed.types.injection\_location\_response

<a id="qca.managed.types.injection_location_response.InjectionLocationResponse"></a>

## InjectionLocationResponse

```python
class InjectionLocationResponse(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/injection_location_response.py)

<a id="qca.managed.types.injection_location_response.InjectionLocationResponse.body"></a>

#### body

<a id="qca.managed.types.injection_location_response.InjectionLocationResponse.header"></a>

#### header

<a id="qca.managed.types.injection_location_update_params"></a>

# qca.managed.types.injection\_location\_update\_params

<a id="qca.managed.types.injection_location_update_params.InjectionLocationUpdateParams"></a>

## InjectionLocationUpdateParams

```python
class InjectionLocationUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/injection_location_update_params.py)

<a id="qca.managed.types.injection_location_update_params.InjectionLocationUpdateParams.body"></a>

#### body

<a id="qca.managed.types.injection_location_update_params.InjectionLocationUpdateParams.header"></a>

#### header

<a id="qca.managed.types.limited_credential_networking_params"></a>

# qca.managed.types.limited\_credential\_networking\_params

<a id="qca.managed.types.limited_credential_networking_params.LimitedCredentialNetworkingParams"></a>

## LimitedCredentialNetworkingParams

```python
class LimitedCredentialNetworkingParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/limited_credential_networking_params.py)

<a id="qca.managed.types.limited_credential_networking_params.LimitedCredentialNetworkingParams.allowed_hosts"></a>

#### allowed\_hosts

<a id="qca.managed.types.limited_credential_networking_params.LimitedCredentialNetworkingParams.type"></a>

#### type

<a id="qca.managed.types.limited_network_params"></a>

# qca.managed.types.limited\_network\_params

<a id="qca.managed.types.limited_network_params.LimitedNetworkParams"></a>

## LimitedNetworkParams

```python
class LimitedNetworkParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/limited_network_params.py)

<a id="qca.managed.types.limited_network_params.LimitedNetworkParams.allow_mcp_servers"></a>

#### allow\_mcp\_servers

<a id="qca.managed.types.limited_network_params.LimitedNetworkParams.allow_package_managers"></a>

#### allow\_package\_managers

<a id="qca.managed.types.limited_network_params.LimitedNetworkParams.allowed_hosts"></a>

#### allowed\_hosts

<a id="qca.managed.types.limited_network_params.LimitedNetworkParams.type"></a>

#### type

<a id="qca.managed.types.mcp_probe"></a>

# qca.managed.types.mcp\_probe

<a id="qca.managed.types.mcp_probe.MCPProbe"></a>

## MCPProbe

```python
class MCPProbe(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcp_probe.py)

<a id="qca.managed.types.mcp_probe.MCPProbe.http_response"></a>

#### http\_response

<a id="qca.managed.types.mcp_probe.MCPProbe.method"></a>

#### method

<a id="qca.managed.types.mcp_server_url_definition"></a>

# qca.managed.types.mcp\_server\_url\_definition

<a id="qca.managed.types.mcp_server_url_definition.MCPServerURLDefinition"></a>

## MCPServerURLDefinition

```python
class MCPServerURLDefinition(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcp_server_url_definition.py)

<a id="qca.managed.types.mcp_server_url_definition.MCPServerURLDefinition.name"></a>

#### name

<a id="qca.managed.types.mcp_server_url_definition.MCPServerURLDefinition.type"></a>

#### type

<a id="qca.managed.types.mcp_server_url_definition.MCPServerURLDefinition.url"></a>

#### url

<a id="qca.managed.types.mcp_tool_config"></a>

# qca.managed.types.mcp\_tool\_config

<a id="qca.managed.types.mcp_tool_config.MCPToolConfig"></a>

## MCPToolConfig

```python
class MCPToolConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcp_tool_config.py)

<a id="qca.managed.types.mcp_tool_config.MCPToolConfig.enabled"></a>

#### enabled

<a id="qca.managed.types.mcp_tool_config.MCPToolConfig.name"></a>

#### name

<a id="qca.managed.types.mcp_tool_config.MCPToolConfig.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.mcp_tool_config_params"></a>

# qca.managed.types.mcp\_tool\_config\_params

<a id="qca.managed.types.mcp_tool_config_params.MCPToolConfigParams"></a>

## MCPToolConfigParams

```python
class MCPToolConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcp_tool_config_params.py)

<a id="qca.managed.types.mcp_tool_config_params.MCPToolConfigParams.name"></a>

#### name

<a id="qca.managed.types.mcp_tool_config_params.MCPToolConfigParams.enabled"></a>

#### enabled

<a id="qca.managed.types.mcp_tool_config_params.MCPToolConfigParams.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.mcp_tool_config_permission_policy_union"></a>

# qca.managed.types.mcp\_tool\_config\_permission\_policy\_union

<a id="qca.managed.types.mcp_tool_config_permission_policy_union.MCPToolConfigPermissionPolicyUnion"></a>

## MCPToolConfigPermissionPolicyUnion

```python
class MCPToolConfigPermissionPolicyUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcp_tool_config_permission_policy_union.py)

<a id="qca.managed.types.mcp_tool_config_permission_policy_union.MCPToolConfigPermissionPolicyUnion.type"></a>

#### type

<a id="qca.managed.types.mcp_toolset_default_config_params"></a>

# qca.managed.types.mcp\_toolset\_default\_config\_params

<a id="qca.managed.types.mcp_toolset_default_config_params.MCPToolsetDefaultConfigParams"></a>

## MCPToolsetDefaultConfigParams

```python
class MCPToolsetDefaultConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcp_toolset_default_config_params.py)

<a id="qca.managed.types.mcp_toolset_default_config_params.MCPToolsetDefaultConfigParams.enabled"></a>

#### enabled

<a id="qca.managed.types.mcp_toolset_default_config_params.MCPToolsetDefaultConfigParams.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.mcp_toolset_params"></a>

# qca.managed.types.mcp\_toolset\_params

<a id="qca.managed.types.mcp_toolset_params.MCPToolsetParams"></a>

## MCPToolsetParams

```python
class MCPToolsetParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcp_toolset_params.py)

<a id="qca.managed.types.mcp_toolset_params.MCPToolsetParams.mcp_server_name"></a>

#### mcp\_server\_name

<a id="qca.managed.types.mcp_toolset_params.MCPToolsetParams.type"></a>

#### type

<a id="qca.managed.types.mcp_toolset_params.MCPToolsetParams.configs"></a>

#### configs

<a id="qca.managed.types.mcp_toolset_params.MCPToolsetParams.default_config"></a>

#### default\_config

<a id="qca.managed.types.mcpo_auth_create_params"></a>

# qca.managed.types.mcpo\_auth\_create\_params

<a id="qca.managed.types.mcpo_auth_create_params.MCPOAuthCreateParams"></a>

## MCPOAuthCreateParams

```python
class MCPOAuthCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcpo_auth_create_params.py)

<a id="qca.managed.types.mcpo_auth_create_params.MCPOAuthCreateParams.access_token"></a>

#### access\_token

<a id="qca.managed.types.mcpo_auth_create_params.MCPOAuthCreateParams.mcp_server_url"></a>

#### mcp\_server\_url

<a id="qca.managed.types.mcpo_auth_create_params.MCPOAuthCreateParams.type"></a>

#### type

<a id="qca.managed.types.mcpo_auth_create_params.MCPOAuthCreateParams.expires_at"></a>

#### expires\_at

<a id="qca.managed.types.mcpo_auth_create_params.MCPOAuthCreateParams.refresh"></a>

#### refresh

<a id="qca.managed.types.mcpo_auth_refresh_params"></a>

# qca.managed.types.mcpo\_auth\_refresh\_params

<a id="qca.managed.types.mcpo_auth_refresh_params.MCPOAuthRefreshParams"></a>

## MCPOAuthRefreshParams

```python
class MCPOAuthRefreshParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcpo_auth_refresh_params.py)

<a id="qca.managed.types.mcpo_auth_refresh_params.MCPOAuthRefreshParams.client_id"></a>

#### client\_id

<a id="qca.managed.types.mcpo_auth_refresh_params.MCPOAuthRefreshParams.refresh_token"></a>

#### refresh\_token

<a id="qca.managed.types.mcpo_auth_refresh_params.MCPOAuthRefreshParams.token_endpoint"></a>

#### token\_endpoint

<a id="qca.managed.types.mcpo_auth_refresh_params.MCPOAuthRefreshParams.token_endpoint_auth"></a>

#### token\_endpoint\_auth

<a id="qca.managed.types.mcpo_auth_refresh_params.MCPOAuthRefreshParams.resource"></a>

#### resource

<a id="qca.managed.types.mcpo_auth_refresh_params.MCPOAuthRefreshParams.scope"></a>

#### scope

<a id="qca.managed.types.mcpo_auth_refresh_response"></a>

# qca.managed.types.mcpo\_auth\_refresh\_response

<a id="qca.managed.types.mcpo_auth_refresh_response.MCPOAuthRefreshResponse"></a>

## MCPOAuthRefreshResponse

```python
class MCPOAuthRefreshResponse(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcpo_auth_refresh_response.py)

<a id="qca.managed.types.mcpo_auth_refresh_response.MCPOAuthRefreshResponse.client_id"></a>

#### client\_id

<a id="qca.managed.types.mcpo_auth_refresh_response.MCPOAuthRefreshResponse.token_endpoint"></a>

#### token\_endpoint

<a id="qca.managed.types.mcpo_auth_refresh_response.MCPOAuthRefreshResponse.token_endpoint_auth"></a>

#### token\_endpoint\_auth

<a id="qca.managed.types.mcpo_auth_refresh_response.MCPOAuthRefreshResponse.resource"></a>

#### resource

<a id="qca.managed.types.mcpo_auth_refresh_response.MCPOAuthRefreshResponse.scope"></a>

#### scope

<a id="qca.managed.types.mcpo_auth_refresh_response_token_endpoint_auth_union"></a>

# qca.managed.types.mcpo\_auth\_refresh\_response\_token\_endpoint\_auth\_union

<a id="qca.managed.types.mcpo_auth_refresh_response_token_endpoint_auth_union.MCPOAuthRefreshResponseTokenEndpointAuthUnion"></a>

## MCPOAuthRefreshResponseTokenEndpointAuthUnion

```python
class MCPOAuthRefreshResponseTokenEndpointAuthUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcpo_auth_refresh_response_token_endpoint_auth_union.py)

<a id="qca.managed.types.mcpo_auth_refresh_response_token_endpoint_auth_union.MCPOAuthRefreshResponseTokenEndpointAuthUnion.type"></a>

#### type

<a id="qca.managed.types.mcpo_auth_refresh_update_params"></a>

# qca.managed.types.mcpo\_auth\_refresh\_update\_params

<a id="qca.managed.types.mcpo_auth_refresh_update_params.MCPOAuthRefreshUpdateParams"></a>

## MCPOAuthRefreshUpdateParams

```python
class MCPOAuthRefreshUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcpo_auth_refresh_update_params.py)

<a id="qca.managed.types.mcpo_auth_refresh_update_params.MCPOAuthRefreshUpdateParams.refresh_token"></a>

#### refresh\_token

<a id="qca.managed.types.mcpo_auth_refresh_update_params.MCPOAuthRefreshUpdateParams.scope"></a>

#### scope

<a id="qca.managed.types.mcpo_auth_refresh_update_params.MCPOAuthRefreshUpdateParams.token_endpoint_auth"></a>

#### token\_endpoint\_auth

<a id="qca.managed.types.mcpo_auth_update_params"></a>

# qca.managed.types.mcpo\_auth\_update\_params

<a id="qca.managed.types.mcpo_auth_update_params.MCPOAuthUpdateParams"></a>

## MCPOAuthUpdateParams

```python
class MCPOAuthUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/mcpo_auth_update_params.py)

<a id="qca.managed.types.mcpo_auth_update_params.MCPOAuthUpdateParams.type"></a>

#### type

<a id="qca.managed.types.mcpo_auth_update_params.MCPOAuthUpdateParams.access_token"></a>

#### access\_token

<a id="qca.managed.types.mcpo_auth_update_params.MCPOAuthUpdateParams.expires_at"></a>

#### expires\_at

<a id="qca.managed.types.mcpo_auth_update_params.MCPOAuthUpdateParams.refresh"></a>

#### refresh

<a id="qca.managed.types.memory"></a>

# qca.managed.types.memory

<a id="qca.managed.types.memory.Memory"></a>

## Memory

```python
class Memory(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory.py)

<a id="qca.managed.types.memory.Memory.metadata"></a>

#### metadata

<a id="qca.managed.types.memory.Memory.id"></a>

#### id

<a id="qca.managed.types.memory.Memory.content_sha256"></a>

#### content\_sha256

<a id="qca.managed.types.memory.Memory.content_size_bytes"></a>

#### content\_size\_bytes

<a id="qca.managed.types.memory.Memory.created_at"></a>

#### created\_at

<a id="qca.managed.types.memory.Memory.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.memory.Memory.memory_version_id"></a>

#### memory\_version\_id

<a id="qca.managed.types.memory.Memory.path"></a>

#### path

<a id="qca.managed.types.memory.Memory.type"></a>

#### type

<a id="qca.managed.types.memory.Memory.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.memory.Memory.content"></a>

#### content

<a id="qca.managed.types.memory_list_item_union"></a>

# qca.managed.types.memory\_list\_item\_union

<a id="qca.managed.types.memory_list_item_union.MemoryListItemUnion"></a>

## MemoryListItemUnion

```python
class MemoryListItemUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_list_item_union.py)

<a id="qca.managed.types.memory_list_item_union.MemoryListItemUnion.id"></a>

#### id

<a id="qca.managed.types.memory_list_item_union.MemoryListItemUnion.content_sha256"></a>

#### content\_sha256

<a id="qca.managed.types.memory_list_item_union.MemoryListItemUnion.content_size_bytes"></a>

#### content\_size\_bytes

<a id="qca.managed.types.memory_list_item_union.MemoryListItemUnion.created_at"></a>

#### created\_at

<a id="qca.managed.types.memory_list_item_union.MemoryListItemUnion.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.memory_list_item_union.MemoryListItemUnion.memory_version_id"></a>

#### memory\_version\_id

<a id="qca.managed.types.memory_list_item_union.MemoryListItemUnion.path"></a>

#### path

<a id="qca.managed.types.memory_list_item_union.MemoryListItemUnion.type"></a>

#### type

<a id="qca.managed.types.memory_list_item_union.MemoryListItemUnion.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.memory_list_item_union.MemoryListItemUnion.content"></a>

#### content

<a id="qca.managed.types.memory_store"></a>

# qca.managed.types.memory\_store

<a id="qca.managed.types.memory_store.MemoryStore"></a>

## MemoryStore

```python
class MemoryStore(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store.py)

<a id="qca.managed.types.memory_store.MemoryStore.id"></a>

#### id

<a id="qca.managed.types.memory_store.MemoryStore.created_at"></a>

#### created\_at

<a id="qca.managed.types.memory_store.MemoryStore.name"></a>

#### name

<a id="qca.managed.types.memory_store.MemoryStore.type"></a>

#### type

<a id="qca.managed.types.memory_store.MemoryStore.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.memory_store.MemoryStore.archived_at"></a>

#### archived\_at

<a id="qca.managed.types.memory_store.MemoryStore.description"></a>

#### description

<a id="qca.managed.types.memory_store.MemoryStore.metadata"></a>

#### metadata

<a id="qca.managed.types.memory_store_archive_params"></a>

# qca.managed.types.memory\_store\_archive\_params

<a id="qca.managed.types.memory_store_archive_params.MemoryStoreArchiveParams"></a>

## MemoryStoreArchiveParams

```python
class MemoryStoreArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_archive_params.py)

<a id="qca.managed.types.memory_store_archive_params.MemoryStoreArchiveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_archive_params.MemoryStoreArchiveParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_create_params"></a>

# qca.managed.types.memory\_store\_create\_params

<a id="qca.managed.types.memory_store_create_params.MemoryStoreCreateParams"></a>

## MemoryStoreCreateParams

```python
class MemoryStoreCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_create_params.py)

<a id="qca.managed.types.memory_store_create_params.MemoryStoreCreateParams.name"></a>

#### name

<a id="qca.managed.types.memory_store_create_params.MemoryStoreCreateParams.description"></a>

#### description

<a id="qca.managed.types.memory_store_create_params.MemoryStoreCreateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_create_params.MemoryStoreCreateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.memory_store_create_params.MemoryStoreCreateParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_delete_params"></a>

# qca.managed.types.memory\_store\_delete\_params

<a id="qca.managed.types.memory_store_delete_params.MemoryStoreDeleteParams"></a>

## MemoryStoreDeleteParams

```python
class MemoryStoreDeleteParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_delete_params.py)

<a id="qca.managed.types.memory_store_delete_params.MemoryStoreDeleteParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_delete_params.MemoryStoreDeleteParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_list_params"></a>

# qca.managed.types.memory\_store\_list\_params

<a id="qca.managed.types.memory_store_list_params.MemoryStoreListParams"></a>

## MemoryStoreListParams

```python
class MemoryStoreListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_list_params.py)

<a id="qca.managed.types.memory_store_list_params.MemoryStoreListParams.name"></a>

#### name

<a id="qca.managed.types.memory_store_list_params.MemoryStoreListParams.created_at_gte"></a>

#### created\_at\_gte

<a id="qca.managed.types.memory_store_list_params.MemoryStoreListParams.created_at_lte"></a>

#### created\_at\_lte

<a id="qca.managed.types.memory_store_list_params.MemoryStoreListParams.include_archived"></a>

#### include\_archived

<a id="qca.managed.types.memory_store_list_params.MemoryStoreListParams.limit"></a>

#### limit

<a id="qca.managed.types.memory_store_list_params.MemoryStoreListParams.page"></a>

#### page

<a id="qca.managed.types.memory_store_list_params.MemoryStoreListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_list_params.MemoryStoreListParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_memory_create_params"></a>

# qca.managed.types.memory\_store\_memory\_create\_params

<a id="qca.managed.types.memory_store_memory_create_params.MemoryStoreMemoryCreateParams"></a>

## MemoryStoreMemoryCreateParams

```python
class MemoryStoreMemoryCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_memory_create_params.py)

<a id="qca.managed.types.memory_store_memory_create_params.MemoryStoreMemoryCreateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.memory_store_memory_create_params.MemoryStoreMemoryCreateParams.content"></a>

#### content

<a id="qca.managed.types.memory_store_memory_create_params.MemoryStoreMemoryCreateParams.path"></a>

#### path

<a id="qca.managed.types.memory_store_memory_create_params.MemoryStoreMemoryCreateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_memory_create_params.MemoryStoreMemoryCreateParams.view"></a>

#### view

<a id="qca.managed.types.memory_store_memory_create_params.MemoryStoreMemoryCreateParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_memory_delete_params"></a>

# qca.managed.types.memory\_store\_memory\_delete\_params

<a id="qca.managed.types.memory_store_memory_delete_params.MemoryStoreMemoryDeleteParams"></a>

## MemoryStoreMemoryDeleteParams

```python
class MemoryStoreMemoryDeleteParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_memory_delete_params.py)

<a id="qca.managed.types.memory_store_memory_delete_params.MemoryStoreMemoryDeleteParams.expected_content_sha256"></a>

#### expected\_content\_sha256

<a id="qca.managed.types.memory_store_memory_delete_params.MemoryStoreMemoryDeleteParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_memory_delete_params.MemoryStoreMemoryDeleteParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_memory_list_params"></a>

# qca.managed.types.memory\_store\_memory\_list\_params

<a id="qca.managed.types.memory_store_memory_list_params.MemoryStoreMemoryListParams"></a>

## MemoryStoreMemoryListParams

```python
class MemoryStoreMemoryListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_memory_list_params.py)

<a id="qca.managed.types.memory_store_memory_list_params.MemoryStoreMemoryListParams.depth"></a>

#### depth

<a id="qca.managed.types.memory_store_memory_list_params.MemoryStoreMemoryListParams.limit"></a>

#### limit

<a id="qca.managed.types.memory_store_memory_list_params.MemoryStoreMemoryListParams.page"></a>

#### page

<a id="qca.managed.types.memory_store_memory_list_params.MemoryStoreMemoryListParams.path_prefix"></a>

#### path\_prefix

<a id="qca.managed.types.memory_store_memory_list_params.MemoryStoreMemoryListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_memory_list_params.MemoryStoreMemoryListParams.view"></a>

#### view

<a id="qca.managed.types.memory_store_memory_list_params.MemoryStoreMemoryListParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_memory_retrieve_params"></a>

# qca.managed.types.memory\_store\_memory\_retrieve\_params

<a id="qca.managed.types.memory_store_memory_retrieve_params.MemoryStoreMemoryRetrieveParams"></a>

## MemoryStoreMemoryRetrieveParams

```python
class MemoryStoreMemoryRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_memory_retrieve_params.py)

<a id="qca.managed.types.memory_store_memory_retrieve_params.MemoryStoreMemoryRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_memory_retrieve_params.MemoryStoreMemoryRetrieveParams.view"></a>

#### view

<a id="qca.managed.types.memory_store_memory_retrieve_params.MemoryStoreMemoryRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_memory_update_params"></a>

# qca.managed.types.memory\_store\_memory\_update\_params

<a id="qca.managed.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams"></a>

## MemoryStoreMemoryUpdateParams

```python
class MemoryStoreMemoryUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_memory_update_params.py)

<a id="qca.managed.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams.content_sha256"></a>

#### content\_sha256

<a id="qca.managed.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams.content"></a>

#### content

<a id="qca.managed.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams.path"></a>

#### path

<a id="qca.managed.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams.view"></a>

#### view

<a id="qca.managed.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams.precondition"></a>

#### precondition

<a id="qca.managed.types.memory_store_memory_update_params.MemoryStoreMemoryUpdateParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_memory_version_list_params"></a>

# qca.managed.types.memory\_store\_memory\_version\_list\_params

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams"></a>

## MemoryStoreMemoryVersionListParams

```python
class MemoryStoreMemoryVersionListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_memory_version_list_params.py)

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.api_key_id"></a>

#### api\_key\_id

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.created_at_gte"></a>

#### created\_at\_gte

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.created_at_lte"></a>

#### created\_at\_lte

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.limit"></a>

#### limit

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.memory_id"></a>

#### memory\_id

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.page"></a>

#### page

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.service_account_id"></a>

#### service\_account\_id

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.session_id"></a>

#### session\_id

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.operation"></a>

#### operation

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.view"></a>

#### view

<a id="qca.managed.types.memory_store_memory_version_list_params.MemoryStoreMemoryVersionListParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_memory_version_redact_params"></a>

# qca.managed.types.memory\_store\_memory\_version\_redact\_params

<a id="qca.managed.types.memory_store_memory_version_redact_params.MemoryStoreMemoryVersionRedactParams"></a>

## MemoryStoreMemoryVersionRedactParams

```python
class MemoryStoreMemoryVersionRedactParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_memory_version_redact_params.py)

<a id="qca.managed.types.memory_store_memory_version_redact_params.MemoryStoreMemoryVersionRedactParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_memory_version_redact_params.MemoryStoreMemoryVersionRedactParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_memory_version_retrieve_params"></a>

# qca.managed.types.memory\_store\_memory\_version\_retrieve\_params

<a id="qca.managed.types.memory_store_memory_version_retrieve_params.MemoryStoreMemoryVersionRetrieveParams"></a>

## MemoryStoreMemoryVersionRetrieveParams

```python
class MemoryStoreMemoryVersionRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_memory_version_retrieve_params.py)

<a id="qca.managed.types.memory_store_memory_version_retrieve_params.MemoryStoreMemoryVersionRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_memory_version_retrieve_params.MemoryStoreMemoryVersionRetrieveParams.view"></a>

#### view

<a id="qca.managed.types.memory_store_memory_version_retrieve_params.MemoryStoreMemoryVersionRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_resource_param"></a>

# qca.managed.types.memory\_store\_resource\_param

<a id="qca.managed.types.memory_store_resource_param.MemoryStoreResourceParam"></a>

## MemoryStoreResourceParam

```python
class MemoryStoreResourceParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_resource_param.py)

<a id="qca.managed.types.memory_store_resource_param.MemoryStoreResourceParam.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.memory_store_resource_param.MemoryStoreResourceParam.type"></a>

#### type

<a id="qca.managed.types.memory_store_resource_param.MemoryStoreResourceParam.instructions"></a>

#### instructions

<a id="qca.managed.types.memory_store_resource_param.MemoryStoreResourceParam.access"></a>

#### access

<a id="qca.managed.types.memory_store_retrieve_params"></a>

# qca.managed.types.memory\_store\_retrieve\_params

<a id="qca.managed.types.memory_store_retrieve_params.MemoryStoreRetrieveParams"></a>

## MemoryStoreRetrieveParams

```python
class MemoryStoreRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_retrieve_params.py)

<a id="qca.managed.types.memory_store_retrieve_params.MemoryStoreRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_retrieve_params.MemoryStoreRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_store_update_params"></a>

# qca.managed.types.memory\_store\_update\_params

<a id="qca.managed.types.memory_store_update_params.MemoryStoreUpdateParams"></a>

## MemoryStoreUpdateParams

```python
class MemoryStoreUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_store_update_params.py)

<a id="qca.managed.types.memory_store_update_params.MemoryStoreUpdateParams.description"></a>

#### description

<a id="qca.managed.types.memory_store_update_params.MemoryStoreUpdateParams.name"></a>

#### name

<a id="qca.managed.types.memory_store_update_params.MemoryStoreUpdateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.memory_store_update_params.MemoryStoreUpdateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.memory_store_update_params.MemoryStoreUpdateParams.betas"></a>

#### betas

<a id="qca.managed.types.memory_version"></a>

# qca.managed.types.memory\_version

<a id="qca.managed.types.memory_version.MemoryVersion"></a>

## MemoryVersion

```python
class MemoryVersion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/memory_version.py)

<a id="qca.managed.types.memory_version.MemoryVersion.id"></a>

#### id

<a id="qca.managed.types.memory_version.MemoryVersion.created_at"></a>

#### created\_at

<a id="qca.managed.types.memory_version.MemoryVersion.memory_id"></a>

#### memory\_id

<a id="qca.managed.types.memory_version.MemoryVersion.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.memory_version.MemoryVersion.operation"></a>

#### operation

<a id="qca.managed.types.memory_version.MemoryVersion.type"></a>

#### type

<a id="qca.managed.types.memory_version.MemoryVersion.content"></a>

#### content

<a id="qca.managed.types.memory_version.MemoryVersion.content_sha256"></a>

#### content\_sha256

<a id="qca.managed.types.memory_version.MemoryVersion.content_size_bytes"></a>

#### content\_size\_bytes

<a id="qca.managed.types.memory_version.MemoryVersion.created_by"></a>

#### created\_by

<a id="qca.managed.types.memory_version.MemoryVersion.path"></a>

#### path

<a id="qca.managed.types.memory_version.MemoryVersion.redacted_at"></a>

#### redacted\_at

<a id="qca.managed.types.memory_version.MemoryVersion.redacted_by"></a>

#### redacted\_by

<a id="qca.managed.types.model_capabilities"></a>

# qca.managed.types.model\_capabilities

<a id="qca.managed.types.model_capabilities.ModelCapabilities"></a>

## ModelCapabilities

```python
class ModelCapabilities(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/model_capabilities.py)

<a id="qca.managed.types.model_capabilities.ModelCapabilities.batch"></a>

#### batch

<a id="qca.managed.types.model_capabilities.ModelCapabilities.citations"></a>

#### citations

<a id="qca.managed.types.model_capabilities.ModelCapabilities.code_execution"></a>

#### code\_execution

<a id="qca.managed.types.model_capabilities.ModelCapabilities.context_management"></a>

#### context\_management

<a id="qca.managed.types.model_capabilities.ModelCapabilities.effort"></a>

#### effort

<a id="qca.managed.types.model_capabilities.ModelCapabilities.image_input"></a>

#### image\_input

<a id="qca.managed.types.model_capabilities.ModelCapabilities.pdf_input"></a>

#### pdf\_input

<a id="qca.managed.types.model_capabilities.ModelCapabilities.structured_outputs"></a>

#### structured\_outputs

<a id="qca.managed.types.model_capabilities.ModelCapabilities.thinking"></a>

#### thinking

<a id="qca.managed.types.model_config"></a>

# qca.managed.types.model\_config

<a id="qca.managed.types.model_config.ModelConfig"></a>

## ModelConfig

```python
class ModelConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/model_config.py)

<a id="qca.managed.types.model_config.ModelConfig.context_window"></a>

#### context\_window

<a id="qca.managed.types.model_config.ModelConfig.id"></a>

#### id

<a id="qca.managed.types.model_config.ModelConfig.effort"></a>

#### effort

<a id="qca.managed.types.model_config.ModelConfig.inference_geo"></a>

#### inference\_geo

<a id="qca.managed.types.model_config.ModelConfig.speed"></a>

#### speed

<a id="qca.managed.types.model_config_effort_union"></a>

# qca.managed.types.model\_config\_effort\_union

<a id="qca.managed.types.model_config_effort_union.ModelConfigEffortUnion"></a>

## ModelConfigEffortUnion

```python
class ModelConfigEffortUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/model_config_effort_union.py)

<a id="qca.managed.types.model_config_effort_union.ModelConfigEffortUnion.type"></a>

#### type

<a id="qca.managed.types.model_config_params"></a>

# qca.managed.types.model\_config\_params

<a id="qca.managed.types.model_config_params.ModelConfigParams"></a>

## ModelConfigParams

```python
class ModelConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/model_config_params.py)

<a id="qca.managed.types.model_config_params.ModelConfigParams.context_window"></a>

#### context\_window

<a id="qca.managed.types.model_config_params.ModelConfigParams.id"></a>

#### id

<a id="qca.managed.types.model_config_params.ModelConfigParams.inference_geo"></a>

#### inference\_geo

<a id="qca.managed.types.model_config_params.ModelConfigParams.effort"></a>

#### effort

<a id="qca.managed.types.model_config_params.ModelConfigParams.speed"></a>

#### speed

<a id="qca.managed.types.model_info"></a>

# qca.managed.types.model\_info

<a id="qca.managed.types.model_info.ModelInfo"></a>

## ModelInfo

```python
class ModelInfo(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/model_info.py)

<a id="qca.managed.types.model_info.ModelInfo.source"></a>

#### source

<a id="qca.managed.types.model_info.ModelInfo.is_enabled"></a>

#### is\_enabled

<a id="qca.managed.types.model_info.ModelInfo.is_new"></a>

#### is\_new

<a id="qca.managed.types.model_info.ModelInfo.price_factor"></a>

#### price\_factor

<a id="qca.managed.types.model_info.ModelInfo.efforts"></a>

#### efforts

<a id="qca.managed.types.model_info.ModelInfo.default_effort"></a>

#### default\_effort

<a id="qca.managed.types.model_info.ModelInfo.default_context_window"></a>

#### default\_context\_window

<a id="qca.managed.types.model_info.ModelInfo.available_context_windows"></a>

#### available\_context\_windows

<a id="qca.managed.types.model_info.ModelInfo.id"></a>

#### id

<a id="qca.managed.types.model_info.ModelInfo.allowed_fallback_models"></a>

#### allowed\_fallback\_models

<a id="qca.managed.types.model_info.ModelInfo.capabilities"></a>

#### capabilities

<a id="qca.managed.types.model_info.ModelInfo.created_at"></a>

#### created\_at

<a id="qca.managed.types.model_info.ModelInfo.display_name"></a>

#### display\_name

<a id="qca.managed.types.model_info.ModelInfo.max_input_tokens"></a>

#### max\_input\_tokens

<a id="qca.managed.types.model_info.ModelInfo.max_tokens"></a>

#### max\_tokens

<a id="qca.managed.types.model_info.ModelInfo.type"></a>

#### type

<a id="qca.managed.types.model_list_params"></a>

# qca.managed.types.model\_list\_params

<a id="qca.managed.types.model_list_params.ModelListParams"></a>

## ModelListParams

```python
class ModelListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/model_list_params.py)

<a id="qca.managed.types.model_list_params.ModelListParams.after_id"></a>

#### after\_id

<a id="qca.managed.types.model_list_params.ModelListParams.before_id"></a>

#### before\_id

<a id="qca.managed.types.model_list_params.ModelListParams.limit"></a>

#### limit

<a id="qca.managed.types.model_list_params.ModelListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.model_list_params.ModelListParams.betas"></a>

#### betas

<a id="qca.managed.types.monetary_amount"></a>

# qca.managed.types.monetary\_amount

<a id="qca.managed.types.monetary_amount.MonetaryAmount"></a>

## MonetaryAmount

```python
class MonetaryAmount(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/monetary_amount.py)

<a id="qca.managed.types.monetary_amount.MonetaryAmount.amount"></a>

#### amount

<a id="qca.managed.types.monetary_amount.MonetaryAmount.currency"></a>

#### currency

<a id="qca.managed.types.monetary_amount_param"></a>

# qca.managed.types.monetary\_amount\_param

<a id="qca.managed.types.monetary_amount_param.MonetaryAmountParam"></a>

## MonetaryAmountParam

```python
class MonetaryAmountParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/monetary_amount_param.py)

<a id="qca.managed.types.monetary_amount_param.MonetaryAmountParam.amount"></a>

#### amount

<a id="qca.managed.types.monetary_amount_param.MonetaryAmountParam.currency"></a>

#### currency

<a id="qca.managed.types.multiagent"></a>

# qca.managed.types.multiagent

<a id="qca.managed.types.multiagent.Multiagent"></a>

## Multiagent

```python
class Multiagent(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/multiagent.py)

<a id="qca.managed.types.multiagent.Multiagent.agents"></a>

#### agents

<a id="qca.managed.types.multiagent.Multiagent.type"></a>

#### type

<a id="qca.managed.types.multiagent_agent_union"></a>

# qca.managed.types.multiagent\_agent\_union

<a id="qca.managed.types.multiagent_agent_union.MultiagentAgentUnion"></a>

## MultiagentAgentUnion

```python
class MultiagentAgentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/multiagent_agent_union.py)

<a id="qca.managed.types.multiagent_agent_union.MultiagentAgentUnion.id"></a>

#### id

<a id="qca.managed.types.multiagent_agent_union.MultiagentAgentUnion.type"></a>

#### type

<a id="qca.managed.types.multiagent_agent_union.MultiagentAgentUnion.version"></a>

#### version

<a id="qca.managed.types.multiagent_agent_union.MultiagentAgentUnion.model"></a>

#### model

<a id="qca.managed.types.multiagent_params"></a>

# qca.managed.types.multiagent\_params

<a id="qca.managed.types.multiagent_params.MultiagentParams"></a>

## MultiagentParams

```python
class MultiagentParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/multiagent_params.py)

<a id="qca.managed.types.multiagent_params.MultiagentParams.agents"></a>

#### agents

<a id="qca.managed.types.multiagent_params.MultiagentParams.type"></a>

#### type

<a id="qca.managed.types.multiagent_self_params"></a>

# qca.managed.types.multiagent\_self\_params

<a id="qca.managed.types.multiagent_self_params.MultiagentSelfParams"></a>

## MultiagentSelfParams

```python
class MultiagentSelfParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/multiagent_self_params.py)

<a id="qca.managed.types.multiagent_self_params.MultiagentSelfParams.type"></a>

#### type

<a id="qca.managed.types.outcome_evaluation_resource"></a>

# qca.managed.types.outcome\_evaluation\_resource

<a id="qca.managed.types.outcome_evaluation_resource.OutcomeEvaluationResource"></a>

## OutcomeEvaluationResource

```python
class OutcomeEvaluationResource(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/outcome_evaluation_resource.py)

<a id="qca.managed.types.outcome_evaluation_resource.OutcomeEvaluationResource.completed_at"></a>

#### completed\_at

<a id="qca.managed.types.outcome_evaluation_resource.OutcomeEvaluationResource.description"></a>

#### description

<a id="qca.managed.types.outcome_evaluation_resource.OutcomeEvaluationResource.explanation"></a>

#### explanation

<a id="qca.managed.types.outcome_evaluation_resource.OutcomeEvaluationResource.iteration"></a>

#### iteration

<a id="qca.managed.types.outcome_evaluation_resource.OutcomeEvaluationResource.outcome_id"></a>

#### outcome\_id

<a id="qca.managed.types.outcome_evaluation_resource.OutcomeEvaluationResource.result"></a>

#### result

<a id="qca.managed.types.outcome_evaluation_resource.OutcomeEvaluationResource.type"></a>

#### type

<a id="qca.managed.types.output_behavior_create_new_param"></a>

# qca.managed.types.output\_behavior\_create\_new\_param

<a id="qca.managed.types.output_behavior_create_new_param.OutputBehaviorCreateNewParam"></a>

## OutputBehaviorCreateNewParam

```python
class OutputBehaviorCreateNewParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/output_behavior_create_new_param.py)

<a id="qca.managed.types.output_behavior_create_new_param.OutputBehaviorCreateNewParam.type"></a>

#### type

<a id="qca.managed.types.output_behavior_union"></a>

# qca.managed.types.output\_behavior\_union

<a id="qca.managed.types.output_behavior_union.OutputBehaviorUnion"></a>

## OutputBehaviorUnion

```python
class OutputBehaviorUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/output_behavior_union.py)

<a id="qca.managed.types.output_behavior_union.OutputBehaviorUnion.type"></a>

#### type

<a id="qca.managed.types.output_behavior_union.OutputBehaviorUnion.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.output_behavior_update_existing_param"></a>

# qca.managed.types.output\_behavior\_update\_existing\_param

<a id="qca.managed.types.output_behavior_update_existing_param.OutputBehaviorUpdateExistingParam"></a>

## OutputBehaviorUpdateExistingParam

```python
class OutputBehaviorUpdateExistingParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/output_behavior_update_existing_param.py)

<a id="qca.managed.types.output_behavior_update_existing_param.OutputBehaviorUpdateExistingParam.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.output_behavior_update_existing_param.OutputBehaviorUpdateExistingParam.type"></a>

#### type

<a id="qca.managed.types.packages"></a>

# qca.managed.types.packages

<a id="qca.managed.types.packages.Packages"></a>

## Packages

```python
class Packages(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/packages.py)

<a id="qca.managed.types.packages.Packages.apt"></a>

#### apt

<a id="qca.managed.types.packages.Packages.cargo"></a>

#### cargo

<a id="qca.managed.types.packages.Packages.gem"></a>

#### gem

<a id="qca.managed.types.packages.Packages.go"></a>

#### go

<a id="qca.managed.types.packages.Packages.npm"></a>

#### npm

<a id="qca.managed.types.packages.Packages.pip"></a>

#### pip

<a id="qca.managed.types.packages.Packages.type"></a>

#### type

<a id="qca.managed.types.packages_params"></a>

# qca.managed.types.packages\_params

<a id="qca.managed.types.packages_params.PackagesParams"></a>

## PackagesParams

```python
class PackagesParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/packages_params.py)

<a id="qca.managed.types.packages_params.PackagesParams.apt"></a>

#### apt

<a id="qca.managed.types.packages_params.PackagesParams.cargo"></a>

#### cargo

<a id="qca.managed.types.packages_params.PackagesParams.gem"></a>

#### gem

<a id="qca.managed.types.packages_params.PackagesParams.go"></a>

#### go

<a id="qca.managed.types.packages_params.PackagesParams.npm"></a>

#### npm

<a id="qca.managed.types.packages_params.PackagesParams.pip"></a>

#### pip

<a id="qca.managed.types.packages_params.PackagesParams.type"></a>

#### type

<a id="qca.managed.types.plain_text_document_source_param"></a>

# qca.managed.types.plain\_text\_document\_source\_param

<a id="qca.managed.types.plain_text_document_source_param.PlainTextDocumentSourceParam"></a>

## PlainTextDocumentSourceParam

```python
class PlainTextDocumentSourceParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/plain_text_document_source_param.py)

<a id="qca.managed.types.plain_text_document_source_param.PlainTextDocumentSourceParam.data"></a>

#### data

<a id="qca.managed.types.plain_text_document_source_param.PlainTextDocumentSourceParam.media_type"></a>

#### media\_type

<a id="qca.managed.types.plain_text_document_source_param.PlainTextDocumentSourceParam.type"></a>

#### type

<a id="qca.managed.types.precondition_param"></a>

# qca.managed.types.precondition\_param

<a id="qca.managed.types.precondition_param.PreconditionParam"></a>

## PreconditionParam

```python
class PreconditionParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/precondition_param.py)

<a id="qca.managed.types.precondition_param.PreconditionParam.type"></a>

#### type

<a id="qca.managed.types.precondition_param.PreconditionParam.content_sha256"></a>

#### content\_sha256

<a id="qca.managed.types.qoder_skill_params"></a>

# qca.managed.types.qoder\_skill\_params

<a id="qca.managed.types.qoder_skill_params.QoderSkillParams"></a>

## QoderSkillParams

```python
class QoderSkillParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/qoder_skill_params.py)

<a id="qca.managed.types.qoder_skill_params.QoderSkillParams.skill_id"></a>

#### skill\_id

<a id="qca.managed.types.qoder_skill_params.QoderSkillParams.type"></a>

#### type

<a id="qca.managed.types.qoder_skill_params.QoderSkillParams.version"></a>

#### version

<a id="qca.managed.types.read_tool_config_params"></a>

# qca.managed.types.read\_tool\_config\_params

<a id="qca.managed.types.read_tool_config_params.ReadToolConfigParams"></a>

## ReadToolConfigParams

```python
class ReadToolConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/read_tool_config_params.py)

<a id="qca.managed.types.read_tool_config_params.ReadToolConfigParams.enabled"></a>

#### enabled

<a id="qca.managed.types.read_tool_config_params.ReadToolConfigParams.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.read_tool_config_params.ReadToolConfigParams.type"></a>

#### type

<a id="qca.managed.types.read_tool_config_params.ReadToolConfigParams.name"></a>

#### name

<a id="qca.managed.types.redacted_block_param"></a>

# qca.managed.types.redacted\_block\_param

<a id="qca.managed.types.redacted_block_param.RedactedBlockParam"></a>

## RedactedBlockParam

```python
class RedactedBlockParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/redacted_block_param.py)

<a id="qca.managed.types.redacted_block_param.RedactedBlockParam.type"></a>

#### type

<a id="qca.managed.types.refresh_http_response"></a>

# qca.managed.types.refresh\_http\_response

<a id="qca.managed.types.refresh_http_response.RefreshHTTPResponse"></a>

## RefreshHTTPResponse

```python
class RefreshHTTPResponse(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/refresh_http_response.py)

<a id="qca.managed.types.refresh_http_response.RefreshHTTPResponse.body"></a>

#### body

<a id="qca.managed.types.refresh_http_response.RefreshHTTPResponse.body_truncated"></a>

#### body\_truncated

<a id="qca.managed.types.refresh_http_response.RefreshHTTPResponse.content_type"></a>

#### content\_type

<a id="qca.managed.types.refresh_http_response.RefreshHTTPResponse.status_code"></a>

#### status\_code

<a id="qca.managed.types.refresh_object"></a>

# qca.managed.types.refresh\_object

<a id="qca.managed.types.refresh_object.RefreshObject"></a>

## RefreshObject

```python
class RefreshObject(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/refresh_object.py)

<a id="qca.managed.types.refresh_object.RefreshObject.http_response"></a>

#### http\_response

<a id="qca.managed.types.refresh_object.RefreshObject.status"></a>

#### status

<a id="qca.managed.types.schedule"></a>

# qca.managed.types.schedule

<a id="qca.managed.types.schedule.Schedule"></a>

## Schedule

```python
class Schedule(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/schedule.py)

<a id="qca.managed.types.schedule.Schedule.expression"></a>

#### expression

<a id="qca.managed.types.schedule.Schedule.timezone"></a>

#### timezone

<a id="qca.managed.types.schedule.Schedule.type"></a>

#### type

<a id="qca.managed.types.schedule.Schedule.last_run_at"></a>

#### last\_run\_at

<a id="qca.managed.types.schedule.Schedule.upcoming_runs_at"></a>

#### upcoming\_runs\_at

<a id="qca.managed.types.schedule_params"></a>

# qca.managed.types.schedule\_params

<a id="qca.managed.types.schedule_params.ScheduleParams"></a>

## ScheduleParams

```python
class ScheduleParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/schedule_params.py)

<a id="qca.managed.types.schedule_params.ScheduleParams.expression"></a>

#### expression

<a id="qca.managed.types.schedule_params.ScheduleParams.timezone"></a>

#### timezone

<a id="qca.managed.types.schedule_params.ScheduleParams.type"></a>

#### type

<a id="qca.managed.types.search_result_block_param"></a>

# qca.managed.types.search\_result\_block\_param

<a id="qca.managed.types.search_result_block_param.SearchResultBlockParam"></a>

## SearchResultBlockParam

```python
class SearchResultBlockParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/search_result_block_param.py)

<a id="qca.managed.types.search_result_block_param.SearchResultBlockParam.citations"></a>

#### citations

<a id="qca.managed.types.search_result_block_param.SearchResultBlockParam.content"></a>

#### content

<a id="qca.managed.types.search_result_block_param.SearchResultBlockParam.source"></a>

#### source

<a id="qca.managed.types.search_result_block_param.SearchResultBlockParam.title"></a>

#### title

<a id="qca.managed.types.search_result_block_param.SearchResultBlockParam.type"></a>

#### type

<a id="qca.managed.types.search_result_citations"></a>

# qca.managed.types.search\_result\_citations

<a id="qca.managed.types.search_result_citations.SearchResultCitations"></a>

## SearchResultCitations

```python
class SearchResultCitations(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/search_result_citations.py)

<a id="qca.managed.types.search_result_citations.SearchResultCitations.enabled"></a>

#### enabled

<a id="qca.managed.types.search_result_citations_param"></a>

# qca.managed.types.search\_result\_citations\_param

<a id="qca.managed.types.search_result_citations_param.SearchResultCitationsParam"></a>

## SearchResultCitationsParam

```python
class SearchResultCitationsParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/search_result_citations_param.py)

<a id="qca.managed.types.search_result_citations_param.SearchResultCitationsParam.enabled"></a>

#### enabled

<a id="qca.managed.types.search_result_content"></a>

# qca.managed.types.search\_result\_content

<a id="qca.managed.types.search_result_content.SearchResultContent"></a>

## SearchResultContent

```python
class SearchResultContent(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/search_result_content.py)

<a id="qca.managed.types.search_result_content.SearchResultContent.text"></a>

#### text

<a id="qca.managed.types.search_result_content.SearchResultContent.type"></a>

#### type

<a id="qca.managed.types.search_result_content_param"></a>

# qca.managed.types.search\_result\_content\_param

<a id="qca.managed.types.search_result_content_param.SearchResultContentParam"></a>

## SearchResultContentParam

```python
class SearchResultContentParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/search_result_content_param.py)

<a id="qca.managed.types.search_result_content_param.SearchResultContentParam.text"></a>

#### text

<a id="qca.managed.types.search_result_content_param.SearchResultContentParam.type"></a>

#### type

<a id="qca.managed.types.self_hosted_config_params"></a>

# qca.managed.types.self\_hosted\_config\_params

<a id="qca.managed.types.self_hosted_config_params.SelfHostedConfigParams"></a>

## SelfHostedConfigParams

```python
class SelfHostedConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/self_hosted_config_params.py)

<a id="qca.managed.types.self_hosted_config_params.SelfHostedConfigParams.type"></a>

#### type

<a id="qca.managed.types.self_hosted_work"></a>

# qca.managed.types.self\_hosted\_work

<a id="qca.managed.types.self_hosted_work.SelfHostedWork"></a>

## SelfHostedWork

```python
class SelfHostedWork(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/self_hosted_work.py)

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.id"></a>

#### id

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.acknowledged_at"></a>

#### acknowledged\_at

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.created_at"></a>

#### created\_at

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.data"></a>

#### data

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.environment_id"></a>

#### environment\_id

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.latest_heartbeat_at"></a>

#### latest\_heartbeat\_at

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.metadata"></a>

#### metadata

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.secret"></a>

#### secret

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.started_at"></a>

#### started\_at

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.state"></a>

#### state

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.stop_requested_at"></a>

#### stop\_requested\_at

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.stopped_at"></a>

#### stopped\_at

<a id="qca.managed.types.self_hosted_work.SelfHostedWork.type"></a>

#### type

<a id="qca.managed.types.self_hosted_work_heartbeat_response"></a>

# qca.managed.types.self\_hosted\_work\_heartbeat\_response

<a id="qca.managed.types.self_hosted_work_heartbeat_response.SelfHostedWorkHeartbeatResponse"></a>

## SelfHostedWorkHeartbeatResponse

```python
class SelfHostedWorkHeartbeatResponse(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/self_hosted_work_heartbeat_response.py)

<a id="qca.managed.types.self_hosted_work_heartbeat_response.SelfHostedWorkHeartbeatResponse.last_heartbeat"></a>

#### last\_heartbeat

<a id="qca.managed.types.self_hosted_work_heartbeat_response.SelfHostedWorkHeartbeatResponse.lease_extended"></a>

#### lease\_extended

<a id="qca.managed.types.self_hosted_work_heartbeat_response.SelfHostedWorkHeartbeatResponse.state"></a>

#### state

<a id="qca.managed.types.self_hosted_work_heartbeat_response.SelfHostedWorkHeartbeatResponse.ttl_seconds"></a>

#### ttl\_seconds

<a id="qca.managed.types.self_hosted_work_heartbeat_response.SelfHostedWorkHeartbeatResponse.type"></a>

#### type

<a id="qca.managed.types.self_hosted_work_queue_stats"></a>

# qca.managed.types.self\_hosted\_work\_queue\_stats

<a id="qca.managed.types.self_hosted_work_queue_stats.SelfHostedWorkQueueStats"></a>

## SelfHostedWorkQueueStats

```python
class SelfHostedWorkQueueStats(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/self_hosted_work_queue_stats.py)

<a id="qca.managed.types.self_hosted_work_queue_stats.SelfHostedWorkQueueStats.depth"></a>

#### depth

<a id="qca.managed.types.self_hosted_work_queue_stats.SelfHostedWorkQueueStats.oldest_queued_at"></a>

#### oldest\_queued\_at

<a id="qca.managed.types.self_hosted_work_queue_stats.SelfHostedWorkQueueStats.pending"></a>

#### pending

<a id="qca.managed.types.self_hosted_work_queue_stats.SelfHostedWorkQueueStats.type"></a>

#### type

<a id="qca.managed.types.self_hosted_work_queue_stats.SelfHostedWorkQueueStats.workers_polling"></a>

#### workers\_polling

<a id="qca.managed.types.send_session_events"></a>

# qca.managed.types.send\_session\_events

<a id="qca.managed.types.send_session_events.SendSessionEvents"></a>

## SendSessionEvents

```python
class SendSessionEvents(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/send_session_events.py)

<a id="qca.managed.types.send_session_events.SendSessionEvents.data"></a>

#### data

<a id="qca.managed.types.send_session_events_data_union"></a>

# qca.managed.types.send\_session\_events\_data\_union

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion"></a>

## SendSessionEventsDataUnion

```python
class SendSessionEventsDataUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/send_session_events_data_union.py)

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.id"></a>

#### id

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.content"></a>

#### content

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.type"></a>

#### type

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.processed_at"></a>

#### processed\_at

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.session_thread_id"></a>

#### session\_thread\_id

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.result"></a>

#### result

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.tool_use_id"></a>

#### tool\_use\_id

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.deny_message"></a>

#### deny\_message

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.custom_tool_use_id"></a>

#### custom\_tool\_use\_id

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.is_error"></a>

#### is\_error

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.description"></a>

#### description

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.max_iterations"></a>

#### max\_iterations

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.outcome_id"></a>

#### outcome\_id

<a id="qca.managed.types.send_session_events_data_union.SendSessionEventsDataUnion.rubric"></a>

#### rubric

<a id="qca.managed.types.server_tool_usage"></a>

# qca.managed.types.server\_tool\_usage

<a id="qca.managed.types.server_tool_usage.ServerToolUsage"></a>

## ServerToolUsage

```python
class ServerToolUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/server_tool_usage.py)

<a id="qca.managed.types.server_tool_usage.ServerToolUsage.web_fetch_requests"></a>

#### web\_fetch\_requests

<a id="qca.managed.types.server_tool_usage.ServerToolUsage.web_search_requests"></a>

#### web\_search\_requests

<a id="qca.managed.types.session"></a>

# qca.managed.types.session

<a id="qca.managed.types.session.Session"></a>

## Session

```python
class Session(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session.py)

<a id="qca.managed.types.session.Session.environment_variables"></a>

#### environment\_variables

<a id="qca.managed.types.session.Session.id"></a>

#### id

<a id="qca.managed.types.session.Session.agent"></a>

#### agent

<a id="qca.managed.types.session.Session.archived_at"></a>

#### archived\_at

<a id="qca.managed.types.session.Session.budget"></a>

#### budget

<a id="qca.managed.types.session.Session.created_at"></a>

#### created\_at

<a id="qca.managed.types.session.Session.environment_id"></a>

#### environment\_id

<a id="qca.managed.types.session.Session.metadata"></a>

#### metadata

<a id="qca.managed.types.session.Session.outcome_evaluations"></a>

#### outcome\_evaluations

<a id="qca.managed.types.session.Session.resources"></a>

#### resources

<a id="qca.managed.types.session.Session.stats"></a>

#### stats

<a id="qca.managed.types.session.Session.status"></a>

#### status

<a id="qca.managed.types.session.Session.title"></a>

#### title

<a id="qca.managed.types.session.Session.type"></a>

#### type

<a id="qca.managed.types.session.Session.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.session.Session.usage"></a>

#### usage

<a id="qca.managed.types.session.Session.vault_ids"></a>

#### vault\_ids

<a id="qca.managed.types.session.Session.deployment_id"></a>

#### deployment\_id

<a id="qca.managed.types.session_agent"></a>

# qca.managed.types.session\_agent

<a id="qca.managed.types.session_agent.SessionAgent"></a>

## SessionAgent

```python
class SessionAgent(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_agent.py)

<a id="qca.managed.types.session_agent.SessionAgent.id"></a>

#### id

<a id="qca.managed.types.session_agent.SessionAgent.description"></a>

#### description

<a id="qca.managed.types.session_agent.SessionAgent.mcp_servers"></a>

#### mcp\_servers

<a id="qca.managed.types.session_agent.SessionAgent.model"></a>

#### model

<a id="qca.managed.types.session_agent.SessionAgent.multiagent"></a>

#### multiagent

<a id="qca.managed.types.session_agent.SessionAgent.name"></a>

#### name

<a id="qca.managed.types.session_agent.SessionAgent.skills"></a>

#### skills

<a id="qca.managed.types.session_agent.SessionAgent.system"></a>

#### system

<a id="qca.managed.types.session_agent.SessionAgent.tools"></a>

#### tools

<a id="qca.managed.types.session_agent.SessionAgent.type"></a>

#### type

<a id="qca.managed.types.session_agent.SessionAgent.version"></a>

#### version

<a id="qca.managed.types.session_agent_skill_union"></a>

# qca.managed.types.session\_agent\_skill\_union

<a id="qca.managed.types.session_agent_skill_union.SessionAgentSkillUnion"></a>

## SessionAgentSkillUnion

```python
class SessionAgentSkillUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_agent_skill_union.py)

<a id="qca.managed.types.session_agent_skill_union.SessionAgentSkillUnion.skill_id"></a>

#### skill\_id

<a id="qca.managed.types.session_agent_skill_union.SessionAgentSkillUnion.type"></a>

#### type

<a id="qca.managed.types.session_agent_skill_union.SessionAgentSkillUnion.version"></a>

#### version

<a id="qca.managed.types.session_agent_tool_union"></a>

# qca.managed.types.session\_agent\_tool\_union

<a id="qca.managed.types.session_agent_tool_union.SessionAgentToolUnion"></a>

## SessionAgentToolUnion

```python
class SessionAgentToolUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_agent_tool_union.py)

<a id="qca.managed.types.session_agent_tool_union.SessionAgentToolUnion.enabled_tools"></a>

#### enabled\_tools

<a id="qca.managed.types.session_agent_tool_union.SessionAgentToolUnion.disallowed_tools"></a>

#### disallowed\_tools

<a id="qca.managed.types.session_agent_tool_union.SessionAgentToolUnion.configs"></a>

#### configs

<a id="qca.managed.types.session_agent_tool_union.SessionAgentToolUnion.default_config"></a>

#### default\_config

<a id="qca.managed.types.session_agent_tool_union.SessionAgentToolUnion.type"></a>

#### type

<a id="qca.managed.types.session_agent_tool_union.SessionAgentToolUnion.mcp_server_name"></a>

#### mcp\_server\_name

<a id="qca.managed.types.session_agent_tool_union.SessionAgentToolUnion.description"></a>

#### description

<a id="qca.managed.types.session_agent_tool_union.SessionAgentToolUnion.input_schema"></a>

#### input\_schema

<a id="qca.managed.types.session_agent_tool_union.SessionAgentToolUnion.name"></a>

#### name

<a id="qca.managed.types.session_agent_tool_union_default_config"></a>

# qca.managed.types.session\_agent\_tool\_union\_default\_config

<a id="qca.managed.types.session_agent_tool_union_default_config.SessionAgentToolUnionDefaultConfig"></a>

## SessionAgentToolUnionDefaultConfig

```python
class SessionAgentToolUnionDefaultConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_agent_tool_union_default_config.py)

<a id="qca.managed.types.session_agent_tool_union_default_config.SessionAgentToolUnionDefaultConfig.enabled"></a>

#### enabled

<a id="qca.managed.types.session_agent_tool_union_default_config.SessionAgentToolUnionDefaultConfig.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.session_agent_tool_union_default_config_permission_policy"></a>

# qca.managed.types.session\_agent\_tool\_union\_default\_config\_permission\_policy

<a id="qca.managed.types.session_agent_tool_union_default_config_permission_policy.SessionAgentToolUnionDefaultConfigPermissionPolicy"></a>

## SessionAgentToolUnionDefaultConfigPermissionPolicy

```python
class SessionAgentToolUnionDefaultConfigPermissionPolicy(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_agent_tool_union_default_config_permission_policy.py)

<a id="qca.managed.types.session_agent_tool_union_default_config_permission_policy.SessionAgentToolUnionDefaultConfigPermissionPolicy.type"></a>

#### type

<a id="qca.managed.types.session_agent_update_param"></a>

# qca.managed.types.session\_agent\_update\_param

<a id="qca.managed.types.session_agent_update_param.SessionAgentUpdateParam"></a>

## SessionAgentUpdateParam

```python
class SessionAgentUpdateParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_agent_update_param.py)

<a id="qca.managed.types.session_agent_update_param.SessionAgentUpdateParam.model"></a>

#### model

<a id="qca.managed.types.session_agent_update_param.SessionAgentUpdateParam.system"></a>

#### system

<a id="qca.managed.types.session_agent_update_param.SessionAgentUpdateParam.skills"></a>

#### skills

<a id="qca.managed.types.session_agent_update_param.SessionAgentUpdateParam.mcp_servers"></a>

#### mcp\_servers

<a id="qca.managed.types.session_agent_update_param.SessionAgentUpdateParam.tools"></a>

#### tools

<a id="qca.managed.types.session_archive_params"></a>

# qca.managed.types.session\_archive\_params

<a id="qca.managed.types.session_archive_params.SessionArchiveParams"></a>

## SessionArchiveParams

```python
class SessionArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_archive_params.py)

<a id="qca.managed.types.session_archive_params.SessionArchiveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_archive_params.SessionArchiveParams.betas"></a>

#### betas

<a id="qca.managed.types.session_create_params"></a>

# qca.managed.types.session\_create\_params

<a id="qca.managed.types.session_create_params.SessionCreateParams"></a>

## SessionCreateParams

```python
class SessionCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_create_params.py)

<a id="qca.managed.types.session_create_params.SessionCreateParams.environment_variables"></a>

#### environment\_variables

<a id="qca.managed.types.session_create_params.SessionCreateParams.agent"></a>

#### agent

<a id="qca.managed.types.session_create_params.SessionCreateParams.environment_id"></a>

#### environment\_id

<a id="qca.managed.types.session_create_params.SessionCreateParams.title"></a>

#### title

<a id="qca.managed.types.session_create_params.SessionCreateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_create_params.SessionCreateParams.budget"></a>

#### budget

<a id="qca.managed.types.session_create_params.SessionCreateParams.initial_events"></a>

#### initial\_events

<a id="qca.managed.types.session_create_params.SessionCreateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.session_create_params.SessionCreateParams.resources"></a>

#### resources

<a id="qca.managed.types.session_create_params.SessionCreateParams.vault_ids"></a>

#### vault\_ids

<a id="qca.managed.types.session_create_params.SessionCreateParams.betas"></a>

#### betas

<a id="qca.managed.types.session_delete_params"></a>

# qca.managed.types.session\_delete\_params

<a id="qca.managed.types.session_delete_params.SessionDeleteParams"></a>

## SessionDeleteParams

```python
class SessionDeleteParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_delete_params.py)

<a id="qca.managed.types.session_delete_params.SessionDeleteParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_delete_params.SessionDeleteParams.betas"></a>

#### betas

<a id="qca.managed.types.session_error_event_error_union"></a>

# qca.managed.types.session\_error\_event\_error\_union

<a id="qca.managed.types.session_error_event_error_union.SessionErrorEventErrorUnion"></a>

## SessionErrorEventErrorUnion

```python
class SessionErrorEventErrorUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_error_event_error_union.py)

<a id="qca.managed.types.session_error_event_error_union.SessionErrorEventErrorUnion.message"></a>

#### message

<a id="qca.managed.types.session_error_event_error_union.SessionErrorEventErrorUnion.retry_status"></a>

#### retry\_status

<a id="qca.managed.types.session_error_event_error_union.SessionErrorEventErrorUnion.type"></a>

#### type

<a id="qca.managed.types.session_error_event_error_union.SessionErrorEventErrorUnion.mcp_server_name"></a>

#### mcp\_server\_name

<a id="qca.managed.types.session_error_event_error_union.SessionErrorEventErrorUnion.credential_id"></a>

#### credential\_id

<a id="qca.managed.types.session_error_event_error_union.SessionErrorEventErrorUnion.vault_id"></a>

#### vault\_id

<a id="qca.managed.types.session_error_event_error_union_retry_status"></a>

# qca.managed.types.session\_error\_event\_error\_union\_retry\_status

<a id="qca.managed.types.session_error_event_error_union_retry_status.SessionErrorEventErrorUnionRetryStatus"></a>

## SessionErrorEventErrorUnionRetryStatus

```python
class SessionErrorEventErrorUnionRetryStatus(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_error_event_error_union_retry_status.py)

<a id="qca.managed.types.session_error_event_error_union_retry_status.SessionErrorEventErrorUnionRetryStatus.type"></a>

#### type

<a id="qca.managed.types.session_event"></a>

# qca.managed.types.session\_event

<a id="qca.managed.types.session_event.SessionEvent"></a>

## SessionEvent

```python
class SessionEvent(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_event.py)

<a id="qca.managed.types.session_event.SessionEvent.id"></a>

#### id

<a id="qca.managed.types.session_event.SessionEvent.content"></a>

#### content

<a id="qca.managed.types.session_event.SessionEvent.type"></a>

#### type

<a id="qca.managed.types.session_event.SessionEvent.processed_at"></a>

#### processed\_at

<a id="qca.managed.types.session_event.SessionEvent.session_thread_id"></a>

#### session\_thread\_id

<a id="qca.managed.types.session_event.SessionEvent.result"></a>

#### result

<a id="qca.managed.types.session_event.SessionEvent.tool_use_id"></a>

#### tool\_use\_id

<a id="qca.managed.types.session_event.SessionEvent.deny_message"></a>

#### deny\_message

<a id="qca.managed.types.session_event.SessionEvent.custom_tool_use_id"></a>

#### custom\_tool\_use\_id

<a id="qca.managed.types.session_event.SessionEvent.is_error"></a>

#### is\_error

<a id="qca.managed.types.session_event.SessionEvent.input"></a>

#### input

<a id="qca.managed.types.session_event.SessionEvent.name"></a>

#### name

<a id="qca.managed.types.session_event.SessionEvent.mcp_server_name"></a>

#### mcp\_server\_name

<a id="qca.managed.types.session_event.SessionEvent.evaluated_permission"></a>

#### evaluated\_permission

<a id="qca.managed.types.session_event.SessionEvent.mcp_tool_use_id"></a>

#### mcp\_tool\_use\_id

<a id="qca.managed.types.session_event.SessionEvent.from_session_thread_id"></a>

#### from\_session\_thread\_id

<a id="qca.managed.types.session_event.SessionEvent.from_agent_name"></a>

#### from\_agent\_name

<a id="qca.managed.types.session_event.SessionEvent.to_session_thread_id"></a>

#### to\_session\_thread\_id

<a id="qca.managed.types.session_event.SessionEvent.to_agent_name"></a>

#### to\_agent\_name

<a id="qca.managed.types.session_event.SessionEvent.error"></a>

#### error

<a id="qca.managed.types.session_event.SessionEvent.stop_reason"></a>

#### stop\_reason

<a id="qca.managed.types.session_event.SessionEvent.agent_name"></a>

#### agent\_name

<a id="qca.managed.types.session_event.SessionEvent.iteration"></a>

#### iteration

<a id="qca.managed.types.session_event.SessionEvent.outcome_id"></a>

#### outcome\_id

<a id="qca.managed.types.session_event.SessionEvent.explanation"></a>

#### explanation

<a id="qca.managed.types.session_event.SessionEvent.outcome_evaluation_start_id"></a>

#### outcome\_evaluation\_start\_id

<a id="qca.managed.types.session_event.SessionEvent.usage"></a>

#### usage

<a id="qca.managed.types.session_event.SessionEvent.model_request_start_id"></a>

#### model\_request\_start\_id

<a id="qca.managed.types.session_event.SessionEvent.model_usage"></a>

#### model\_usage

<a id="qca.managed.types.session_event.SessionEvent.description"></a>

#### description

<a id="qca.managed.types.session_event.SessionEvent.max_iterations"></a>

#### max\_iterations

<a id="qca.managed.types.session_event.SessionEvent.rubric"></a>

#### rubric

<a id="qca.managed.types.session_event.SessionEvent.agent"></a>

#### agent

<a id="qca.managed.types.session_event.SessionEvent.budget"></a>

#### budget

<a id="qca.managed.types.session_event.SessionEvent.metadata"></a>

#### metadata

<a id="qca.managed.types.session_event.SessionEvent.title"></a>

#### title

<a id="qca.managed.types.session_event_list_params"></a>

# qca.managed.types.session\_event\_list\_params

<a id="qca.managed.types.session_event_list_params.SessionEventListParams"></a>

## SessionEventListParams

```python
class SessionEventListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_event_list_params.py)

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.before_id"></a>

#### before\_id

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.after_id"></a>

#### after\_id

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.created_at_gt"></a>

#### created\_at\_gt

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.created_at_gte"></a>

#### created\_at\_gte

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.created_at_lt"></a>

#### created\_at\_lt

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.created_at_lte"></a>

#### created\_at\_lte

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.limit"></a>

#### limit

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.page"></a>

#### page

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.order"></a>

#### order

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.types"></a>

#### types

<a id="qca.managed.types.session_event_list_params.SessionEventListParams.betas"></a>

#### betas

<a id="qca.managed.types.session_event_send_params"></a>

# qca.managed.types.session\_event\_send\_params

<a id="qca.managed.types.session_event_send_params.SessionEventSendParams"></a>

## SessionEventSendParams

```python
class SessionEventSendParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_event_send_params.py)

<a id="qca.managed.types.session_event_send_params.SessionEventSendParams.events"></a>

#### events

<a id="qca.managed.types.session_event_send_params.SessionEventSendParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_event_send_params.SessionEventSendParams.betas"></a>

#### betas

<a id="qca.managed.types.session_event_stop_reason"></a>

# qca.managed.types.session\_event\_stop\_reason

<a id="qca.managed.types.session_event_stop_reason.SessionEventStopReason"></a>

## SessionEventStopReason

```python
class SessionEventStopReason(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_event_stop_reason.py)

<a id="qca.managed.types.session_event_stop_reason.SessionEventStopReason.type"></a>

#### type

<a id="qca.managed.types.session_event_stop_reason.SessionEventStopReason.event_ids"></a>

#### event\_ids

<a id="qca.managed.types.session_event_stream_params"></a>

# qca.managed.types.session\_event\_stream\_params

<a id="qca.managed.types.session_event_stream_params.SessionEventStreamParams"></a>

## SessionEventStreamParams

```python
class SessionEventStreamParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_event_stream_params.py)

<a id="qca.managed.types.session_event_stream_params.SessionEventStreamParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_event_stream_params.SessionEventStreamParams.event_deltas"></a>

#### event\_deltas

<a id="qca.managed.types.session_event_stream_params.SessionEventStreamParams.betas"></a>

#### betas

<a id="qca.managed.types.session_event_stream_params.SessionEventStreamParams.last_event_id"></a>

#### last\_event\_id

<a id="qca.managed.types.session_event_usage"></a>

# qca.managed.types.session\_event\_usage

<a id="qca.managed.types.session_event_usage.SessionEventUsage"></a>

## SessionEventUsage

```python
class SessionEventUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_event_usage.py)

<a id="qca.managed.types.session_event_usage.SessionEventUsage.cache_creation_input_tokens"></a>

#### cache\_creation\_input\_tokens

<a id="qca.managed.types.session_event_usage.SessionEventUsage.cache_read_input_tokens"></a>

#### cache\_read\_input\_tokens

<a id="qca.managed.types.session_event_usage.SessionEventUsage.input_tokens"></a>

#### input\_tokens

<a id="qca.managed.types.session_event_usage.SessionEventUsage.output_tokens"></a>

#### output\_tokens

<a id="qca.managed.types.session_event_usage.SessionEventUsage.speed"></a>

#### speed

<a id="qca.managed.types.session_event_usage.SessionEventUsage.active_seconds"></a>

#### active\_seconds

<a id="qca.managed.types.session_event_usage.SessionEventUsage.cache_creation"></a>

#### cache\_creation

<a id="qca.managed.types.session_event_usage.SessionEventUsage.list_cost"></a>

#### list\_cost

<a id="qca.managed.types.session_event_usage.SessionEventUsage.server_tool_use"></a>

#### server\_tool\_use

<a id="qca.managed.types.session_list_params"></a>

# qca.managed.types.session\_list\_params

<a id="qca.managed.types.session_list_params.SessionListParams"></a>

## SessionListParams

```python
class SessionListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_list_params.py)

<a id="qca.managed.types.session_list_params.SessionListParams.agent_id"></a>

#### agent\_id

<a id="qca.managed.types.session_list_params.SessionListParams.agent_version"></a>

#### agent\_version

<a id="qca.managed.types.session_list_params.SessionListParams.created_at_gt"></a>

#### created\_at\_gt

<a id="qca.managed.types.session_list_params.SessionListParams.created_at_gte"></a>

#### created\_at\_gte

<a id="qca.managed.types.session_list_params.SessionListParams.created_at_lt"></a>

#### created\_at\_lt

<a id="qca.managed.types.session_list_params.SessionListParams.created_at_lte"></a>

#### created\_at\_lte

<a id="qca.managed.types.session_list_params.SessionListParams.deployment_id"></a>

#### deployment\_id

<a id="qca.managed.types.session_list_params.SessionListParams.include_archived"></a>

#### include\_archived

<a id="qca.managed.types.session_list_params.SessionListParams.limit"></a>

#### limit

<a id="qca.managed.types.session_list_params.SessionListParams.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.session_list_params.SessionListParams.page"></a>

#### page

<a id="qca.managed.types.session_list_params.SessionListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_list_params.SessionListParams.order"></a>

#### order

<a id="qca.managed.types.session_list_params.SessionListParams.statuses"></a>

#### statuses

<a id="qca.managed.types.session_list_params.SessionListParams.betas"></a>

#### betas

<a id="qca.managed.types.session_multiagent_coordinator"></a>

# qca.managed.types.session\_multiagent\_coordinator

<a id="qca.managed.types.session_multiagent_coordinator.SessionMultiagentCoordinator"></a>

## SessionMultiagentCoordinator

```python
class SessionMultiagentCoordinator(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_multiagent_coordinator.py)

<a id="qca.managed.types.session_multiagent_coordinator.SessionMultiagentCoordinator.agents"></a>

#### agents

<a id="qca.managed.types.session_multiagent_coordinator.SessionMultiagentCoordinator.type"></a>

#### type

<a id="qca.managed.types.session_multiagent_coordinator_agent_union"></a>

# qca.managed.types.session\_multiagent\_coordinator\_agent\_union

<a id="qca.managed.types.session_multiagent_coordinator_agent_union.SessionMultiagentCoordinatorAgentUnion"></a>

## SessionMultiagentCoordinatorAgentUnion

```python
class SessionMultiagentCoordinatorAgentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_multiagent_coordinator_agent_union.py)

<a id="qca.managed.types.session_multiagent_coordinator_agent_union.SessionMultiagentCoordinatorAgentUnion.id"></a>

#### id

<a id="qca.managed.types.session_multiagent_coordinator_agent_union.SessionMultiagentCoordinatorAgentUnion.description"></a>

#### description

<a id="qca.managed.types.session_multiagent_coordinator_agent_union.SessionMultiagentCoordinatorAgentUnion.mcp_servers"></a>

#### mcp\_servers

<a id="qca.managed.types.session_multiagent_coordinator_agent_union.SessionMultiagentCoordinatorAgentUnion.model"></a>

#### model

<a id="qca.managed.types.session_multiagent_coordinator_agent_union.SessionMultiagentCoordinatorAgentUnion.name"></a>

#### name

<a id="qca.managed.types.session_multiagent_coordinator_agent_union.SessionMultiagentCoordinatorAgentUnion.skills"></a>

#### skills

<a id="qca.managed.types.session_multiagent_coordinator_agent_union.SessionMultiagentCoordinatorAgentUnion.system"></a>

#### system

<a id="qca.managed.types.session_multiagent_coordinator_agent_union.SessionMultiagentCoordinatorAgentUnion.tools"></a>

#### tools

<a id="qca.managed.types.session_multiagent_coordinator_agent_union.SessionMultiagentCoordinatorAgentUnion.type"></a>

#### type

<a id="qca.managed.types.session_multiagent_coordinator_agent_union.SessionMultiagentCoordinatorAgentUnion.version"></a>

#### version

<a id="qca.managed.types.session_resource_add_params"></a>

# qca.managed.types.session\_resource\_add\_params

<a id="qca.managed.types.session_resource_add_params.SessionResourceAddParams"></a>

## SessionResourceAddParams

```python
class SessionResourceAddParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_resource_add_params.py)

<a id="qca.managed.types.session_resource_add_params.SessionResourceAddParams.file_id"></a>

#### file\_id

<a id="qca.managed.types.session_resource_add_params.SessionResourceAddParams.type"></a>

#### type

<a id="qca.managed.types.session_resource_add_params.SessionResourceAddParams.mount_path"></a>

#### mount\_path

<a id="qca.managed.types.session_resource_add_params.SessionResourceAddParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_resource_add_params.SessionResourceAddParams.betas"></a>

#### betas

<a id="qca.managed.types.session_resource_config_union"></a>

# qca.managed.types.session\_resource\_config\_union

<a id="qca.managed.types.session_resource_config_union.SessionResourceConfigUnion"></a>

## SessionResourceConfigUnion

```python
class SessionResourceConfigUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_resource_config_union.py)

<a id="qca.managed.types.session_resource_config_union.SessionResourceConfigUnion.type"></a>

#### type

<a id="qca.managed.types.session_resource_config_union.SessionResourceConfigUnion.url"></a>

#### url

<a id="qca.managed.types.session_resource_config_union.SessionResourceConfigUnion.checkout"></a>

#### checkout

<a id="qca.managed.types.session_resource_config_union.SessionResourceConfigUnion.mount_path"></a>

#### mount\_path

<a id="qca.managed.types.session_resource_config_union.SessionResourceConfigUnion.file_id"></a>

#### file\_id

<a id="qca.managed.types.session_resource_config_union.SessionResourceConfigUnion.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.session_resource_config_union.SessionResourceConfigUnion.access"></a>

#### access

<a id="qca.managed.types.session_resource_config_union.SessionResourceConfigUnion.instructions"></a>

#### instructions

<a id="qca.managed.types.session_resource_delete_params"></a>

# qca.managed.types.session\_resource\_delete\_params

<a id="qca.managed.types.session_resource_delete_params.SessionResourceDeleteParams"></a>

## SessionResourceDeleteParams

```python
class SessionResourceDeleteParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_resource_delete_params.py)

<a id="qca.managed.types.session_resource_delete_params.SessionResourceDeleteParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_resource_delete_params.SessionResourceDeleteParams.betas"></a>

#### betas

<a id="qca.managed.types.session_resource_get_response_union"></a>

# qca.managed.types.session\_resource\_get\_response\_union

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion"></a>

## SessionResourceGetResponseUnion

```python
class SessionResourceGetResponseUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_resource_get_response_union.py)

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.id"></a>

#### id

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.created_at"></a>

#### created\_at

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.mount_path"></a>

#### mount\_path

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.type"></a>

#### type

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.url"></a>

#### url

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.checkout"></a>

#### checkout

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.file_id"></a>

#### file\_id

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.access"></a>

#### access

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.description"></a>

#### description

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.instructions"></a>

#### instructions

<a id="qca.managed.types.session_resource_get_response_union.SessionResourceGetResponseUnion.name"></a>

#### name

<a id="qca.managed.types.session_resource_list_params"></a>

# qca.managed.types.session\_resource\_list\_params

<a id="qca.managed.types.session_resource_list_params.SessionResourceListParams"></a>

## SessionResourceListParams

```python
class SessionResourceListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_resource_list_params.py)

<a id="qca.managed.types.session_resource_list_params.SessionResourceListParams.before_id"></a>

#### before\_id

<a id="qca.managed.types.session_resource_list_params.SessionResourceListParams.after_id"></a>

#### after\_id

<a id="qca.managed.types.session_resource_list_params.SessionResourceListParams.limit"></a>

#### limit

<a id="qca.managed.types.session_resource_list_params.SessionResourceListParams.page"></a>

#### page

<a id="qca.managed.types.session_resource_list_params.SessionResourceListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_resource_list_params.SessionResourceListParams.betas"></a>

#### betas

<a id="qca.managed.types.session_resource_retrieve_params"></a>

# qca.managed.types.session\_resource\_retrieve\_params

<a id="qca.managed.types.session_resource_retrieve_params.SessionResourceRetrieveParams"></a>

## SessionResourceRetrieveParams

```python
class SessionResourceRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_resource_retrieve_params.py)

<a id="qca.managed.types.session_resource_retrieve_params.SessionResourceRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_resource_retrieve_params.SessionResourceRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.session_resource_union"></a>

# qca.managed.types.session\_resource\_union

<a id="qca.managed.types.session_resource_union.SessionResourceUnion"></a>

## SessionResourceUnion

```python
class SessionResourceUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_resource_union.py)

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.id"></a>

#### id

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.created_at"></a>

#### created\_at

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.mount_path"></a>

#### mount\_path

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.type"></a>

#### type

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.url"></a>

#### url

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.checkout"></a>

#### checkout

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.file_id"></a>

#### file\_id

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.access"></a>

#### access

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.description"></a>

#### description

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.instructions"></a>

#### instructions

<a id="qca.managed.types.session_resource_union.SessionResourceUnion.name"></a>

#### name

<a id="qca.managed.types.session_resource_update_params"></a>

# qca.managed.types.session\_resource\_update\_params

<a id="qca.managed.types.session_resource_update_params.SessionResourceUpdateParams"></a>

## SessionResourceUpdateParams

```python
class SessionResourceUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_resource_update_params.py)

<a id="qca.managed.types.session_resource_update_params.SessionResourceUpdateParams.password"></a>

#### password

<a id="qca.managed.types.session_resource_update_params.SessionResourceUpdateParams.authorization_token"></a>

#### authorization\_token

<a id="qca.managed.types.session_resource_update_params.SessionResourceUpdateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_resource_update_params.SessionResourceUpdateParams.betas"></a>

#### betas

<a id="qca.managed.types.session_resource_update_response_union"></a>

# qca.managed.types.session\_resource\_update\_response\_union

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion"></a>

## SessionResourceUpdateResponseUnion

```python
class SessionResourceUpdateResponseUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_resource_update_response_union.py)

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.id"></a>

#### id

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.created_at"></a>

#### created\_at

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.mount_path"></a>

#### mount\_path

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.type"></a>

#### type

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.url"></a>

#### url

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.checkout"></a>

#### checkout

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.file_id"></a>

#### file\_id

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.memory_store_id"></a>

#### memory\_store\_id

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.access"></a>

#### access

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.description"></a>

#### description

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.instructions"></a>

#### instructions

<a id="qca.managed.types.session_resource_update_response_union.SessionResourceUpdateResponseUnion.name"></a>

#### name

<a id="qca.managed.types.session_retrieve_params"></a>

# qca.managed.types.session\_retrieve\_params

<a id="qca.managed.types.session_retrieve_params.SessionRetrieveParams"></a>

## SessionRetrieveParams

```python
class SessionRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_retrieve_params.py)

<a id="qca.managed.types.session_retrieve_params.SessionRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_retrieve_params.SessionRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.session_stats"></a>

# qca.managed.types.session\_stats

<a id="qca.managed.types.session_stats.SessionStats"></a>

## SessionStats

```python
class SessionStats(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_stats.py)

<a id="qca.managed.types.session_stats.SessionStats.active_seconds"></a>

#### active\_seconds

<a id="qca.managed.types.session_stats.SessionStats.duration_seconds"></a>

#### duration\_seconds

<a id="qca.managed.types.session_stream_event"></a>

# qca.managed.types.session\_stream\_event

<a id="qca.managed.types.session_stream_event.SessionStreamEvent"></a>

## SessionStreamEvent

```python
class SessionStreamEvent(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_stream_event.py)

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.id"></a>

#### id

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.content"></a>

#### content

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.type"></a>

#### type

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.processed_at"></a>

#### processed\_at

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.session_thread_id"></a>

#### session\_thread\_id

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.result"></a>

#### result

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.tool_use_id"></a>

#### tool\_use\_id

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.deny_message"></a>

#### deny\_message

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.custom_tool_use_id"></a>

#### custom\_tool\_use\_id

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.is_error"></a>

#### is\_error

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.input"></a>

#### input

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.name"></a>

#### name

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.mcp_server_name"></a>

#### mcp\_server\_name

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.evaluated_permission"></a>

#### evaluated\_permission

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.mcp_tool_use_id"></a>

#### mcp\_tool\_use\_id

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.from_session_thread_id"></a>

#### from\_session\_thread\_id

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.from_agent_name"></a>

#### from\_agent\_name

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.to_session_thread_id"></a>

#### to\_session\_thread\_id

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.to_agent_name"></a>

#### to\_agent\_name

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.error"></a>

#### error

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.stop_reason"></a>

#### stop\_reason

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.agent_name"></a>

#### agent\_name

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.iteration"></a>

#### iteration

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.outcome_id"></a>

#### outcome\_id

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.explanation"></a>

#### explanation

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.outcome_evaluation_start_id"></a>

#### outcome\_evaluation\_start\_id

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.usage"></a>

#### usage

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.model_request_start_id"></a>

#### model\_request\_start\_id

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.model_usage"></a>

#### model\_usage

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.description"></a>

#### description

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.max_iterations"></a>

#### max\_iterations

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.rubric"></a>

#### rubric

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.agent"></a>

#### agent

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.budget"></a>

#### budget

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.metadata"></a>

#### metadata

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.title"></a>

#### title

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.event"></a>

#### event

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.delta"></a>

#### delta

<a id="qca.managed.types.session_stream_event.SessionStreamEvent.event_id"></a>

#### event\_id

<a id="qca.managed.types.session_stream_event_stop_reason"></a>

# qca.managed.types.session\_stream\_event\_stop\_reason

<a id="qca.managed.types.session_stream_event_stop_reason.SessionStreamEventStopReason"></a>

## SessionStreamEventStopReason

```python
class SessionStreamEventStopReason(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_stream_event_stop_reason.py)

<a id="qca.managed.types.session_stream_event_stop_reason.SessionStreamEventStopReason.type"></a>

#### type

<a id="qca.managed.types.session_stream_event_stop_reason.SessionStreamEventStopReason.event_ids"></a>

#### event\_ids

<a id="qca.managed.types.session_stream_event_usage"></a>

# qca.managed.types.session\_stream\_event\_usage

<a id="qca.managed.types.session_stream_event_usage.SessionStreamEventUsage"></a>

## SessionStreamEventUsage

```python
class SessionStreamEventUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_stream_event_usage.py)

<a id="qca.managed.types.session_stream_event_usage.SessionStreamEventUsage.cache_creation_input_tokens"></a>

#### cache\_creation\_input\_tokens

<a id="qca.managed.types.session_stream_event_usage.SessionStreamEventUsage.cache_read_input_tokens"></a>

#### cache\_read\_input\_tokens

<a id="qca.managed.types.session_stream_event_usage.SessionStreamEventUsage.input_tokens"></a>

#### input\_tokens

<a id="qca.managed.types.session_stream_event_usage.SessionStreamEventUsage.output_tokens"></a>

#### output\_tokens

<a id="qca.managed.types.session_stream_event_usage.SessionStreamEventUsage.speed"></a>

#### speed

<a id="qca.managed.types.session_stream_event_usage.SessionStreamEventUsage.active_seconds"></a>

#### active\_seconds

<a id="qca.managed.types.session_stream_event_usage.SessionStreamEventUsage.cache_creation"></a>

#### cache\_creation

<a id="qca.managed.types.session_stream_event_usage.SessionStreamEventUsage.list_cost"></a>

#### list\_cost

<a id="qca.managed.types.session_stream_event_usage.SessionStreamEventUsage.server_tool_use"></a>

#### server\_tool\_use

<a id="qca.managed.types.session_thread"></a>

# qca.managed.types.session\_thread

<a id="qca.managed.types.session_thread.SessionThread"></a>

## SessionThread

```python
class SessionThread(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread.py)

<a id="qca.managed.types.session_thread.SessionThread.id"></a>

#### id

<a id="qca.managed.types.session_thread.SessionThread.agent"></a>

#### agent

<a id="qca.managed.types.session_thread.SessionThread.archived_at"></a>

#### archived\_at

<a id="qca.managed.types.session_thread.SessionThread.created_at"></a>

#### created\_at

<a id="qca.managed.types.session_thread.SessionThread.parent_thread_id"></a>

#### parent\_thread\_id

<a id="qca.managed.types.session_thread.SessionThread.session_id"></a>

#### session\_id

<a id="qca.managed.types.session_thread.SessionThread.stats"></a>

#### stats

<a id="qca.managed.types.session_thread.SessionThread.status"></a>

#### status

<a id="qca.managed.types.session_thread.SessionThread.type"></a>

#### type

<a id="qca.managed.types.session_thread.SessionThread.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.session_thread.SessionThread.usage"></a>

#### usage

<a id="qca.managed.types.session_thread_agent_skill_union"></a>

# qca.managed.types.session\_thread\_agent\_skill\_union

<a id="qca.managed.types.session_thread_agent_skill_union.SessionThreadAgentSkillUnion"></a>

## SessionThreadAgentSkillUnion

```python
class SessionThreadAgentSkillUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_agent_skill_union.py)

<a id="qca.managed.types.session_thread_agent_skill_union.SessionThreadAgentSkillUnion.skill_id"></a>

#### skill\_id

<a id="qca.managed.types.session_thread_agent_skill_union.SessionThreadAgentSkillUnion.type"></a>

#### type

<a id="qca.managed.types.session_thread_agent_skill_union.SessionThreadAgentSkillUnion.version"></a>

#### version

<a id="qca.managed.types.session_thread_agent_tool_union"></a>

# qca.managed.types.session\_thread\_agent\_tool\_union

<a id="qca.managed.types.session_thread_agent_tool_union.SessionThreadAgentToolUnion"></a>

## SessionThreadAgentToolUnion

```python
class SessionThreadAgentToolUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_agent_tool_union.py)

<a id="qca.managed.types.session_thread_agent_tool_union.SessionThreadAgentToolUnion.enabled_tools"></a>

#### enabled\_tools

<a id="qca.managed.types.session_thread_agent_tool_union.SessionThreadAgentToolUnion.disallowed_tools"></a>

#### disallowed\_tools

<a id="qca.managed.types.session_thread_agent_tool_union.SessionThreadAgentToolUnion.configs"></a>

#### configs

<a id="qca.managed.types.session_thread_agent_tool_union.SessionThreadAgentToolUnion.default_config"></a>

#### default\_config

<a id="qca.managed.types.session_thread_agent_tool_union.SessionThreadAgentToolUnion.type"></a>

#### type

<a id="qca.managed.types.session_thread_agent_tool_union.SessionThreadAgentToolUnion.mcp_server_name"></a>

#### mcp\_server\_name

<a id="qca.managed.types.session_thread_agent_tool_union.SessionThreadAgentToolUnion.description"></a>

#### description

<a id="qca.managed.types.session_thread_agent_tool_union.SessionThreadAgentToolUnion.input_schema"></a>

#### input\_schema

<a id="qca.managed.types.session_thread_agent_tool_union.SessionThreadAgentToolUnion.name"></a>

#### name

<a id="qca.managed.types.session_thread_agent_tool_union_default_config"></a>

# qca.managed.types.session\_thread\_agent\_tool\_union\_default\_config

<a id="qca.managed.types.session_thread_agent_tool_union_default_config.SessionThreadAgentToolUnionDefaultConfig"></a>

## SessionThreadAgentToolUnionDefaultConfig

```python
class SessionThreadAgentToolUnionDefaultConfig(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_agent_tool_union_default_config.py)

<a id="qca.managed.types.session_thread_agent_tool_union_default_config.SessionThreadAgentToolUnionDefaultConfig.enabled"></a>

#### enabled

<a id="qca.managed.types.session_thread_agent_tool_union_default_config.SessionThreadAgentToolUnionDefaultConfig.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.session_thread_agent_tool_union_default_config_permission_policy"></a>

# qca.managed.types.session\_thread\_agent\_tool\_union\_default\_config\_permission\_policy

<a id="qca.managed.types.session_thread_agent_tool_union_default_config_permission_policy.SessionThreadAgentToolUnionDefaultConfigPermissionPolicy"></a>

## SessionThreadAgentToolUnionDefaultConfigPermissionPolicy

```python
class SessionThreadAgentToolUnionDefaultConfigPermissionPolicy(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_agent_tool_union_default_config_permission_policy.py)

<a id="qca.managed.types.session_thread_agent_tool_union_default_config_permission_policy.SessionThreadAgentToolUnionDefaultConfigPermissionPolicy.type"></a>

#### type

<a id="qca.managed.types.session_thread_agent_union"></a>

# qca.managed.types.session\_thread\_agent\_union

<a id="qca.managed.types.session_thread_agent_union.SessionThreadAgentUnion"></a>

## SessionThreadAgentUnion

```python
class SessionThreadAgentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_agent_union.py)

<a id="qca.managed.types.session_thread_agent_union.SessionThreadAgentUnion.id"></a>

#### id

<a id="qca.managed.types.session_thread_agent_union.SessionThreadAgentUnion.description"></a>

#### description

<a id="qca.managed.types.session_thread_agent_union.SessionThreadAgentUnion.mcp_servers"></a>

#### mcp\_servers

<a id="qca.managed.types.session_thread_agent_union.SessionThreadAgentUnion.model"></a>

#### model

<a id="qca.managed.types.session_thread_agent_union.SessionThreadAgentUnion.name"></a>

#### name

<a id="qca.managed.types.session_thread_agent_union.SessionThreadAgentUnion.skills"></a>

#### skills

<a id="qca.managed.types.session_thread_agent_union.SessionThreadAgentUnion.system"></a>

#### system

<a id="qca.managed.types.session_thread_agent_union.SessionThreadAgentUnion.tools"></a>

#### tools

<a id="qca.managed.types.session_thread_agent_union.SessionThreadAgentUnion.type"></a>

#### type

<a id="qca.managed.types.session_thread_agent_union.SessionThreadAgentUnion.version"></a>

#### version

<a id="qca.managed.types.session_thread_archive_params"></a>

# qca.managed.types.session\_thread\_archive\_params

<a id="qca.managed.types.session_thread_archive_params.SessionThreadArchiveParams"></a>

## SessionThreadArchiveParams

```python
class SessionThreadArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_archive_params.py)

<a id="qca.managed.types.session_thread_archive_params.SessionThreadArchiveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_thread_archive_params.SessionThreadArchiveParams.betas"></a>

#### betas

<a id="qca.managed.types.session_thread_event_list_params"></a>

# qca.managed.types.session\_thread\_event\_list\_params

<a id="qca.managed.types.session_thread_event_list_params.SessionThreadEventListParams"></a>

## SessionThreadEventListParams

```python
class SessionThreadEventListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_event_list_params.py)

<a id="qca.managed.types.session_thread_event_list_params.SessionThreadEventListParams.before_id"></a>

#### before\_id

<a id="qca.managed.types.session_thread_event_list_params.SessionThreadEventListParams.after_id"></a>

#### after\_id

<a id="qca.managed.types.session_thread_event_list_params.SessionThreadEventListParams.limit"></a>

#### limit

<a id="qca.managed.types.session_thread_event_list_params.SessionThreadEventListParams.page"></a>

#### page

<a id="qca.managed.types.session_thread_event_list_params.SessionThreadEventListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_thread_event_list_params.SessionThreadEventListParams.betas"></a>

#### betas

<a id="qca.managed.types.session_thread_event_stream_params"></a>

# qca.managed.types.session\_thread\_event\_stream\_params

<a id="qca.managed.types.session_thread_event_stream_params.SessionThreadEventStreamParams"></a>

## SessionThreadEventStreamParams

```python
class SessionThreadEventStreamParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_event_stream_params.py)

<a id="qca.managed.types.session_thread_event_stream_params.SessionThreadEventStreamParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_thread_event_stream_params.SessionThreadEventStreamParams.event_deltas"></a>

#### event\_deltas

<a id="qca.managed.types.session_thread_event_stream_params.SessionThreadEventStreamParams.betas"></a>

#### betas

<a id="qca.managed.types.session_thread_list_params"></a>

# qca.managed.types.session\_thread\_list\_params

<a id="qca.managed.types.session_thread_list_params.SessionThreadListParams"></a>

## SessionThreadListParams

```python
class SessionThreadListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_list_params.py)

<a id="qca.managed.types.session_thread_list_params.SessionThreadListParams.limit"></a>

#### limit

<a id="qca.managed.types.session_thread_list_params.SessionThreadListParams.page"></a>

#### page

<a id="qca.managed.types.session_thread_list_params.SessionThreadListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_thread_list_params.SessionThreadListParams.betas"></a>

#### betas

<a id="qca.managed.types.session_thread_retrieve_params"></a>

# qca.managed.types.session\_thread\_retrieve\_params

<a id="qca.managed.types.session_thread_retrieve_params.SessionThreadRetrieveParams"></a>

## SessionThreadRetrieveParams

```python
class SessionThreadRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_retrieve_params.py)

<a id="qca.managed.types.session_thread_retrieve_params.SessionThreadRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_thread_retrieve_params.SessionThreadRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.session_thread_stats"></a>

# qca.managed.types.session\_thread\_stats

<a id="qca.managed.types.session_thread_stats.SessionThreadStats"></a>

## SessionThreadStats

```python
class SessionThreadStats(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_stats.py)

<a id="qca.managed.types.session_thread_stats.SessionThreadStats.active_seconds"></a>

#### active\_seconds

<a id="qca.managed.types.session_thread_stats.SessionThreadStats.duration_seconds"></a>

#### duration\_seconds

<a id="qca.managed.types.session_thread_stats.SessionThreadStats.startup_seconds"></a>

#### startup\_seconds

<a id="qca.managed.types.session_thread_usage"></a>

# qca.managed.types.session\_thread\_usage

<a id="qca.managed.types.session_thread_usage.SessionThreadUsage"></a>

## SessionThreadUsage

```python
class SessionThreadUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_thread_usage.py)

<a id="qca.managed.types.session_thread_usage.SessionThreadUsage.active_seconds"></a>

#### active\_seconds

<a id="qca.managed.types.session_thread_usage.SessionThreadUsage.cache_creation"></a>

#### cache\_creation

<a id="qca.managed.types.session_thread_usage.SessionThreadUsage.cache_read_input_tokens"></a>

#### cache\_read\_input\_tokens

<a id="qca.managed.types.session_thread_usage.SessionThreadUsage.input_tokens"></a>

#### input\_tokens

<a id="qca.managed.types.session_thread_usage.SessionThreadUsage.list_cost"></a>

#### list\_cost

<a id="qca.managed.types.session_thread_usage.SessionThreadUsage.output_tokens"></a>

#### output\_tokens

<a id="qca.managed.types.session_thread_usage.SessionThreadUsage.server_tool_use"></a>

#### server\_tool\_use

<a id="qca.managed.types.session_update_params"></a>

# qca.managed.types.session\_update\_params

<a id="qca.managed.types.session_update_params.SessionUpdateParams"></a>

## SessionUpdateParams

```python
class SessionUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_update_params.py)

<a id="qca.managed.types.session_update_params.SessionUpdateParams.environment_variables"></a>

#### environment\_variables

<a id="qca.managed.types.session_update_params.SessionUpdateParams.title"></a>

#### title

<a id="qca.managed.types.session_update_params.SessionUpdateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.session_update_params.SessionUpdateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.session_update_params.SessionUpdateParams.agent"></a>

#### agent

<a id="qca.managed.types.session_update_params.SessionUpdateParams.budget"></a>

#### budget

<a id="qca.managed.types.session_update_params.SessionUpdateParams.vault_ids"></a>

#### vault\_ids

<a id="qca.managed.types.session_update_params.SessionUpdateParams.betas"></a>

#### betas

<a id="qca.managed.types.session_usage"></a>

# qca.managed.types.session\_usage

<a id="qca.managed.types.session_usage.SessionUsage"></a>

## SessionUsage

```python
class SessionUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_usage.py)

<a id="qca.managed.types.session_usage.SessionUsage.active_seconds"></a>

#### active\_seconds

<a id="qca.managed.types.session_usage.SessionUsage.cache_creation"></a>

#### cache\_creation

<a id="qca.managed.types.session_usage.SessionUsage.cache_read_input_tokens"></a>

#### cache\_read\_input\_tokens

<a id="qca.managed.types.session_usage.SessionUsage.input_tokens"></a>

#### input\_tokens

<a id="qca.managed.types.session_usage.SessionUsage.list_cost"></a>

#### list\_cost

<a id="qca.managed.types.session_usage.SessionUsage.output_tokens"></a>

#### output\_tokens

<a id="qca.managed.types.session_usage.SessionUsage.server_tool_use"></a>

#### server\_tool\_use

<a id="qca.managed.types.session_work_data"></a>

# qca.managed.types.session\_work\_data

<a id="qca.managed.types.session_work_data.SessionWorkData"></a>

## SessionWorkData

```python
class SessionWorkData(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/session_work_data.py)

<a id="qca.managed.types.session_work_data.SessionWorkData.id"></a>

#### id

<a id="qca.managed.types.session_work_data.SessionWorkData.type"></a>

#### type

<a id="qca.managed.types.skill"></a>

# qca.managed.types.skill

<a id="qca.managed.types.skill.Skill"></a>

## Skill

```python
class Skill(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill.py)

<a id="qca.managed.types.skill.Skill.metadata"></a>

#### metadata

<a id="qca.managed.types.skill.Skill.id"></a>

#### id

<a id="qca.managed.types.skill.Skill.created_at"></a>

#### created\_at

<a id="qca.managed.types.skill.Skill.display_title"></a>

#### display\_title

<a id="qca.managed.types.skill.Skill.latest_version"></a>

#### latest\_version

<a id="qca.managed.types.skill.Skill.source"></a>

#### source

<a id="qca.managed.types.skill.Skill.type"></a>

#### type

<a id="qca.managed.types.skill.Skill.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.skill_create_params"></a>

# qca.managed.types.skill\_create\_params

<a id="qca.managed.types.skill_create_params.SkillCreateParams"></a>

## SkillCreateParams

```python
class SkillCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill_create_params.py)

<a id="qca.managed.types.skill_create_params.SkillCreateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.skill_create_params.SkillCreateParams.files"></a>

#### files

<a id="qca.managed.types.skill_create_params.SkillCreateParams.display_title"></a>

#### display\_title

<a id="qca.managed.types.skill_create_params.SkillCreateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.skill_create_params.SkillCreateParams.betas"></a>

#### betas

<a id="qca.managed.types.skill_delete_params"></a>

# qca.managed.types.skill\_delete\_params

<a id="qca.managed.types.skill_delete_params.SkillDeleteParams"></a>

## SkillDeleteParams

```python
class SkillDeleteParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill_delete_params.py)

<a id="qca.managed.types.skill_delete_params.SkillDeleteParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.skill_delete_params.SkillDeleteParams.betas"></a>

#### betas

<a id="qca.managed.types.skill_list_params"></a>

# qca.managed.types.skill\_list\_params

<a id="qca.managed.types.skill_list_params.SkillListParams"></a>

## SkillListParams

```python
class SkillListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill_list_params.py)

<a id="qca.managed.types.skill_list_params.SkillListParams.display_name"></a>

#### display\_name

<a id="qca.managed.types.skill_list_params.SkillListParams.name"></a>

#### name

<a id="qca.managed.types.skill_list_params.SkillListParams.before_id"></a>

#### before\_id

<a id="qca.managed.types.skill_list_params.SkillListParams.after_id"></a>

#### after\_id

<a id="qca.managed.types.skill_list_params.SkillListParams.page"></a>

#### page

<a id="qca.managed.types.skill_list_params.SkillListParams.source"></a>

#### source

<a id="qca.managed.types.skill_list_params.SkillListParams.limit"></a>

#### limit

<a id="qca.managed.types.skill_list_params.SkillListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.skill_list_params.SkillListParams.betas"></a>

#### betas

<a id="qca.managed.types.skill_retrieve_params"></a>

# qca.managed.types.skill\_retrieve\_params

<a id="qca.managed.types.skill_retrieve_params.SkillRetrieveParams"></a>

## SkillRetrieveParams

```python
class SkillRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill_retrieve_params.py)

<a id="qca.managed.types.skill_retrieve_params.SkillRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.skill_retrieve_params.SkillRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.skill_source"></a>

# qca.managed.types.skill\_source

<a id="qca.managed.types.skill_source.SkillSource"></a>

## SkillSource

```python
class SkillSource(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill_source.py)

<a id="qca.managed.types.skill_source.SkillSource.type"></a>

#### type

<a id="qca.managed.types.skill_version"></a>

# qca.managed.types.skill\_version

<a id="qca.managed.types.skill_version.SkillVersion"></a>

## SkillVersion

```python
class SkillVersion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill_version.py)

<a id="qca.managed.types.skill_version.SkillVersion.version"></a>

#### version

<a id="qca.managed.types.skill_version.SkillVersion.directory"></a>

#### directory

<a id="qca.managed.types.skill_version.SkillVersion.id"></a>

#### id

<a id="qca.managed.types.skill_version.SkillVersion.created_at"></a>

#### created\_at

<a id="qca.managed.types.skill_version.SkillVersion.description"></a>

#### description

<a id="qca.managed.types.skill_version.SkillVersion.name"></a>

#### name

<a id="qca.managed.types.skill_version.SkillVersion.skill_id"></a>

#### skill\_id

<a id="qca.managed.types.skill_version.SkillVersion.type"></a>

#### type

<a id="qca.managed.types.skill_version_create_params"></a>

# qca.managed.types.skill\_version\_create\_params

<a id="qca.managed.types.skill_version_create_params.SkillVersionCreateParams"></a>

## SkillVersionCreateParams

```python
class SkillVersionCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill_version_create_params.py)

<a id="qca.managed.types.skill_version_create_params.SkillVersionCreateParams.files"></a>

#### files

<a id="qca.managed.types.skill_version_create_params.SkillVersionCreateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.skill_version_create_params.SkillVersionCreateParams.betas"></a>

#### betas

<a id="qca.managed.types.skill_version_delete_params"></a>

# qca.managed.types.skill\_version\_delete\_params

<a id="qca.managed.types.skill_version_delete_params.SkillVersionDeleteParams"></a>

## SkillVersionDeleteParams

```python
class SkillVersionDeleteParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill_version_delete_params.py)

<a id="qca.managed.types.skill_version_delete_params.SkillVersionDeleteParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.skill_version_delete_params.SkillVersionDeleteParams.betas"></a>

#### betas

<a id="qca.managed.types.skill_version_download_params"></a>

# qca.managed.types.skill\_version\_download\_params

<a id="qca.managed.types.skill_version_download_params.SkillVersionDownloadParams"></a>

## SkillVersionDownloadParams

```python
class SkillVersionDownloadParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill_version_download_params.py)

<a id="qca.managed.types.skill_version_download_params.SkillVersionDownloadParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.skill_version_download_params.SkillVersionDownloadParams.betas"></a>

#### betas

<a id="qca.managed.types.skill_version_list_params"></a>

# qca.managed.types.skill\_version\_list\_params

<a id="qca.managed.types.skill_version_list_params.SkillVersionListParams"></a>

## SkillVersionListParams

```python
class SkillVersionListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill_version_list_params.py)

<a id="qca.managed.types.skill_version_list_params.SkillVersionListParams.limit"></a>

#### limit

<a id="qca.managed.types.skill_version_list_params.SkillVersionListParams.page"></a>

#### page

<a id="qca.managed.types.skill_version_list_params.SkillVersionListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.skill_version_list_params.SkillVersionListParams.betas"></a>

#### betas

<a id="qca.managed.types.skill_version_retrieve_params"></a>

# qca.managed.types.skill\_version\_retrieve\_params

<a id="qca.managed.types.skill_version_retrieve_params.SkillVersionRetrieveParams"></a>

## SkillVersionRetrieveParams

```python
class SkillVersionRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/skill_version_retrieve_params.py)

<a id="qca.managed.types.skill_version_retrieve_params.SkillVersionRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.skill_version_retrieve_params.SkillVersionRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.span_model_usage"></a>

# qca.managed.types.span\_model\_usage

<a id="qca.managed.types.span_model_usage.SpanModelUsage"></a>

## SpanModelUsage

```python
class SpanModelUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/span_model_usage.py)

<a id="qca.managed.types.span_model_usage.SpanModelUsage.cache_creation_input_tokens"></a>

#### cache\_creation\_input\_tokens

<a id="qca.managed.types.span_model_usage.SpanModelUsage.cache_read_input_tokens"></a>

#### cache\_read\_input\_tokens

<a id="qca.managed.types.span_model_usage.SpanModelUsage.input_tokens"></a>

#### input\_tokens

<a id="qca.managed.types.span_model_usage.SpanModelUsage.output_tokens"></a>

#### output\_tokens

<a id="qca.managed.types.span_model_usage.SpanModelUsage.speed"></a>

#### speed

<a id="qca.managed.types.start_event_preview_union"></a>

# qca.managed.types.start\_event\_preview\_union

<a id="qca.managed.types.start_event_preview_union.StartEventPreviewUnion"></a>

## StartEventPreviewUnion

```python
class StartEventPreviewUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/start_event_preview_union.py)

<a id="qca.managed.types.start_event_preview_union.StartEventPreviewUnion.id"></a>

#### id

<a id="qca.managed.types.start_event_preview_union.StartEventPreviewUnion.type"></a>

#### type

<a id="qca.managed.types.static_bearer_create_params"></a>

# qca.managed.types.static\_bearer\_create\_params

<a id="qca.managed.types.static_bearer_create_params.StaticBearerCreateParams"></a>

## StaticBearerCreateParams

```python
class StaticBearerCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/static_bearer_create_params.py)

<a id="qca.managed.types.static_bearer_create_params.StaticBearerCreateParams.token"></a>

#### token

<a id="qca.managed.types.static_bearer_create_params.StaticBearerCreateParams.mcp_server_url"></a>

#### mcp\_server\_url

<a id="qca.managed.types.static_bearer_create_params.StaticBearerCreateParams.type"></a>

#### type

<a id="qca.managed.types.static_bearer_update_params"></a>

# qca.managed.types.static\_bearer\_update\_params

<a id="qca.managed.types.static_bearer_update_params.StaticBearerUpdateParams"></a>

## StaticBearerUpdateParams

```python
class StaticBearerUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/static_bearer_update_params.py)

<a id="qca.managed.types.static_bearer_update_params.StaticBearerUpdateParams.type"></a>

#### type

<a id="qca.managed.types.static_bearer_update_params.StaticBearerUpdateParams.token"></a>

#### token

<a id="qca.managed.types.stream_session_thread_events_union"></a>

# qca.managed.types.stream\_session\_thread\_events\_union

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion"></a>

## StreamSessionThreadEventsUnion

```python
class StreamSessionThreadEventsUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/stream_session_thread_events_union.py)

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.id"></a>

#### id

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.content"></a>

#### content

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.type"></a>

#### type

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.processed_at"></a>

#### processed\_at

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.session_thread_id"></a>

#### session\_thread\_id

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.result"></a>

#### result

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.tool_use_id"></a>

#### tool\_use\_id

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.deny_message"></a>

#### deny\_message

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.custom_tool_use_id"></a>

#### custom\_tool\_use\_id

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.is_error"></a>

#### is\_error

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.input"></a>

#### input

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.name"></a>

#### name

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.mcp_server_name"></a>

#### mcp\_server\_name

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.evaluated_permission"></a>

#### evaluated\_permission

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.mcp_tool_use_id"></a>

#### mcp\_tool\_use\_id

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.from_session_thread_id"></a>

#### from\_session\_thread\_id

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.from_agent_name"></a>

#### from\_agent\_name

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.to_session_thread_id"></a>

#### to\_session\_thread\_id

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.to_agent_name"></a>

#### to\_agent\_name

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.error"></a>

#### error

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.stop_reason"></a>

#### stop\_reason

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.agent_name"></a>

#### agent\_name

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.iteration"></a>

#### iteration

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.outcome_id"></a>

#### outcome\_id

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.explanation"></a>

#### explanation

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.outcome_evaluation_start_id"></a>

#### outcome\_evaluation\_start\_id

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.usage"></a>

#### usage

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.model_request_start_id"></a>

#### model\_request\_start\_id

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.model_usage"></a>

#### model\_usage

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.description"></a>

#### description

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.max_iterations"></a>

#### max\_iterations

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.rubric"></a>

#### rubric

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.agent"></a>

#### agent

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.budget"></a>

#### budget

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.metadata"></a>

#### metadata

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.title"></a>

#### title

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.event"></a>

#### event

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.delta"></a>

#### delta

<a id="qca.managed.types.stream_session_thread_events_union.StreamSessionThreadEventsUnion.event_id"></a>

#### event\_id

<a id="qca.managed.types.stream_session_thread_events_union_stop_reason"></a>

# qca.managed.types.stream\_session\_thread\_events\_union\_stop\_reason

<a id="qca.managed.types.stream_session_thread_events_union_stop_reason.StreamSessionThreadEventsUnionStopReason"></a>

## StreamSessionThreadEventsUnionStopReason

```python
class StreamSessionThreadEventsUnionStopReason(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/stream_session_thread_events_union_stop_reason.py)

<a id="qca.managed.types.stream_session_thread_events_union_stop_reason.StreamSessionThreadEventsUnionStopReason.type"></a>

#### type

<a id="qca.managed.types.stream_session_thread_events_union_stop_reason.StreamSessionThreadEventsUnionStopReason.event_ids"></a>

#### event\_ids

<a id="qca.managed.types.stream_session_thread_events_union_usage"></a>

# qca.managed.types.stream\_session\_thread\_events\_union\_usage

<a id="qca.managed.types.stream_session_thread_events_union_usage.StreamSessionThreadEventsUnionUsage"></a>

## StreamSessionThreadEventsUnionUsage

```python
class StreamSessionThreadEventsUnionUsage(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/stream_session_thread_events_union_usage.py)

<a id="qca.managed.types.stream_session_thread_events_union_usage.StreamSessionThreadEventsUnionUsage.cache_creation_input_tokens"></a>

#### cache\_creation\_input\_tokens

<a id="qca.managed.types.stream_session_thread_events_union_usage.StreamSessionThreadEventsUnionUsage.cache_read_input_tokens"></a>

#### cache\_read\_input\_tokens

<a id="qca.managed.types.stream_session_thread_events_union_usage.StreamSessionThreadEventsUnionUsage.input_tokens"></a>

#### input\_tokens

<a id="qca.managed.types.stream_session_thread_events_union_usage.StreamSessionThreadEventsUnionUsage.output_tokens"></a>

#### output\_tokens

<a id="qca.managed.types.stream_session_thread_events_union_usage.StreamSessionThreadEventsUnionUsage.speed"></a>

#### speed

<a id="qca.managed.types.stream_session_thread_events_union_usage.StreamSessionThreadEventsUnionUsage.active_seconds"></a>

#### active\_seconds

<a id="qca.managed.types.stream_session_thread_events_union_usage.StreamSessionThreadEventsUnionUsage.cache_creation"></a>

#### cache\_creation

<a id="qca.managed.types.stream_session_thread_events_union_usage.StreamSessionThreadEventsUnionUsage.list_cost"></a>

#### list\_cost

<a id="qca.managed.types.stream_session_thread_events_union_usage.StreamSessionThreadEventsUnionUsage.server_tool_use"></a>

#### server\_tool\_use

<a id="qca.managed.types.system_content_block"></a>

# qca.managed.types.system\_content\_block

<a id="qca.managed.types.system_content_block.SystemContentBlock"></a>

## SystemContentBlock

```python
class SystemContentBlock(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/system_content_block.py)

<a id="qca.managed.types.system_content_block.SystemContentBlock.text"></a>

#### text

<a id="qca.managed.types.system_content_block.SystemContentBlock.type"></a>

#### type

<a id="qca.managed.types.system_content_block_param"></a>

# qca.managed.types.system\_content\_block\_param

<a id="qca.managed.types.system_content_block_param.SystemContentBlockParam"></a>

## SystemContentBlockParam

```python
class SystemContentBlockParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/system_content_block_param.py)

<a id="qca.managed.types.system_content_block_param.SystemContentBlockParam.text"></a>

#### text

<a id="qca.managed.types.system_content_block_param.SystemContentBlockParam.type"></a>

#### type

<a id="qca.managed.types.system_message_event_params"></a>

# qca.managed.types.system\_message\_event\_params

<a id="qca.managed.types.system_message_event_params.SystemMessageEventParams"></a>

## SystemMessageEventParams

```python
class SystemMessageEventParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/system_message_event_params.py)

<a id="qca.managed.types.system_message_event_params.SystemMessageEventParams.content"></a>

#### content

<a id="qca.managed.types.system_message_event_params.SystemMessageEventParams.type"></a>

#### type

<a id="qca.managed.types.text_block"></a>

# qca.managed.types.text\_block

<a id="qca.managed.types.text_block.TextBlock"></a>

## TextBlock

```python
class TextBlock(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/text_block.py)

<a id="qca.managed.types.text_block.TextBlock.text"></a>

#### text

<a id="qca.managed.types.text_block.TextBlock.type"></a>

#### type

<a id="qca.managed.types.text_block_param"></a>

# qca.managed.types.text\_block\_param

<a id="qca.managed.types.text_block_param.TextBlockParam"></a>

## TextBlockParam

```python
class TextBlockParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/text_block_param.py)

<a id="qca.managed.types.text_block_param.TextBlockParam.text"></a>

#### text

<a id="qca.managed.types.text_block_param.TextBlockParam.type"></a>

#### type

<a id="qca.managed.types.text_rubric_params"></a>

# qca.managed.types.text\_rubric\_params

<a id="qca.managed.types.text_rubric_params.TextRubricParams"></a>

## TextRubricParams

```python
class TextRubricParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/text_rubric_params.py)

<a id="qca.managed.types.text_rubric_params.TextRubricParams.content"></a>

#### content

<a id="qca.managed.types.text_rubric_params.TextRubricParams.type"></a>

#### type

<a id="qca.managed.types.thinking_capability"></a>

# qca.managed.types.thinking\_capability

<a id="qca.managed.types.thinking_capability.ThinkingCapability"></a>

## ThinkingCapability

```python
class ThinkingCapability(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/thinking_capability.py)

<a id="qca.managed.types.thinking_capability.ThinkingCapability.supported"></a>

#### supported

<a id="qca.managed.types.thinking_capability.ThinkingCapability.types"></a>

#### types

<a id="qca.managed.types.thinking_types"></a>

# qca.managed.types.thinking\_types

<a id="qca.managed.types.thinking_types.ThinkingTypes"></a>

## ThinkingTypes

```python
class ThinkingTypes(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/thinking_types.py)

<a id="qca.managed.types.thinking_types.ThinkingTypes.adaptive"></a>

#### adaptive

<a id="qca.managed.types.thinking_types.ThinkingTypes.enabled"></a>

#### enabled

<a id="qca.managed.types.token_endpoint_auth_basic_param"></a>

# qca.managed.types.token\_endpoint\_auth\_basic\_param

<a id="qca.managed.types.token_endpoint_auth_basic_param.TokenEndpointAuthBasicParam"></a>

## TokenEndpointAuthBasicParam

```python
class TokenEndpointAuthBasicParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/token_endpoint_auth_basic_param.py)

<a id="qca.managed.types.token_endpoint_auth_basic_param.TokenEndpointAuthBasicParam.client_secret"></a>

#### client\_secret

<a id="qca.managed.types.token_endpoint_auth_basic_param.TokenEndpointAuthBasicParam.type"></a>

#### type

<a id="qca.managed.types.token_endpoint_auth_basic_update_param"></a>

# qca.managed.types.token\_endpoint\_auth\_basic\_update\_param

<a id="qca.managed.types.token_endpoint_auth_basic_update_param.TokenEndpointAuthBasicUpdateParam"></a>

## TokenEndpointAuthBasicUpdateParam

```python
class TokenEndpointAuthBasicUpdateParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/token_endpoint_auth_basic_update_param.py)

<a id="qca.managed.types.token_endpoint_auth_basic_update_param.TokenEndpointAuthBasicUpdateParam.type"></a>

#### type

<a id="qca.managed.types.token_endpoint_auth_basic_update_param.TokenEndpointAuthBasicUpdateParam.client_secret"></a>

#### client\_secret

<a id="qca.managed.types.token_endpoint_auth_none_param"></a>

# qca.managed.types.token\_endpoint\_auth\_none\_param

<a id="qca.managed.types.token_endpoint_auth_none_param.TokenEndpointAuthNoneParam"></a>

## TokenEndpointAuthNoneParam

```python
class TokenEndpointAuthNoneParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/token_endpoint_auth_none_param.py)

<a id="qca.managed.types.token_endpoint_auth_none_param.TokenEndpointAuthNoneParam.type"></a>

#### type

<a id="qca.managed.types.token_endpoint_auth_post_param"></a>

# qca.managed.types.token\_endpoint\_auth\_post\_param

<a id="qca.managed.types.token_endpoint_auth_post_param.TokenEndpointAuthPostParam"></a>

## TokenEndpointAuthPostParam

```python
class TokenEndpointAuthPostParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/token_endpoint_auth_post_param.py)

<a id="qca.managed.types.token_endpoint_auth_post_param.TokenEndpointAuthPostParam.client_secret"></a>

#### client\_secret

<a id="qca.managed.types.token_endpoint_auth_post_param.TokenEndpointAuthPostParam.type"></a>

#### type

<a id="qca.managed.types.token_endpoint_auth_post_update_param"></a>

# qca.managed.types.token\_endpoint\_auth\_post\_update\_param

<a id="qca.managed.types.token_endpoint_auth_post_update_param.TokenEndpointAuthPostUpdateParam"></a>

## TokenEndpointAuthPostUpdateParam

```python
class TokenEndpointAuthPostUpdateParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/token_endpoint_auth_post_update_param.py)

<a id="qca.managed.types.token_endpoint_auth_post_update_param.TokenEndpointAuthPostUpdateParam.type"></a>

#### type

<a id="qca.managed.types.token_endpoint_auth_post_update_param.TokenEndpointAuthPostUpdateParam.client_secret"></a>

#### client\_secret

<a id="qca.managed.types.trigger_context_union"></a>

# qca.managed.types.trigger\_context\_union

<a id="qca.managed.types.trigger_context_union.TriggerContextUnion"></a>

## TriggerContextUnion

```python
class TriggerContextUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/trigger_context_union.py)

<a id="qca.managed.types.trigger_context_union.TriggerContextUnion.scheduled_at"></a>

#### scheduled\_at

<a id="qca.managed.types.trigger_context_union.TriggerContextUnion.type"></a>

#### type

<a id="qca.managed.types.unrestricted_credential_networking_params"></a>

# qca.managed.types.unrestricted\_credential\_networking\_params

<a id="qca.managed.types.unrestricted_credential_networking_params.UnrestrictedCredentialNetworkingParams"></a>

## UnrestrictedCredentialNetworkingParams

```python
class UnrestrictedCredentialNetworkingParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/unrestricted_credential_networking_params.py)

<a id="qca.managed.types.unrestricted_credential_networking_params.UnrestrictedCredentialNetworkingParams.type"></a>

#### type

<a id="qca.managed.types.unrestricted_network_param"></a>

# qca.managed.types.unrestricted\_network\_param

<a id="qca.managed.types.unrestricted_network_param.UnrestrictedNetworkParam"></a>

## UnrestrictedNetworkParam

```python
class UnrestrictedNetworkParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/unrestricted_network_param.py)

<a id="qca.managed.types.unrestricted_network_param.UnrestrictedNetworkParam.type"></a>

#### type

<a id="qca.managed.types.url_document_source_param"></a>

# qca.managed.types.url\_document\_source\_param

<a id="qca.managed.types.url_document_source_param.URLDocumentSourceParam"></a>

## URLDocumentSourceParam

```python
class URLDocumentSourceParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/url_document_source_param.py)

<a id="qca.managed.types.url_document_source_param.URLDocumentSourceParam.type"></a>

#### type

<a id="qca.managed.types.url_document_source_param.URLDocumentSourceParam.url"></a>

#### url

<a id="qca.managed.types.url_image_source_param"></a>

# qca.managed.types.url\_image\_source\_param

<a id="qca.managed.types.url_image_source_param.URLImageSourceParam"></a>

## URLImageSourceParam

```python
class URLImageSourceParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/url_image_source_param.py)

<a id="qca.managed.types.url_image_source_param.URLImageSourceParam.type"></a>

#### type

<a id="qca.managed.types.url_image_source_param.URLImageSourceParam.url"></a>

#### url

<a id="qca.managed.types.urlmcp_server_params"></a>

# qca.managed.types.urlmcp\_server\_params

<a id="qca.managed.types.urlmcp_server_params.URLMCPServerParams"></a>

## URLMCPServerParams

```python
class URLMCPServerParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/urlmcp_server_params.py)

<a id="qca.managed.types.urlmcp_server_params.URLMCPServerParams.name"></a>

#### name

<a id="qca.managed.types.urlmcp_server_params.URLMCPServerParams.type"></a>

#### type

<a id="qca.managed.types.urlmcp_server_params.URLMCPServerParams.url"></a>

#### url

<a id="qca.managed.types.user_custom_tool_result_event_content_union"></a>

# qca.managed.types.user\_custom\_tool\_result\_event\_content\_union

<a id="qca.managed.types.user_custom_tool_result_event_content_union.UserCustomToolResultEventContentUnion"></a>

## UserCustomToolResultEventContentUnion

```python
class UserCustomToolResultEventContentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_custom_tool_result_event_content_union.py)

<a id="qca.managed.types.user_custom_tool_result_event_content_union.UserCustomToolResultEventContentUnion.text"></a>

#### text

<a id="qca.managed.types.user_custom_tool_result_event_content_union.UserCustomToolResultEventContentUnion.type"></a>

#### type

<a id="qca.managed.types.user_custom_tool_result_event_content_union.UserCustomToolResultEventContentUnion.source"></a>

#### source

<a id="qca.managed.types.user_custom_tool_result_event_content_union.UserCustomToolResultEventContentUnion.context"></a>

#### context

<a id="qca.managed.types.user_custom_tool_result_event_content_union.UserCustomToolResultEventContentUnion.title"></a>

#### title

<a id="qca.managed.types.user_custom_tool_result_event_content_union.UserCustomToolResultEventContentUnion.citations"></a>

#### citations

<a id="qca.managed.types.user_custom_tool_result_event_content_union.UserCustomToolResultEventContentUnion.content"></a>

#### content

<a id="qca.managed.types.user_custom_tool_result_event_params"></a>

# qca.managed.types.user\_custom\_tool\_result\_event\_params

<a id="qca.managed.types.user_custom_tool_result_event_params.UserCustomToolResultEventParams"></a>

## UserCustomToolResultEventParams

```python
class UserCustomToolResultEventParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_custom_tool_result_event_params.py)

<a id="qca.managed.types.user_custom_tool_result_event_params.UserCustomToolResultEventParams.custom_tool_use_id"></a>

#### custom\_tool\_use\_id

<a id="qca.managed.types.user_custom_tool_result_event_params.UserCustomToolResultEventParams.type"></a>

#### type

<a id="qca.managed.types.user_custom_tool_result_event_params.UserCustomToolResultEventParams.is_error"></a>

#### is\_error

<a id="qca.managed.types.user_custom_tool_result_event_params.UserCustomToolResultEventParams.content"></a>

#### content

<a id="qca.managed.types.user_define_outcome_event_params"></a>

# qca.managed.types.user\_define\_outcome\_event\_params

<a id="qca.managed.types.user_define_outcome_event_params.UserDefineOutcomeEventParams"></a>

## UserDefineOutcomeEventParams

```python
class UserDefineOutcomeEventParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_define_outcome_event_params.py)

<a id="qca.managed.types.user_define_outcome_event_params.UserDefineOutcomeEventParams.description"></a>

#### description

<a id="qca.managed.types.user_define_outcome_event_params.UserDefineOutcomeEventParams.rubric"></a>

#### rubric

<a id="qca.managed.types.user_define_outcome_event_params.UserDefineOutcomeEventParams.type"></a>

#### type

<a id="qca.managed.types.user_define_outcome_event_params.UserDefineOutcomeEventParams.max_iterations"></a>

#### max\_iterations

<a id="qca.managed.types.user_define_outcome_event_rubric_union"></a>

# qca.managed.types.user\_define\_outcome\_event\_rubric\_union

<a id="qca.managed.types.user_define_outcome_event_rubric_union.UserDefineOutcomeEventRubricUnion"></a>

## UserDefineOutcomeEventRubricUnion

```python
class UserDefineOutcomeEventRubricUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_define_outcome_event_rubric_union.py)

<a id="qca.managed.types.user_define_outcome_event_rubric_union.UserDefineOutcomeEventRubricUnion.file_id"></a>

#### file\_id

<a id="qca.managed.types.user_define_outcome_event_rubric_union.UserDefineOutcomeEventRubricUnion.type"></a>

#### type

<a id="qca.managed.types.user_define_outcome_event_rubric_union.UserDefineOutcomeEventRubricUnion.content"></a>

#### content

<a id="qca.managed.types.user_interrupt_event_params"></a>

# qca.managed.types.user\_interrupt\_event\_params

<a id="qca.managed.types.user_interrupt_event_params.UserInterruptEventParams"></a>

## UserInterruptEventParams

```python
class UserInterruptEventParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_interrupt_event_params.py)

<a id="qca.managed.types.user_interrupt_event_params.UserInterruptEventParams.type"></a>

#### type

<a id="qca.managed.types.user_interrupt_event_params.UserInterruptEventParams.session_thread_id"></a>

#### session\_thread\_id

<a id="qca.managed.types.user_location"></a>

# qca.managed.types.user\_location

<a id="qca.managed.types.user_location.UserLocation"></a>

## UserLocation

```python
class UserLocation(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_location.py)

<a id="qca.managed.types.user_location.UserLocation.type"></a>

#### type

<a id="qca.managed.types.user_location.UserLocation.city"></a>

#### city

<a id="qca.managed.types.user_location.UserLocation.country"></a>

#### country

<a id="qca.managed.types.user_location.UserLocation.region"></a>

#### region

<a id="qca.managed.types.user_location.UserLocation.timezone"></a>

#### timezone

<a id="qca.managed.types.user_location_param"></a>

# qca.managed.types.user\_location\_param

<a id="qca.managed.types.user_location_param.UserLocationParam"></a>

## UserLocationParam

```python
class UserLocationParam(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_location_param.py)

<a id="qca.managed.types.user_location_param.UserLocationParam.city"></a>

#### city

<a id="qca.managed.types.user_location_param.UserLocationParam.country"></a>

#### country

<a id="qca.managed.types.user_location_param.UserLocationParam.region"></a>

#### region

<a id="qca.managed.types.user_location_param.UserLocationParam.timezone"></a>

#### timezone

<a id="qca.managed.types.user_location_param.UserLocationParam.type"></a>

#### type

<a id="qca.managed.types.user_message_event_content_union"></a>

# qca.managed.types.user\_message\_event\_content\_union

<a id="qca.managed.types.user_message_event_content_union.UserMessageEventContentUnion"></a>

## UserMessageEventContentUnion

```python
class UserMessageEventContentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_message_event_content_union.py)

<a id="qca.managed.types.user_message_event_content_union.UserMessageEventContentUnion.text"></a>

#### text

<a id="qca.managed.types.user_message_event_content_union.UserMessageEventContentUnion.type"></a>

#### type

<a id="qca.managed.types.user_message_event_content_union.UserMessageEventContentUnion.source"></a>

#### source

<a id="qca.managed.types.user_message_event_content_union.UserMessageEventContentUnion.context"></a>

#### context

<a id="qca.managed.types.user_message_event_content_union.UserMessageEventContentUnion.title"></a>

#### title

<a id="qca.managed.types.user_message_event_content_union_source"></a>

# qca.managed.types.user\_message\_event\_content\_union\_source

<a id="qca.managed.types.user_message_event_content_union_source.UserMessageEventContentUnionSource"></a>

## UserMessageEventContentUnionSource

```python
class UserMessageEventContentUnionSource(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_message_event_content_union_source.py)

<a id="qca.managed.types.user_message_event_content_union_source.UserMessageEventContentUnionSource.data"></a>

#### data

<a id="qca.managed.types.user_message_event_content_union_source.UserMessageEventContentUnionSource.media_type"></a>

#### media\_type

<a id="qca.managed.types.user_message_event_content_union_source.UserMessageEventContentUnionSource.type"></a>

#### type

<a id="qca.managed.types.user_message_event_content_union_source.UserMessageEventContentUnionSource.url"></a>

#### url

<a id="qca.managed.types.user_message_event_content_union_source.UserMessageEventContentUnionSource.file_id"></a>

#### file\_id

<a id="qca.managed.types.user_message_event_params"></a>

# qca.managed.types.user\_message\_event\_params

<a id="qca.managed.types.user_message_event_params.UserMessageEventParams"></a>

## UserMessageEventParams

```python
class UserMessageEventParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_message_event_params.py)

<a id="qca.managed.types.user_message_event_params.UserMessageEventParams.content"></a>

#### content

<a id="qca.managed.types.user_message_event_params.UserMessageEventParams.type"></a>

#### type

<a id="qca.managed.types.user_tool_confirmation_event_params"></a>

# qca.managed.types.user\_tool\_confirmation\_event\_params

<a id="qca.managed.types.user_tool_confirmation_event_params.UserToolConfirmationEventParams"></a>

## UserToolConfirmationEventParams

```python
class UserToolConfirmationEventParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_tool_confirmation_event_params.py)

<a id="qca.managed.types.user_tool_confirmation_event_params.UserToolConfirmationEventParams.result"></a>

#### result

<a id="qca.managed.types.user_tool_confirmation_event_params.UserToolConfirmationEventParams.tool_use_id"></a>

#### tool\_use\_id

<a id="qca.managed.types.user_tool_confirmation_event_params.UserToolConfirmationEventParams.type"></a>

#### type

<a id="qca.managed.types.user_tool_confirmation_event_params.UserToolConfirmationEventParams.deny_message"></a>

#### deny\_message

<a id="qca.managed.types.user_tool_result_event_content_union"></a>

# qca.managed.types.user\_tool\_result\_event\_content\_union

<a id="qca.managed.types.user_tool_result_event_content_union.UserToolResultEventContentUnion"></a>

## UserToolResultEventContentUnion

```python
class UserToolResultEventContentUnion(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_tool_result_event_content_union.py)

<a id="qca.managed.types.user_tool_result_event_content_union.UserToolResultEventContentUnion.text"></a>

#### text

<a id="qca.managed.types.user_tool_result_event_content_union.UserToolResultEventContentUnion.type"></a>

#### type

<a id="qca.managed.types.user_tool_result_event_content_union.UserToolResultEventContentUnion.source"></a>

#### source

<a id="qca.managed.types.user_tool_result_event_content_union.UserToolResultEventContentUnion.context"></a>

#### context

<a id="qca.managed.types.user_tool_result_event_content_union.UserToolResultEventContentUnion.title"></a>

#### title

<a id="qca.managed.types.user_tool_result_event_content_union.UserToolResultEventContentUnion.citations"></a>

#### citations

<a id="qca.managed.types.user_tool_result_event_content_union.UserToolResultEventContentUnion.content"></a>

#### content

<a id="qca.managed.types.user_tool_result_event_params"></a>

# qca.managed.types.user\_tool\_result\_event\_params

<a id="qca.managed.types.user_tool_result_event_params.UserToolResultEventParams"></a>

## UserToolResultEventParams

```python
class UserToolResultEventParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/user_tool_result_event_params.py)

<a id="qca.managed.types.user_tool_result_event_params.UserToolResultEventParams.tool_use_id"></a>

#### tool\_use\_id

<a id="qca.managed.types.user_tool_result_event_params.UserToolResultEventParams.type"></a>

#### type

<a id="qca.managed.types.user_tool_result_event_params.UserToolResultEventParams.is_error"></a>

#### is\_error

<a id="qca.managed.types.user_tool_result_event_params.UserToolResultEventParams.content"></a>

#### content

<a id="qca.managed.types.vault"></a>

# qca.managed.types.vault

<a id="qca.managed.types.vault.Vault"></a>

## Vault

```python
class Vault(BaseModel)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault.py)

<a id="qca.managed.types.vault.Vault.id"></a>

#### id

<a id="qca.managed.types.vault.Vault.archived_at"></a>

#### archived\_at

<a id="qca.managed.types.vault.Vault.created_at"></a>

#### created\_at

<a id="qca.managed.types.vault.Vault.display_name"></a>

#### display\_name

<a id="qca.managed.types.vault.Vault.metadata"></a>

#### metadata

<a id="qca.managed.types.vault.Vault.type"></a>

#### type

<a id="qca.managed.types.vault.Vault.updated_at"></a>

#### updated\_at

<a id="qca.managed.types.vault_archive_params"></a>

# qca.managed.types.vault\_archive\_params

<a id="qca.managed.types.vault_archive_params.VaultArchiveParams"></a>

## VaultArchiveParams

```python
class VaultArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_archive_params.py)

<a id="qca.managed.types.vault_archive_params.VaultArchiveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_archive_params.VaultArchiveParams.betas"></a>

#### betas

<a id="qca.managed.types.vault_create_params"></a>

# qca.managed.types.vault\_create\_params

<a id="qca.managed.types.vault_create_params.VaultCreateParams"></a>

## VaultCreateParams

```python
class VaultCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_create_params.py)

<a id="qca.managed.types.vault_create_params.VaultCreateParams.display_name"></a>

#### display\_name

<a id="qca.managed.types.vault_create_params.VaultCreateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_create_params.VaultCreateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.vault_create_params.VaultCreateParams.betas"></a>

#### betas

<a id="qca.managed.types.vault_credential_archive_params"></a>

# qca.managed.types.vault\_credential\_archive\_params

<a id="qca.managed.types.vault_credential_archive_params.VaultCredentialArchiveParams"></a>

## VaultCredentialArchiveParams

```python
class VaultCredentialArchiveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_credential_archive_params.py)

<a id="qca.managed.types.vault_credential_archive_params.VaultCredentialArchiveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_credential_archive_params.VaultCredentialArchiveParams.betas"></a>

#### betas

<a id="qca.managed.types.vault_credential_create_params"></a>

# qca.managed.types.vault\_credential\_create\_params

<a id="qca.managed.types.vault_credential_create_params.VaultCredentialCreateParams"></a>

## VaultCredentialCreateParams

```python
class VaultCredentialCreateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_credential_create_params.py)

<a id="qca.managed.types.vault_credential_create_params.VaultCredentialCreateParams.auth"></a>

#### auth

<a id="qca.managed.types.vault_credential_create_params.VaultCredentialCreateParams.display_name"></a>

#### display\_name

<a id="qca.managed.types.vault_credential_create_params.VaultCredentialCreateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_credential_create_params.VaultCredentialCreateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.vault_credential_create_params.VaultCredentialCreateParams.betas"></a>

#### betas

<a id="qca.managed.types.vault_credential_delete_params"></a>

# qca.managed.types.vault\_credential\_delete\_params

<a id="qca.managed.types.vault_credential_delete_params.VaultCredentialDeleteParams"></a>

## VaultCredentialDeleteParams

```python
class VaultCredentialDeleteParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_credential_delete_params.py)

<a id="qca.managed.types.vault_credential_delete_params.VaultCredentialDeleteParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_credential_delete_params.VaultCredentialDeleteParams.betas"></a>

#### betas

<a id="qca.managed.types.vault_credential_list_params"></a>

# qca.managed.types.vault\_credential\_list\_params

<a id="qca.managed.types.vault_credential_list_params.VaultCredentialListParams"></a>

## VaultCredentialListParams

```python
class VaultCredentialListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_credential_list_params.py)

<a id="qca.managed.types.vault_credential_list_params.VaultCredentialListParams.name"></a>

#### name

<a id="qca.managed.types.vault_credential_list_params.VaultCredentialListParams.before_id"></a>

#### before\_id

<a id="qca.managed.types.vault_credential_list_params.VaultCredentialListParams.after_id"></a>

#### after\_id

<a id="qca.managed.types.vault_credential_list_params.VaultCredentialListParams.include_archived"></a>

#### include\_archived

<a id="qca.managed.types.vault_credential_list_params.VaultCredentialListParams.limit"></a>

#### limit

<a id="qca.managed.types.vault_credential_list_params.VaultCredentialListParams.page"></a>

#### page

<a id="qca.managed.types.vault_credential_list_params.VaultCredentialListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_credential_list_params.VaultCredentialListParams.betas"></a>

#### betas

<a id="qca.managed.types.vault_credential_mcpo_auth_validate_params"></a>

# qca.managed.types.vault\_credential\_mcpo\_auth\_validate\_params

<a id="qca.managed.types.vault_credential_mcpo_auth_validate_params.VaultCredentialMCPOAuthValidateParams"></a>

## VaultCredentialMCPOAuthValidateParams

```python
class VaultCredentialMCPOAuthValidateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_credential_mcpo_auth_validate_params.py)

<a id="qca.managed.types.vault_credential_mcpo_auth_validate_params.VaultCredentialMCPOAuthValidateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_credential_mcpo_auth_validate_params.VaultCredentialMCPOAuthValidateParams.betas"></a>

#### betas

<a id="qca.managed.types.vault_credential_retrieve_params"></a>

# qca.managed.types.vault\_credential\_retrieve\_params

<a id="qca.managed.types.vault_credential_retrieve_params.VaultCredentialRetrieveParams"></a>

## VaultCredentialRetrieveParams

```python
class VaultCredentialRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_credential_retrieve_params.py)

<a id="qca.managed.types.vault_credential_retrieve_params.VaultCredentialRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_credential_retrieve_params.VaultCredentialRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.vault_credential_update_params"></a>

# qca.managed.types.vault\_credential\_update\_params

<a id="qca.managed.types.vault_credential_update_params.VaultCredentialUpdateParams"></a>

## VaultCredentialUpdateParams

```python
class VaultCredentialUpdateParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_credential_update_params.py)

<a id="qca.managed.types.vault_credential_update_params.VaultCredentialUpdateParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_credential_update_params.VaultCredentialUpdateParams.metadata"></a>

#### metadata

<a id="qca.managed.types.vault_credential_update_params.VaultCredentialUpdateParams.auth"></a>

#### auth

<a id="qca.managed.types.vault_credential_update_params.VaultCredentialUpdateParams.betas"></a>

#### betas

<a id="qca.managed.types.vault_delete_params"></a>

# qca.managed.types.vault\_delete\_params

<a id="qca.managed.types.vault_delete_params.VaultDeleteParams"></a>

## VaultDeleteParams

```python
class VaultDeleteParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_delete_params.py)

<a id="qca.managed.types.vault_delete_params.VaultDeleteParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_delete_params.VaultDeleteParams.betas"></a>

#### betas

<a id="qca.managed.types.vault_list_params"></a>

# qca.managed.types.vault\_list\_params

<a id="qca.managed.types.vault_list_params.VaultListParams"></a>

## VaultListParams

```python
class VaultListParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_list_params.py)

<a id="qca.managed.types.vault_list_params.VaultListParams.name"></a>

#### name

<a id="qca.managed.types.vault_list_params.VaultListParams.before_id"></a>

#### before\_id

<a id="qca.managed.types.vault_list_params.VaultListParams.after_id"></a>

#### after\_id

<a id="qca.managed.types.vault_list_params.VaultListParams.include_archived"></a>

#### include\_archived

<a id="qca.managed.types.vault_list_params.VaultListParams.limit"></a>

#### limit

<a id="qca.managed.types.vault_list_params.VaultListParams.page"></a>

#### page

<a id="qca.managed.types.vault_list_params.VaultListParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_list_params.VaultListParams.betas"></a>

#### betas

<a id="qca.managed.types.vault_retrieve_params"></a>

# qca.managed.types.vault\_retrieve\_params

<a id="qca.managed.types.vault_retrieve_params.VaultRetrieveParams"></a>

## VaultRetrieveParams

```python
class VaultRetrieveParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/vault_retrieve_params.py)

<a id="qca.managed.types.vault_retrieve_params.VaultRetrieveParams.workspace_id"></a>

#### workspace\_id

<a id="qca.managed.types.vault_retrieve_params.VaultRetrieveParams.betas"></a>

#### betas

<a id="qca.managed.types.web_fetch_tool_config_params"></a>

# qca.managed.types.web\_fetch\_tool\_config\_params

<a id="qca.managed.types.web_fetch_tool_config_params.WebFetchToolConfigParams"></a>

## WebFetchToolConfigParams

```python
class WebFetchToolConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/web_fetch_tool_config_params.py)

<a id="qca.managed.types.web_fetch_tool_config_params.WebFetchToolConfigParams.enabled"></a>

#### enabled

<a id="qca.managed.types.web_fetch_tool_config_params.WebFetchToolConfigParams.max_content_tokens"></a>

#### max\_content\_tokens

<a id="qca.managed.types.web_fetch_tool_config_params.WebFetchToolConfigParams.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.web_fetch_tool_config_params.WebFetchToolConfigParams.allowed_domains"></a>

#### allowed\_domains

<a id="qca.managed.types.web_fetch_tool_config_params.WebFetchToolConfigParams.blocked_domains"></a>

#### blocked\_domains

<a id="qca.managed.types.web_fetch_tool_config_params.WebFetchToolConfigParams.type"></a>

#### type

<a id="qca.managed.types.web_fetch_tool_config_params.WebFetchToolConfigParams.name"></a>

#### name

<a id="qca.managed.types.web_search_tool_config_params"></a>

# qca.managed.types.web\_search\_tool\_config\_params

<a id="qca.managed.types.web_search_tool_config_params.WebSearchToolConfigParams"></a>

## WebSearchToolConfigParams

```python
class WebSearchToolConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/web_search_tool_config_params.py)

<a id="qca.managed.types.web_search_tool_config_params.WebSearchToolConfigParams.enabled"></a>

#### enabled

<a id="qca.managed.types.web_search_tool_config_params.WebSearchToolConfigParams.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.web_search_tool_config_params.WebSearchToolConfigParams.allowed_domains"></a>

#### allowed\_domains

<a id="qca.managed.types.web_search_tool_config_params.WebSearchToolConfigParams.blocked_domains"></a>

#### blocked\_domains

<a id="qca.managed.types.web_search_tool_config_params.WebSearchToolConfigParams.type"></a>

#### type

<a id="qca.managed.types.web_search_tool_config_params.WebSearchToolConfigParams.user_location"></a>

#### user\_location

<a id="qca.managed.types.web_search_tool_config_params.WebSearchToolConfigParams.name"></a>

#### name

<a id="qca.managed.types.write_tool_config_params"></a>

# qca.managed.types.write\_tool\_config\_params

<a id="qca.managed.types.write_tool_config_params.WriteToolConfigParams"></a>

## WriteToolConfigParams

```python
class WriteToolConfigParams(TypedDict)
```

[[view_source]](https://github.com/QoderAI/qoder-cloud-agents-sdk-python/blob/main/src/qca/managed/types/write_tool_config_params.py)

<a id="qca.managed.types.write_tool_config_params.WriteToolConfigParams.enabled"></a>

#### enabled

<a id="qca.managed.types.write_tool_config_params.WriteToolConfigParams.permission_policy"></a>

#### permission\_policy

<a id="qca.managed.types.write_tool_config_params.WriteToolConfigParams.type"></a>

#### type

<a id="qca.managed.types.write_tool_config_params.WriteToolConfigParams.name"></a>

#### name
