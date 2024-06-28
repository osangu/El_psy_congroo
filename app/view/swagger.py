from enum import Enum
from typing import List

from pydantic import BaseModel


class Tags(str, Enum):
    USER = 'User'


class SwaggerDetail(BaseModel):
    tags: List[Tags]
    summary: str


class SwaggerDetails:
    register = SwaggerDetail(summary='회원가입', tags=[Tags.USER])
    login = SwaggerDetail(summary='로그인', tags=[Tags.USER])
