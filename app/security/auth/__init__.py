from dataclasses import dataclass

from fastapi import Depends

from app.security.auth.role import Role
from app.security.jwt.decoder import Decoder

from app.security.jwt.payload import Payload


@dataclass
class AuthInfo:
    role: Role
    user_id: int


def authorization(jwt_token: str = Depends()) -> AuthInfo:
    payload: Payload = Decoder.access_token(jwt_token)

    return AuthInfo(
        user_id=payload.sub,
        role=Role(payload.role)
    )
