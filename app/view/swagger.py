from enum import Enum
from typing import List


class Tags(str, Enum):
    USER = "User"
    ALBUM = "Album"


class SwaggerDetail(dict):
    tags: List[Tags]
    summary: str

    def __init__(self, summary: str, tags: List[Tags]):
        super().__init__()

        self.tags = tags
        self.summary = summary


class SwaggerDetails:
    publish_album = SwaggerDetail(summary='음원 출판', tags=[Tags.ALBUM])
