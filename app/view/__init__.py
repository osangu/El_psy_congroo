from fastapi import FastAPI


def include_routers(app: FastAPI) -> None:
    app.include_router(user_router)
