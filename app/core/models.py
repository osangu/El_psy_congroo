from datetime import datetime
from typing import List


class User:
    pass


class Album:
    name: str
    owner_id: int
    cover_image_path: str
    created_at: datetime

    @property
    def tracks(self):
        return []

    @property
    def titles(self):
        return []


class Track:
    album_id: int
    featuring: List[id, str]
    file_path: str

    is_title: bool
    is_rated: bool
