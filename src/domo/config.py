"""Configuration pour les environnements de dev, de test et de production"""
import os
from pathlib import Path


HERE = Path(__file__).parent
SQLITE_DEV = "sqlite:///" + str(HERE / "domo_dev.db")
SQLITE_TEST = "sqlite:///" + str(HERE / "domo_test.db")
SQLITE_PROD = "sqlite:///" + str(HERE / "domo_prod.db")


class Config:
    """configuration par défaut"""

    SECRET_KEY = os.getenv("SECRET_KEY", "open me")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = SQLITE_TEST


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQLITE_DEV)


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQLITE_PROD)
    PRESERVE_CONTEXT_ON_EXCEPTION = True


ENV_CONFIG_DICT = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


def get_config(config_name):
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)
