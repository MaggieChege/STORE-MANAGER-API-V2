from flask import request, jsonify, make_response
from flask_restful import Resource
# from app.dbconn import Database_Connection
from app.api.v2.models.products_models import Product
from app.api.v2.models.users_model import Users
from app.api.v2.views.users_views import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.v2.utils.schemas import products_schema
from flask_expects_json import expects_json


from app import db
con = db.con
cur = db.cursor

class Products(Resource):
    
    def get(self):
        dd =Product.get_product(self)

        if not dd:
            return make_response(jsonify({"message":"No Products.products"}),404)
        return make_response(jsonify({"message":"all product in the system","products":dd,"status":"okay"}),200)
    

    # @jwt_required
    # @admin_required
    @expects_json(products_schema)
    def post(self):
        data = request.get_json()
        product_name =data['product_name']
        category = data['category']
        price = data['price']
        quantity = data['quantity']
        if not product_name or product_name == "":
            return {"message":"Product Name is required"}
        if not category or category == "":
            return {"message":"Product Name is required"}
        if not price or price == "":
            return {"message":"Product Name is required"}
        if not quantity or quantity == "":
            return {"message":"Product Name is required"}



        dd =Product.get_product(self)
        if dd:
            new = [product for product in dd if product["product_name"] == product_name]
            if new:
                return {"message": "Product exists"}




        if type((request.json['price']) or (request.json(quantity))) not in[int or float]:
            return{"message": "Must be a Number"}

        # con =Database_Connection()
        # cur=con.cursor()
        query = "INSERT INTO products(product_name,category,price,quantity) VALUES('{}','{}','{}','{}');".format(product_name,category,price,quantity)
        cur.execute(query)
        con.commit()
        product = Product(product_name,category,price,quantity).create_product()
        # products.append(product)
        return make_response(jsonify({'product':product}),201)


class DeleteProd(Resource):
    
    # @jwt_required
    # @admin_required
    def delete(self,product_id):
        # db_products =Product.get_product(self)
        Product.delete_product(product_id)
        return {"message":"Deleted successfully"}

class Products_update(Resource):
    # @jwt_required
    # @admin_required
    @expects_json(products_schema)
    def put(self,product_id):
        data = request.get_json()
        # prod_id = data["product_id"]
        product_name = data["product_name"]
        category = data["category"]
        price = data["price"]
        quantity = data["quantity"]

        query=Product( product_name, category, price, quantity).update(product_id)
        return{"message":"Product successfully updated","Product":data}
        # print(data)

        return query

class Single_product(Resource):
    def get(self,product_id):
        single_product = Product.get_product_by_id(product_id)
        print(single_product)
        if not single_product:
            return make_response(jsonify({"message":"Product Does not exist"}),200)
        else:
            return single_product
