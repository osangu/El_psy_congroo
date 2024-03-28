from fastapi import FastAPI, Request

from app.exception.auth import INVALID_JWT_EXCEPTION
from app.security.auth import AuthProperties


def check_token_expire(suffix):
    pass


def get_role(suffix):
    pass


def include_authorization_middleware(app: FastAPI):
    @app.middleware('http')
    async def authorization_middleware(request: Request, next_func):
        method = request.method
        path = request.scope.get('path')

        role_list = AuthProperties.role_list(path, method)

        if role_list is not None:

            prefix, suffix = request.headers.get('Authorization').split(' ')

            if prefix != "Bearer":
                raise INVALID_JWT_EXCEPTION  # return

            if check_token_expire(suffix):
                raise

            if get_role(suffix) not in role_list:
                raise

        return await next_func(request)
