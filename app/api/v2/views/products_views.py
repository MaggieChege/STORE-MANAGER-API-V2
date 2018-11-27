from flask import request, jsonify, make_response
from flask_restful import Resource
from app.dbconn import Database_Connection
from app.api.v2.models.products_models import Product
from app.api.v2.models.users_model import Users
# from app.api.v2.views.users_views import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from app.api.v2.utils.schemas import products_schema
from flask_expects_json import expects_json
class Products(Resource):
    
    def get(self):
        # qua=Product.get_total_products(self)
        # for a in qua:
        #     print(a)
        # m = a[0]
        # print(m)

        # int(a)
        # n =sum(a)
        # print(n)
        dd =Product.get_product(self)

        if not dd:
            return make_response(jsonify({"message":"No Products.products"}),404)
        return make_response(jsonify({"message":"all product in the system","products":dd,"status":"okay"}),200)
    

    @jwt_required
    @expects_json(products_schema)
    def post(self):

        claims = get_jwt_claims()
        if claims['role'] != 'Admin':
            return {"message":"Must be logged in as Admin"},403


        data = request.get_json()
        product_name =data['product_name']
        category = data['category']
        price = data['price']
        quantity = data['quantity']
        
        if not product_name or not category or not price or not quantity:
            return( make_response(jsonify({
                "message": "All fields are required"
                }),400))

        if not product_name or product_name == "":
            return{"message":"Product Name is required"}
        if not category or category == "":
            return{"message":"Product Name is required"}
        if not price or price == "":
           return{"message":"Price is required"}
        if not quantity or quantity == "":
           return{"message":"Quantity is required"}
            



        dd =Product.get_product(self)
        if dd:
            new = [product for product in dd if product["product_name"] == product_name]
            if new:
                return({"message": "Product exists"})





        if type((data['price']) and (data['quantity'])) not in[int]:
            return {"message": "Must be a Number"}

        con =Database_Connection()
        cur=con.cursor()
        query = "INSERT INTO products(product_name,category,price,quantity) VALUES('{}','{}','{}','{}');".format(product_name,category,price,quantity)
        cur.execute(query)
        con.commit()
        product = Product(product_name,category,price,quantity).create_product()
        # products.append(product)
        return make_response(jsonify({'product':product}),201)


class DeleteProduct(Resource):
    
    @jwt_required
    def delete(self,product_id):

        claims = get_jwt_claims()
        if claims['role'] != 'Admin':
            return {"message":"Must be logged in as Admin"},403

        delete_product = Product.delete_product(product_id)
        if not delete_product:
            return {"message": "Product Does not exist"}
        return {"message":"Deleted successfully"}

class ProductsUpdate(Resource):
    @jwt_required
    @expects_json(products_schema)
    def put(self,product_id):

        claims = get_jwt_claims()
        if claims['role'] != 'Admin':
            return {"message":"Must be logged in as Admin"},403


        data = request.get_json()
        # prod_id = data["product_id"]
        product_name = data["product_name"]
        category = data["category"]
        price = data["price"]
        quantity = data["quantity"]

        query=Product( product_name, category, price, quantity).update(product_id)
        return{"message":"Product successfully updated","Product":data}
    

        return query

class SingleProduct(Resource):
    def get(self,product_id):
        single_product = Product.get_product_by_id(product_id)
    
        if not single_product:
            return make_response(jsonify({"message":"Product Does not exist"}),200)
        else:
            return single_product