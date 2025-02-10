from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import CORSConfig


def include_cors_middleware(app: FastAPI):
    origins = CORSConfig.ORIGINS.split(',')
    methods = CORSConfig.METHODS.split(',')
    headers = CORSConfig.HEADERS.split(',')

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=methods,
        allow_headers=headers,
        allow_credentials=True,
    )
