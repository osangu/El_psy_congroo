from contextlib import contextmanager
from typing import Optional

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


class Client:
    session: Optional[sessionmaker] = None

    @contextmanager
    def session_scope(self):
        with self.session() as session:
            try:
                yield session
                session.commit()
            except Exception as e:
                session.rollback()
                raise e


def init_rdb_client(
        host: str = None,
        port: str = None,
        name: str = None,
        username: str = None,
        password: str = None,
        url: str = None,
        init_table: bool = False
):
    if not url:
        url = ''

    engine = create_engine(url)
    Client.session = sessionmaker(bind=engine, autoflush=False)

    if init_table:
        _create_table(engine)


def _create_table(engine):
    pass
