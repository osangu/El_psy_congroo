from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import DatabaseConfig

Base = declarative_base()
engine = create_engine(DatabaseConfig.URL)
LocalSession = sessionmaker(bind=engine)
