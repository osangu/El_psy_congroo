from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.orm import create_session, Session as SessionType

from app.config import DatabaseConfig

engine = create_engine(DatabaseConfig.URL)
session = create_session(bind=engine)

"""
session = scoped_session(
     sessionmaker(bind=engine)
)
"""


class DAO(ABC):

    def __init__(self, session: SessionType):
        self.session = session

    def __call__(self):
        try:
            with self.session:
                yield self
                self.session.commit()

        except Exception as e:
            self.session.rollback()
            raise e

        finally:
            self.session.close()
