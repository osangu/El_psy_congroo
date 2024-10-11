from enum import Enum
from typing import List


class Tag(str, Enum):
    USER = "User"
    ALBUM = "Album"


class SwaggerDetail(dict):
    tags: List[Tag]
    summary: str

    def __init__(self, summary: str, tags: List[Tag]):
        super().__init__()

        self.tags = tags
        self.summary = summary


class SwaggerDetails:
    publish_album = SwaggerDetail(summary='음원 출판', tags=[Tag.ALBUM])
