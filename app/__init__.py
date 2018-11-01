from flask import Flask,Blueprint
from instance.config import app_configuration
from app.dbconn import create_tables
from flask_jwt_extended import JWTManager

def create_app(config_name):
    app=Flask(__name__)
    from app.api.v2 import blue as v2
    app.register_blueprint(v2)
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    jwt = JWTManager(app)
    create_tables()
    # app.config.from_object(app_configuration[config_name])
    # # app.config.from_pyfile('config.py')
    # application_database_connection = DatabaseConn(config_name)
    # application_database_connection.create_table()
    




    return app
