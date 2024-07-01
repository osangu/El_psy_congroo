from http import HTTPStatus
from typing import Optional

from fastapi import HTTPException


class PlayGroundException(HTTPException):

    def __init__(
            self,
            status_code: int,
            detail: Optional[str] = None
    ):
        self.status_code = status_code
        self.detail = (
            detail
            if detail is not None
            else HTTPStatus(status_code).name
        )

    def __call__(self, detail: Optional[str]):
        if detail is not None:
            self.detail = detail

        return self


# 400
FORBIDDEN_EXCEPTION = PlayGroundException(403)
NOT_FOUND_EXCEPTION = PlayGroundException(404)
ALREADY_EXIST_EXCEPTION = PlayGroundException(409)
