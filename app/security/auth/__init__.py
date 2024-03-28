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


class AuthProperties:
    _authorization_url = {
        "/users/token": {
            "PUT": [Role.USER]
        },
        "/users/me": {
            "GET": [Role.USER]
        }
    }

    @staticmethod
    def role_list(path: str, method: str):
        method_dict = AuthProperties._authorization_url.get(path)

        if method_dict is None:
            return None

        return method_dict.get(method)

        # return None if method_dict is None else method_dict.get(path)
