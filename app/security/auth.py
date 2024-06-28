from fastapi import Depends, Header
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials as Credentials

from .token import JWTDecoder

access_token_capture = HTTPBearer()


class Authorization:

    def __init__(self, decoder: JWTDecoder = Depends(JWTDecoder)):
        self.decoder = decoder

    def __call__(self, jwt_prefix: str) -> int:
        user_id = self.decoder.access_token(jwt_prefix)

        # check in redis

        return user_id

    def header(self, jwt: str = Header(alias='Authorization')):
        suffix, prefix = jwt.split(' ')

        self.check_suffix(suffix)

        return self(prefix)

    def bearer(self, jwt: Credentials = Depends(access_token_capture)):
        suffix, prefix = jwt.scheme, jwt.credentials

        self.check_suffix(suffix)

        return self(prefix)

    @staticmethod
    def check_suffix(suffix: str):
        suffix = suffix.lower()

        assert suffix == 'bearer'
