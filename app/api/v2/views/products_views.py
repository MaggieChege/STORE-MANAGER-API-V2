from flask import request, jsonify, make_response
from flask_restful import Resource
from app.dbconn import Database_Connection
from app.api.v2.models.products_models import Product,products

class Products(Resource):
    def get(self):
        con =Database_Connection()
        cur=con.cursor()
        query = "SELECT * FROM products;"
        cur.execute(query)
        data = cur.fetchall()
        for k,v in enumerate(data):
            product_id,product_name,category, price, quantity=v
            prod = {"product_id":product_id,
            "product_name":product_name,
            "category":category,
            "quantity":quantity,
            "price":price}
            products.append(prod)
        if not prod:
            return make_response(jsonify({"message":"No products"}),200)
        return make_response(jsonify(products),201)


    def post(self):

        product_id = len(products)+1
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
        
        product = [product for product in products if product ["product_name"] == product_name ]
        if product:
            return {"message": "Product exists"}
        if type((request.json['price']) or (request.json(quantity))) not in[int or float]:
            return{"message": "Must be a Number"}
        con =Database_Connection()
        cur=con.cursor()
        query = "INSERT INTO products(product_id,product_name,category,price,quantity) VALUES (%s,%s,%s,%s,%s);"
        cur.execute(query,(product_id,product_name,category,price,quantity))
        con.commit()
        try:
            
            product = Product(product_id,product_name,category,price,quantity).create_product()
            products.append(product)
            return make_response(jsonify({'product':product}),201)
        except Exception as a:
            return {"message":a}


    def delete(self,product_id):
        '''delete product by id'''
        
        product=[product for product in products if product['product_id']==product_id]
        if not product:
            return make_response(jsonify({"message":"Product not found"}),200)
        else:
            con =Database_Connection()
            cur=con.cursor()
            query = "DELETE FROM products where product_id=%s;"
            cur.execute(query,(product_id))
            database.commit()
            return{"message":"Deleted successfully"}

class Get_product_id(Resource):
    
    def get(self,product_id):
        pro = [product for product in products if product['product_id'] == product_id] or None
        if pro:
            return jsonify({'product':pro[0]})
        else:
            return jsonify({'message': "specific product not found"})
