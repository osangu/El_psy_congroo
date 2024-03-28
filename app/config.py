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


class JWTConfig:
    ALGORITHM = os.environ["JWT_ALGORITHM"]

    ACCESS = os.environ["JWT_ACCESS_CLAIM"]
    ACCESS_KEY = os.environ["JWT_ACCESS_KEY"]
    ACCESS_EXP_SEC = os.environ["JWT_ACCESS_EXP_SEC"]

    REFRESH = os.environ["JWT_REFRESH_CLAIM"]
    REFRESH_KEY = os.environ["JWT_REFRESH_KEY"]
    REFRESH_EXP_SEC = os.environ["JWT_REFRESH_EXP_SEC"]
