class Config:
    TESTING = False


class ProductionConfig(Config):
    DATABASE_URI = "mysql://user@localhost/foo"


class DevelopmentConfig(Config):
    DATABASE_URI = "sqlite:////tmp/foo.db"


class TestingConfig(Config):
    DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
