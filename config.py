import os

class Config:

    '''
    class config
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://alinur:admin@localhost/pitch'
    SECRET_KEY=os.environ.get("SECRET_KEY")


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'): 
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://','postgresql://',1)
    SECRET_KEY = os.environ.get('SECRET_KEY')


    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USE_SSL = True
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")










class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alinur:admin@localhost/pitch_test'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alinur:admin@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'test':TestConfig,
'production':ProdConfig
}