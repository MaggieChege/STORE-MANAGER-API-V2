from flask import Flask,Blueprint
from app.dbconn import create_tables
from flask_jwt_extended import JWTManager
from instance.config import app_config 
from flask_cors import CORS
from app.api.v2.models.users_model import *
from flask_restful import Api,Resource
from datetime import timedelta

# from app.api.v2.views.products_views import Products,Get_product_id
from app.api.v2.views.products_views import Products,DeleteProduct,ProductsUpdate,SingleProduct
from app.api.v2.views.sale_views import *
# Sales,Get_sale_id,DeleteSale
from app.api.v2.views.users_views import UserRegistration,UserLogin,Logout,AllUsers
# Register your resources here
blue = Blueprint("api", __name__, url_prefix="/api/v2")
api=Api(blue)



def create_app(config_name):
# ,instance_relative_config=True
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.config.from_object(app_config['development'])
    create_tables()
    CORS(app)

    # from app.api.v2 import blue as v2

    app.register_blueprint(blue)
    api.add_resource(Products,"/products")
    api.add_resource(SingleProduct,"/products/<int:product_id>")
    api.add_resource(UserLogin,"/users/login")
    api.add_resource(UserRegistration,"/auth/user")
    api.add_resource(Sales,"/sales")
    # api.add_resource(Deletesale,"/sales/<int:sale_id>")
    api.add_resource(GetSaleId,"/sales/<int:product_id>")
    api.add_resource(DeleteProduct,"/products/<int:product_id>")
    api.add_resource(ProductsUpdate,"/products/<int:product_id>")
    api.add_resource(Logout,'/users/logout')
    api.add_resource(AllUsers,"/users")

    jwt = JWTManager(app)

    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
    # app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=72)



    @jwt.token_in_blacklist_loader
    def check_blacklist(decrypted_token):
        '''check if token is in black list'''
        token = decrypted_token['jti']
        revoked_tokens = Users()
        return revoked_tokens.check_blacklist(token)


    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user[2]

    @jwt.user_claims_loader
    def user_claims_check(user):
        return {'role':user[4]}


    @jwt.expired_token_loader
    def my_expired_token_callback():
        return jsonify({
            'message': 'The token has expired'
        }), 401

    @jwt.expired_token_loader
    def my_expired_token_callback():
        return jsonify({
            'status': 401,
            'sub_status': 42,
            'msg': 'The token has expired'
        }), 401


    @app.errorhandler(404)
    def not_found(e):
        # defining function
        return make_response(jsonify({
            "Message": "Route not found. Please check on the route"
        }), 404)
    
    return app


