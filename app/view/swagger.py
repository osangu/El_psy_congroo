from enum import Enum
from typing import List


class Tags(str, Enum):
    USER = 'User'


class SwaggerDetail(dict):
    tags: List[Tags]
    summary: str


class SwaggerDetails:
    login = SwaggerDetail(summary='로그인', tags=[Tags.USER])
    register = SwaggerDetail(summary='회원가입', tags=[Tags.USER])
