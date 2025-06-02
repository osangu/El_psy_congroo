from uuid import uuid4, UUID
from dataclasses import dataclass, field


@dataclass
class User:
    age: int
    sex: str
    name: str
    email: str
    password: str

    id: UUID = field(default_factory=uuid4)
