from flask import Flask,Blueprint
from instance.config import app_configuration
from app.dbconn import create_tables
from flask_jwt_extended import JWTManager,get_raw_jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from app.api.v2.models.users_model import *
jwt = JWTManager()


def create_app(config_name):
    app=Flask(__name__)
    from app.api.v2 import blue as v2
    app.register_blueprint(v2)
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
    create_tables()
    jwt.init_app(app)


    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        blacklist = set()
        jti = decrypted_token['jti']
        return jti in blacklist


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



