from sqlalchemy import Column, Integer, String

from .abc import Base


class User(Base):
    __tablename__ = 'tbl_user'

    id = Column(Integer, primary_key=True)
    name = Column(String(5), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
