from fastapi import APIRouter, Depends

from .schema.request import UserRegisterRequest

from app.core.service.user import UserService
from ...security.auth import Authorization

user_router = APIRouter(prefix="/users")


@user_router.post(
    path='/register'
)
def user_sign_up(
        request: UserRegisterRequest,
        service: UserService.register = Depends(UserService.register)
):
    service(
        service.DTO(
            **request.model_dump()
        )
    )


@user_router.post(
    path='/login'
)
def user_login(
    request: None,
):
    pass


@user_router.get(
    path='/me'
)
def user_get_profile(
    user_id: int = Depends(Authorization.bearer)
):
    pass
