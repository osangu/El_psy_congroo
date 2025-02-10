import os


class CORSConfig:
    ORIGINS = os.environ['CORS_ALLOWED_ORIGINS']
    METHODS = os.environ['CORS_ALLOWED_METHODS']
    HEADERS = os.environ['CORS_ALLOWED_HEADERS']
