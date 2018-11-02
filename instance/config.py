import os


class Config():
	debug = False
	SECRET = os.getenv('SECRET')

class DevelopmentConfig(Config):
	debug= True
	DATABASE_URL = os.getenv('DATABASE_URL')

class TestingConfig(Config):
    '''Testing app configurations'''
    TESTING = True
    DEBUG = True
    connection_Variables ="dbname='store_test' user='postgres' host='localhost' password='Kwaziest.'"
    os.environ['ENVIRONMEMENT']="testing"
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