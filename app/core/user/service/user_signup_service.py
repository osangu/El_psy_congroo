from fastapi import Depends

from app.database.repository.user import UserRepository


class UserSignUpService:

    def __init__(self, repository: UserRepository = Depends(UserRepository)):
        self.repository = repository

    def execute(self, request):
        pass
