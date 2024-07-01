from abc import ABC, abstractmethod

from fastapi import Depends

from ..token import JWTDecoder


class Auth(ABC):

    @abstractmethod
    def __init__(self, jwt_decoder: JWTDecoder = Depends(JWTDecoder)):
        self.jwt_decoder = jwt_decoder

    @abstractmethod
    def __call__(self, suffix: str, prefix: str):
        raise NotImplementedError

    @abstractmethod
    def validate_suffix(self, suffix: str):
        raise NotImplementedError

    @abstractmethod
    def validate_prefix(self, prefix: str):
        raise NotImplementedError
