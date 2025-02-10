from contextlib import asynccontextmanager
from typing import Callable
from fastapi import FastAPI

from .security import include_cors_middleware


def create_app(lifespan: Callable):
    app = FastAPI(lifespan=lifespan)

    """
    lifespan -  for infra (db, mq, ...)
    create_app - for own app features
    """

    # include_routers()
    include_cors_middleware(app)

    return app


@asynccontextmanager
def lifespan(_: FastAPI):
    # init_document_db()
    # init_rdb()

    yield

    # cleaning some stuff
