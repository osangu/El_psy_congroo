from typing import List

from pydantic import BaseModel


class AlbumDistributeRequest(BaseModel):
    name: str
    titles: List[int]

