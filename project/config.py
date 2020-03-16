import os


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = "default"
    SECRET_KEY = "my_precious"


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.environ.get("APP_SECRET")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
