from qca.common._models import BaseModel


class OAuthStartResponse(BaseModel):
    authorization_url: str
    state: str
    callback_origin: str
