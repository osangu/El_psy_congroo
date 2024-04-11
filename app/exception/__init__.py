from typing import Optional
from http import HTTPStatus

from fastapi import HTTPException


class CustomException(HTTPException):

    def __init__(self, status_code: int, detail: Optional[str] = None):
        self.status_code = status_code
        self.detail = (detail
                       if detail
                       else HTTPStatus(status_code).name)

    def __call__(
            self,
            status_code: Optional[int] = None,
            detail: Optional[str] = None,
    ):
        if status_code:
            self.status_code = status_code

        if detail:
            self.detail = detail

        return self


NOT_FOUND_EXCEPTION = CustomException(404)
ALREADY_EXIST_EXCEPTION = CustomException(409)
INVALID_REQUEST_EXCEPTION = CustomException(422)
