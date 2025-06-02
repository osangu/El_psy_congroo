from abc import ABC, abstractmethod

from app.core.models.user import User


class UserRepository(ABC):

    @staticmethod
    @abstractmethod
    def save(user: User, _) -> User:
        raise NotImplementedError
