from sqlalchemy.orm import Session

from app.core.models import User
from app.abc.repository.user import UserRepository


class UserRepositoryImpl(UserRepository):

    @staticmethod
    def save(user: User, session: Session) -> User:
        pass