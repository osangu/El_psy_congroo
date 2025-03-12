from uuid import UUID
from typing import Annotated
from dataclasses import dataclass


@dataclass
class User:
    id: Annotated[str, UUID]
    name: str
    password: str

    def __eq__(self, other: "User"):
        return str(self.id) == str(other.id)


@dataclass
class Post:
    id: int
    user_id: Annotated[str, UUID]
    title: str
    content: str