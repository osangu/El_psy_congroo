from fastapi import Depends
from pydantic import BaseModel

from app.exception import NOT_FOUND_EXCEPTION
from app.facade.orm import Repository


class OutputDTO(BaseModel):
    name: str
    email: str


class UserProfile:
    Output = OutputDTO

    def __init__(
            self,
            user_repository: Repository.user = Depends(Repository.user)
    ):
        self.user_repository = user_repository

    def __call__(self, user_id: int) -> Output:
        user = self.user_repository.find_by_id(user_id)

        if user is None:
            raise NOT_FOUND_EXCEPTION("USER_NOT_FOUND")

        return self.Output(
            name=user.name,
            email=user.email
        )
