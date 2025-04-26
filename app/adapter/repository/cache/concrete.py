from typing import Optional

from redis import StrictRedis

from app.abc.repository.cache import CacheRepository


class CacheRepositoryImpl(CacheRepository):

    @staticmethod
    def __init__(
            host: str,
            port: str,
            password: str,
            client: Optional[str] = None
    ):
        if client is None:
            client = StrictRedis(
                host=host,
                port=port,
                password=password
            )

        CacheRepositoryImpl.client = client

    client: StrictRedis = None

    def save(self, *args, **kwargs):
        pass

    def save_with_ttl(self, *args, **kwargs):
        pass

    def find_by_key(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass
