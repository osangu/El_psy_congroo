from jwt import decode
from jwt.exceptions import (
    ExpiredSignatureError,
    InvalidSignatureError,
    InvalidKeyError,
    InvalidAlgorithmError,
)

from app.config import JWTConfig
from app.security.jwt.payload import Payload
from app.exception.auth import EXPIRED_JWT_EXCEPTION, INVALID_JWT_EXCEPTION


class Decoder:

    @staticmethod
    def __decode(jwt_token: str, key: str) -> Payload:
        try:
            claims = decode(
                key=key,
                jwt=jwt_token,
                algorithms=JWTConfig.ALGORITHM
            )
            return Payload(**claims)

        except ExpiredSignatureError:
            raise EXPIRED_JWT_EXCEPTION

        except (
                InvalidAlgorithmError,
                InvalidSignatureError,
                InvalidKeyError
        ):
            raise INVALID_JWT_EXCEPTION

    @staticmethod
    def access_token(jwt_token: str) -> Payload:
        key = JWTConfig.ACCESS_KEY

        return Decoder.__decode(jwt_token, key)

    @staticmethod
    def refresh_token(jwt_token) -> Payload:
        key = JWTConfig.REFRESH_KEY

        return Decoder.__decode(jwt_token, key)
