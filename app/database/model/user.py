from sqlalchemy import Column, Integer, Text

from app.database.abc import Base


class User(Base):
    __tablename__ = "tbl_user"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    email = Column("email", Text, nullable=False)
    password = Column("password", Text, nullable=False)
