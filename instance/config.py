import os


class Config():
	DEBUG = False
	SECRET_KEY="secret"
class DevelopmentConfig(Config):
	DEBUG= True
	APP_SET = "development"
	DATABASE_URL = "dbname='store' host='localhost' port='5432' user='postgres' password='root'"
	os.environ['ENVIRONMENT']="development"

class TestingConfig(Config):
    '''Testing app configurations'''
    TESTING = True
    DEBUG = True
    TESTING_DATABASE_URL ="dbname='store_tests' host='localhost' port='5432' user='postgres' password='root'"
class ProductionConfig(Config):
    """Production Config"""
    DEBUG = False
    TESTING = False



app_config={
	"development" : DevelopmentConfig,
	"testing": TestingConfig,
	"production":ProductionConfig
}

# secret_key = Config.SECRET