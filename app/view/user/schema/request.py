from pydantic import BaseModel


class UserRegisterRequest(BaseModel):
    name: str
    email: str
    password: str

    # validation,
