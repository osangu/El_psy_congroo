from fastapi import Depends
from pydantic import BaseModel

from app.exception import ALREADY_EXIST_EXCEPTION
from app.facade.orm import Repository
from app.core.model.user import User
from app.security.token import JWTEncoder
from app.security.password import PasswordEncoder


class InputDTO(BaseModel):
    name: str
    email: str
    password: str


class OutPutDTO(BaseModel):
    name: str
    email: str

    access_token: str
    access_token_exp: float

    refresh_token: str
    refresh_token_exp: float


class UserRegister:
    Input = InputDTO
    OutPut = OutPutDTO

    def __init__(
            self,
            jwt_encoder: JWTEncoder = Depends(JWTEncoder),
            repository: Repository.user = Depends(Repository.user),
            password_encoder: PasswordEncoder = Depends(PasswordEncoder),
    ):
        self.repository = repository
        self.jwt_encoder = jwt_encoder
        self.password_encoder = password_encoder

    def __call__(self, dto: Input) -> OutPut:
        self._check_user_in_db(dto.email)

        hash_password = self.password_encoder(dto.password)
        user = self._create_user_and_save(dto, hash_password)

        access_token, access_exp = self.jwt_encoder.access_token(user.id)
        refresh_token, refresh_exp = self.jwt_encoder.refresh_token(user.id)

        return self.OutPut(
            name=user.name,
            email=user.email,
            access_token=access_token,
            access_token_exp=access_exp,
            refresh_token=refresh_token,
            refresh_token_exp=refresh_exp,
        )

    def _check_user_in_db(self, email: str):
        user_in_db = self.repository.find_by_email(email)

        if user_in_db is not None:
            raise ALREADY_EXIST_EXCEPTION("USER_ALREADY_EXIST")

    def _create_user_and_save(self, dto: Input, hash_password: str):
        user = User(name=dto.name, email=dto.email, password=hash_password)
        self.repository.save(user)

        return user
