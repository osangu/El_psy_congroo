from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, func
from sqlalchemy import CHAR, VARCHAR, Integer, DateTime

from .abc import Entity


class UserEntity(Entity):
    table_name = 'tbl_user'
    fields = (
        Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4),
        Column('age', Integer, nullable=True, default=None),
        Column('sex', CHAR(6), nullable=True, default=None),
        Column('name', VARCHAR(25), nullable=False),
        Column('email', VARCHAR(45), nullable=False, unique=True),
        Column('password', CHAR(60), nullable=False),
        Column('created_at', DateTime, nullable=False, insert_default=func.now),
    )
