from fastapi import APIRouter, Depends

from .schema.request import UserRegisterRequest
from ..swagger import SwaggerDetails

from app.core.service.user import UserService
from app.security.auth import Authorization

router = APIRouter(prefix="/users")


@router.post(
    **SwaggerDetails.register,
    response_model=None,
    status_code=202,
    path='/register',
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


@router.post(
    **SwaggerDetails.login,
    response_model=None,
    status_code=200,
    path='/login'
)
def user_login(
        request: None,
):
    pass


@router.get(
    path='/me'
)
def user_get_profile(
        user_id: int = Depends(Authorization.bearer)
):
    pass
