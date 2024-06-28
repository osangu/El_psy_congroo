from pydantic import BaseModel


class Payload(BaseModel):
    sub: int
    exp: float

