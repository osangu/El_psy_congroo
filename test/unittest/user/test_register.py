from pytest import raises
from fastapi import Depends

from app.core.service.user import UserService


class TestUserRegister:

    def __init__(
            self,
            service: UserService = Depends(UserService.register)
    ):
        self.service = service

    def test_success_register(self):
        pass

    def test_fail_user_already_exist(self):
        pass
