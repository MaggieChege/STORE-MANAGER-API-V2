from flask import request, jsonify, make_response
from flask_restful import Resource
from app.dbconn import Database_Connection
from app.api.v2.models.products_models import Product,products
from app.api.v2.models.users_model import Users
from app.api.v2.views.users_views import *
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

class Products(Resource):

    def get(self):
        dd =Product.get_product(self)
        
        if not dd:
            return make_response(jsonify({"message":"No Products.products"}),404)
        return make_response(jsonify({"message":"all product in the system","products":dd,"status":"okay"}),200)
    
    
    @jwt_required
    @admin_only
    def post(self):
        user = Users.fetch_by_role(get_jwt_identity())
        print(user)

        if not user ==  "Admin":
            return{"message":"Unauthorized access"},403



        data = request.get_json()
        product_name =data['product_name']
        category = data['category']
        price = data['price']
        quantity = data['quantity']

        required = [product_name,category,price,quantity]
        for n in required:
            if not n:
                return make_response(jsonify({"message": "Some required data fields are empty!"}))
        
        dd =Product.get_product(self)
        if dd:
            new = [product for product in dd if product["product_name"] == product_name]
            if new:
                return {"message": "Product exists"}
        

        
       
        if type((request.json['price']) or (request.json(quantity))) not in[int or float]:
            return{"message": "Must be a Number"}

        con =Database_Connection()
        cur=con.cursor()
        query = "INSERT INTO products(product_name,category,price,quantity) VALUES('{}','{}','{}','{}');".format(product_name,category,price,quantity)
        cur.execute(query)
        con.commit()
        product = Product(product_name,category,price,quantity).create_product()
        products.append(product)
        return make_response(jsonify({'product':product}),201)

class DeleteProd(Resource):
    
    def delete(self,product_id):
        # db_products =Product.get_product(self)
        Product.delete_product(product_id)
        return {"message":"Deleted successfully"}

class Products_update(Resource):
    @jwt_required
    @admin_only
    def put(self,product_id):
        data = request.get_json()
        # prod_id = data["product_id"]
        product_name = data["product_name"]
        category = data["category"]
        price = data["price"]
        quantity = data["quantity"]

        query=Product( product_name, category, price, quantity).update(product_id)

        return query

    