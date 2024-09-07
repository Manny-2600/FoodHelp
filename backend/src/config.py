import os


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my_precious"
    BCRYPT_LOG_ROUNDS = 13
    ACCESS_TOKEN_EXPIRATION = 900
    REFRESH_TOKEN_EXPIRATION = 2592000
    SQLALCHEMY_DATABASE_URI = "sqlite:///reddit_clone.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # # ADDED
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reddit_clone.db"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


class DevelopmentConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = "sqlite:///reddit_clone.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    url = os.environ.get("DATABASE_URL")

    if url is not None and url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = url
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
