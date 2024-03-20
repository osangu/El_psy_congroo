import os


class DatabaseConfig:

    DBMS = os.environ['DATABASE_SYSTEM']
    DRIVER = os.environ['DATABASE_DRIVER']

    NAME = os.environ['DATABASE_NAME']
    HOST = os.environ['DATABASE_HOST']
    PORT = os.environ['DATABASE_PORT']

    USER_NAME = os.environ['DATABASE_USER_NAME']
    USER_PASSWORD = os.environ['DATABASE_USER_PASSWORD']

    URL = f'{DBMS}+{DRIVER}://{USER_NAME}:{USER_PASSWORD}@{HOST}:{PORT}/{NAME}'
