from pydantic import BaseModel


class UserRegisterResponse(BaseModel):
    name: str
    email: str

    access_token: str
    access_token_exp: float

    refresh_token: str
    refresh_token_exp: float


class UserProfileResponse(BaseModel):
    name: str
    email: str