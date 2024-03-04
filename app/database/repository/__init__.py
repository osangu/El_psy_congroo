from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DatabaseConfig

from app.database.repository.user import UserDAO

engine = create_engine(DatabaseConfig.URL)
SessionLocal = sessionmaker(bind=engine)


class Repository:
    user = UserDAO(SessionLocal)
