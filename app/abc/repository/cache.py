from typing import Any, Optional
from abc import ABC, abstractmethod


class CacheRepository(ABC):

    @abstractmethod
    def save(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def save_with_ttl(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def find_by_key(self, *args, **kwargs):
        # ! Notice !
        # Have to decode after find value
        raise NotImplementedError

    @abstractmethod
    def delete(self, *args, **kwargs):
        raise NotImplementedError
