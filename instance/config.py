import os


class Config():
	DEBUG = False
	DATABASE_URL = os.getenv('DATABASE_URL')
class DevelopmentConfig(Config):
	DEBUG= True
	DATABASE_URL = "dbname='store' host='localhost' port='5432' user='postgres' password='root'"
	os.environ['ENV']="development"

class TestingConfig(Config):
    '''Testing app configurations'''
    TESTING = True
    DEBUG = True
    TESTING_DATABASE_URL ="dbname='store_tests' host='localhost' port='5432' user='postgres' password='root'"
class ProductionConfig(Config):
    """Production Config"""
    DEBUG = False
    TESTING = False



app_configuration={
	"development" : DevelopmentConfig,
	"testing": TestingConfig,
	"production":ProductionConfig,
	
}

# secret_key = Config.SECRET