from flask import request, jsonify, make_response
from flask_restful import Resource
from app.dbconn import Database_Connection
from app.api.v2.models.products_models import Product,products

class Products(Resource):

    def get(self):
        dd =Product.get_product(self)
        
        if not dd:
            return make_response(jsonify({"message":"No Products.products"}),404)
        return make_response(jsonify({"message":"all product in the system","products":dd,"status":"okay"}),200)


    def post(self):

        product_id = request.json.get('product_id')
        product_name = request.json.get('product_name')
        category = request.json.get('category')
        price = request.json.get('price')
        quantity = request.json.get('quantity')
        if not product_name or product_name == "":
            return 404
        if not price or price == "":
            return 404
        if not quantity or quantity == "":
            return 404

        dd =Product.get_product(self)
        new = [product for product in dd if product ["product_name"] == product_name ]
        if new:
            return {"message": "Product exists"}
        check_id = [product for product in dd if product ["product_id"] == product_id ]   
        if check_id:
            return {"message":"A product with this Id exists"}
        if type((request.json['price']) or (request.json(quantity))) not in[int or float]:
            return{"message": "Must be a Number"}

        con =Database_Connection()
        cur=con.cursor()
        query = "INSERT INTO products(product_id,product_name,category,price,quantity) VALUES('{}','{}','{}','{}','{}');".format(product_id,product_name,category,price,quantity)
        cur.execute(query)
        con.commit()
        product = Product(product_id,product_name,category,price,quantity).create_product()
        products.append(product)
        return make_response(jsonify({'product':product}),201)
class DeleteProd(Resource):
    def delete(self,product_id):
        # db_products =Product.get_product(self)
        Product.delete_product(product_id)
        return {"message":"Deleted successfully"}

class Products_update(Resource):
    def put(self,product_id):
        data = request.get_json()
        prod_id = data["product_id"]
        product_name = data["product_name"]
        category = data["category"]
        price = data["price"]
        quantity = data["quantity"]

        query=Product(prod_id, product_name, category, price, quantity).update(product_id)

        return query