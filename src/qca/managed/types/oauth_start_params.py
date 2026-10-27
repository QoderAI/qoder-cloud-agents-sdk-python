from typing_extensions import Required, TypedDict


class OAuthStartParams(TypedDict, total=False):
    vault_id: Required[str]
    mcp_server_url: Required[str]
    client_id: str
    client_secret: str
    workspace_id: str
