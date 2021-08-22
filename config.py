import os


class Config:
    DEBUG = False
    TESTING = False

    API_TITLE = "Flask Library"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_URL_PREFIX = "/api"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    JSON_AS_ASCII = False

    SQLALCHEMY_DATABASE_URI = DATABASE_URL = os.getenv('DATABASE_URL',
                                                       'postgresql://postgres:example@localhost/postgres').replace(
        "postgres://", "postgresql://")

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DebugConfig(Config):
    DEBUG = True
    TESTING = True
