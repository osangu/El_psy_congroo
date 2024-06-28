from fastapi import FastAPI
from .user import user_router


def include_routers(app: FastAPI) -> None:
    app.include_router(user_router)
