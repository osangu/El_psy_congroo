from fastapi import Depends

from .abc import Auth
from ..token import JWTDecoder, Payload


class BasicAuth(Auth):

    def __init__(self, jwt_decoder: JWTDecoder = Depends(JWTDecoder)):
        self.jwt_decoder = jwt_decoder

    def __call__(self, suffix: str, prefix: str):
        self.validate_suffix(suffix)

        return self.validate_prefix(prefix)

    def validate_suffix(self, suffix: str):
        suffix = suffix.lower()

        assert suffix == 'bearer'

    def validate_prefix(self, prefix: str):
        payload: Payload = self.jwt_decoder.access_token(prefix)

        return payload.sub
