from flask import Flask,Blueprint
from app.dbconn import create_tables
from flask_jwt_extended import JWTManager,get_raw_jwt
from instance.config import app_config 
from app.api.v2.models.users_model import *
jwt = JWTManager()


def create_app(config_name):
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py')
    # app.config.from_object(app_config[config_name])
    from app.api.v2 import blue as v2
    app.register_blueprint(v2)
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
    create_tables()
    jwt.init_app(app)


   


    return app


