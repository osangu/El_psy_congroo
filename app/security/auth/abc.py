from abc import ABC, abstractmethod
from typing import Any, Union, Callable


class Authorization(ABC):

    def __init__(self, jwt_decoder):
        self.jwt_decoder = jwt_decoder

    @abstractmethod
    def __call__(self, token: Callable[[Any], str]):  # access_token
        return self._validate(token)

    @abstractmethod
    def refresh_token(self, token: Callable[[Any], str]):
        return self._validate(token)

    def _validate(self, token: str):
        prefix, suffix = token.split()
        _, payload = (
            self._validate_prefix(prefix),
            self._validate_suffix(suffix)
        )
        return payload

    @staticmethod
    def _validate_prefix(prefix: Union[str, Any]):  # TODO
        assert prefix.lower() == "bearer"

    def _validate_suffix(self, suffix):
        pass
