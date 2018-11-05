from flask import Flask,Blueprint
from instance.config import app_configuration
from app.dbconn import create_tables
from flask_jwt_extended import JWTManager
from jwt import ExpiredSignatureError, InvalidTokenError
from app.api.v2.models.users_model import *
jwt = JWTManager()


def create_app(config_name):
    app=Flask(__name__)
    from app.api.v2 import blue as v2
    app.register_blueprint(v2)
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    create_tables()
    jwt.init_app(app)


    return app


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
 user_email=identity
 user=Users.fetch_by_email(user_email)
 print(user)
 if user:
    if user == 'Admin':
        return {'roles': 'Admin'}
    else:
        return {'roles': 'User'}

@jwt.expired_token_loader
def expired_token_loader():
    return jsonify({
        'status': 401,
        'sub_status': 42,
        'msg': 'The token has expired'
    }), 401



