from typing import Optional

from app.core.model.user import User
from app.facade.orm.abc import DAO


class UserDAO(DAO):

    def save(self, user: User) -> User:
        self.session.add(user)
        self.session.flush()

        return user

    def find_by_id(self, user_id: int) -> Optional[User]:
        user = self.session.query(User).where(User.id == user_id).scalar()

        return user

    def find_by_email(self, email: str) -> Optional[User]:
        user = self.session.query(User).where(User.email == email).scalar()

        return user
