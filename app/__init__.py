from typing import Callable, Optional

from fastapi import FastAPI


def create_app(lifespan: Optional[Callable] = None) -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    return app
