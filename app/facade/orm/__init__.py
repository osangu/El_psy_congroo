from app.facade.orm.user import UserDAO
from .abc import session


class Repository:
    user: UserDAO = UserDAO(session=session)
