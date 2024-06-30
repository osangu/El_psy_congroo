import os


class DatabaseConfig:
    _RDBMS = os.environ["DATABASE_RDBMS"]
    _DRIVER = os.environ["DATABASE_DRIVER"]

    _NAME = os.environ["DATABASE_NAME"]
    _HOST = os.environ["DATABASE_HOST"]
    _PORT = os.environ["DATABASE_PORT"]

    _USER_NAME = os.environ["DATABASE_USER_NAME"]
    _USER_PASSWORD = os.environ["DATABASE_USER_PASSWORD"]

    URL = f"{_RDBMS}+{_DRIVER}://{_USER_NAME}:{_USER_PASSWORD}:{_HOST}:{_PORT}/{_NAME}"


class JWTConfig:
    ALGORITHM = os.environ["JWT_ALGORITHM"]

    ACCESS = os.environ["JWT_ACCESS"]
    ACCESS_KEY = os.environ["JWT_ACCESS_KEY"]
    ACCESS_EXP = int(os.environ["JWT_ACCESS_EXPIRED_AT"])  # sec

    REFRESH = os.environ["JWT_REFRESH"]
    REFRESH_KEY = os.environ["JWT_REFRESH_KEY"]
    REFRESH_EXP = int(os.environ["JWT_REFRESH_EXP"])  # sec
