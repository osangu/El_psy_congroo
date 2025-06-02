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


# TODO: set params default as RDBConfig
def init_rdb(
        host: str,
        port: str,
        name: str,
        username: str,
        password: str,
        url: str = None,
        dbms: str = 'postgres',
        driver: str = 'psycopg2'
):
    from . import entity

    if url is None:
        url = f'{dbms}+{driver}://{username}:{password}@{host}:{port}/{name}'

    engine = create_engine(url)

    entity.init(engine=engine)

    Client.session = sessionmaker(bind=engine, autoflush=False)
