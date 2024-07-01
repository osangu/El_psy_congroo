from typing import Optional

from fastapi import Depends, Header
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials as Credentials

from .abc import Auth
from .basic import BasicAuth

access_token_capture = HTTPBearer()


class Authorization:

    @staticmethod
    def bearer(
            auth: Auth = Depends(BasicAuth),
            jwt: Credentials = Depends(access_token_capture)
    ) -> int:
        suffix, prefix = jwt.scheme, jwt.credentials

        return auth(suffix, prefix)

    @staticmethod
    def header(
            auth: Auth = Depends(BasicAuth),
            jwt: str = Header(alias='Authorization')
    ) -> int:
        suffix, prefix = jwt.split()

        return auth(suffix, prefix)
