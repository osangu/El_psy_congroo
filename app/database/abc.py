from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session

Base = declarative_base()


class DAO:

    def __init__(self, session_local: sessionmaker):
        self.session: Session
        self._session_local: sessionmaker

        self._session_local = session_local

    def __call__(self):
        with self._session_local as session:
            self.session: Session = session

            try:
                yield self

            except Exception as e:
                self.session.rollback()
                raise e

            finally:
                self.session.close()
