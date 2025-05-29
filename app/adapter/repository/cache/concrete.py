from typing import Optional

from redis import StrictRedis

from app.abc.repository.cache import CacheRepository


def init_cache_client(
        host: str,
        port: int,
        password: str
):
    CacheRepositoryImpl.client = StrictRedis(
        host=host,
        port=port,
        password=password
    )


class CacheRepositoryImpl(CacheRepository):
    client: Optional[StrictRedis] = None

    def save(self, *args, **kwargs):
        pass

    def save_with_ttl(self, *args, **kwargs):
        pass

    def find_by_key(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass
