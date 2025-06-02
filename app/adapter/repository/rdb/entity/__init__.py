from .user import UserEntity


def init(engine):
    _start_mappers()
    _create_table(engine)


def _start_mappers():
    from app.core import models

    user_mapper = UserEntity.mapper(
        model=models.User,
        properties={}
    )


def _create_table(engine):
    from .abc import Base

    Base.metadata.create_all(bind=engine)


__all__ = [
    'init',
    'UserEntity'
]
