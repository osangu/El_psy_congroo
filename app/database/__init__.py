# SQLAlchemy
from sqlalchemy.engine import Engine

# Repository
from app.database.repository import engine, SessionLocal, Repository

# Model
from app.database.model import create_all
from app.database.model.user import User


def create_all_table(bind: Engine): create_all(bind)
