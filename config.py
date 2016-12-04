import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''
    TOKEN = 'wechat'
    APPID = 'wx4ab6faac2f0115a0'
    APPSECRET = '85f39901fd07df2f8b89b8675474b7d0'

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user:pass@localhost/dbname'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,

    'default': DevelopmentConfig
}
