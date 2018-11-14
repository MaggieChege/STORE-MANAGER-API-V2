from flask import Flask,Blueprint
from app.dbconn import create_tables
from flask_jwt_extended import JWTManager,get_raw_jwt
from instance.config import app_config 
from flask_cors import CORS
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
    CORS(app)
    jwt.init_app(app)


    # @jwt.user_identity_loader
    # def user_identity_lookup(logged_user):
    #     '''set token identity for logged_user'''
    #     print(logged_user)
    #     return logged_user

    # @jwt.user_claims_loader
    # def add_claims_to_access_token(logged_user):
    #     '''This methods adds claims from logged_user'''
    #     return {'role': logged_user['role'],'user':logged_user['id']}

    @jwt.expired_token_loader
    def expired_handler():
        return jsonify({
            "Message": "Token has expired"

            })
    @jwt.token_in_blacklist_loader
    def check_blacklist(decrypted_token):
        '''check if token is in black list'''
        token = decrypted_token['jti']
        revoked_tokens = Users()
        return revoked_tokens.check_blacklist(token)





    @app.errorhandler(404)
    def not_found(e):
        # defining function
        return make_response(jsonify({
            "Message": "Route not found. Please check on the route"
        }), 404)

    @app.errorhandler(500)
    def internal_error(e):
        return make_response(jsonify({
            "Message": "Token has expired"
        }), 500)
    return app



   


    return app


