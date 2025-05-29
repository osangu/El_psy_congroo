from contextlib import asynccontextmanager

import pytest_asyncio

from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from testcontainers.redis import RedisContainer
from testcontainers.postgres import PostgresContainer

from app import create_app

from app.adapter.repository.rdb import init_rdb_client
from app.adapter.repository.cache import init_cache_client


@pytest_asyncio.fixture(scope='session')
async def mock_postgres_url():
    with PostgresContainer() as postgres:
        yield postgres.get_connection_url()


@pytest_asyncio.fixture(scope='session')
async def mock_redis_conn_info():
    password = 'qwer1234!!'

    with RedisContainer(port=6379, password=password) as redis:
        host = redis.get_container_host_ip()
        port = redis.get_exposed_port(6379)

        yield host, port, password


@pytest_asyncio.fixture(scope='session')
async def client(
        mock_postgres_url,
        mock_redis_conn_info
):
    redis_host, redis_port, redis_password = mock_redis_conn_info

    @asynccontextmanager
    async def lifespan():
        init_rdb_client(mock_postgres_url)
        init_cache_client(redis_host, redis_port, redis_password)

        yield

    app = create_app(lifespan=lifespan)

    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url='https://test') as client:
            yield client
