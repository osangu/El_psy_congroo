from enum import Enum
from typing import List


class Tags(str, Enum):
    USER = 'User'


class SwaggerDetail(dict):
    tags: List[Tags]
    summary: str

    def __init__(self, summary: str, tags: List[Tags]):
        super().__init__()

        self.tags = tags
        self.summary = summary


class SwaggerDetails:
    login = SwaggerDetail(summary='로그인', tags=[Tags.USER])
    register = SwaggerDetail(summary='회원가입', tags=[Tags.USER])
    profile = SwaggerDetail(summary='내 정보 조회', tags=[Tags.USER])
