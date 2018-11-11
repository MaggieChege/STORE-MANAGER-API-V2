from flask import Flask,Blueprint
from flask_jwt_extended import JWTManager
# from app.api.v2.models.users_model import *
from app.dbconn import Database_Connection
from instance.config import app_config 


db = Database_Connection()



def create_app(config_name):
    app=Flask(__name__,instance_relative_config=True)
    jwt = JWTManager(app)
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    # app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)


    from app.api.v2 import blue as v2
    app.register_blueprint(v2)
    return app


