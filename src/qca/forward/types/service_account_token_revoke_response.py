from qca.common._models import BaseModel

__all__ = ["ServiceAccountTokenRevokeResponse"]


class ServiceAccountTokenRevokeResponse(BaseModel):
    revoked: bool
