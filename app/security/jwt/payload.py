from dataclasses import dataclass
from typing import List

EXP = "exp"
SUB = "sub"
ROLE = "role"
TYPE = "type"


@dataclass
class Payload:
    exp: str
    sub: str
    role: List[str]
    type: str
