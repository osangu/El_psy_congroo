from fastapi import APIRouter, Depends

from app.core.user.service import UserService

user_router = APIRouter(prefix="/users")


@user_router.post("/sign-up")
def user_register(
        request: UserSignUpRequest,
        service: UserService.sign_up = Depends(UserService.sign_up)
):
    service.execute()
