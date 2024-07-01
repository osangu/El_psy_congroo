from typing import Optional

from jwt import decode
from jwt.exceptions import ExpiredSignatureError
from jwt.exceptions import (InvalidKeyError,
                            InvalidTokenError,
                            InvalidSignatureError,
                            InvalidAlgorithmError)

from .data import Payload
from app.config import JWTConfig
from ...exception import FORBIDDEN_EXCEPTION


class Decoder:

    def __call__(self, jwt: str, key: str) -> Optional[Payload]:
        try:
            payload_dict = decode(jwt=jwt, key=key, algorithms=JWTConfig.ALGORITHM)

            return Payload(**payload_dict)

        except ExpiredSignatureError:
            raise FORBIDDEN_EXCEPTION("EXPIRED_REQUEST_ARRIVED")

        except (
                InvalidKeyError, InvalidSignatureError,
                InvalidTokenError, InvalidAlgorithmError
        ):
            raise FORBIDDEN_EXCEPTION("INVALID_REQUEST_ARRIVED")

    def access_token(self, jwt: str) -> Optional[Payload]:
        return self(jwt=jwt, key=JWTConfig.ACCESS_KEY)

    def refresh_token(self, jwt: str) -> Optional[Payload]:
        return self(jwt=jwt, key="")
