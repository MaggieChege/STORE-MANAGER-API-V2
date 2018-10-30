from flask import request, jsonify, make_response
from flask_restful import Resource
from app.dbconn import Database_Connection
from app.api.v2.models.sale_models import Sale
from app.api.v2.views.products_views import Product


class Sales(Resource):
    def get(self):
        con =Database_Connection()
        cur=con.cursor()
        query = "SELECT * FROM sales;"
        cur.execute(query)
        data = cur.fetchall()
        
        for k,v in enumerate(data):
            sale_id,product_id,product_name,price,attendant,total_sale,quantity=v
            sal = {"sale_id": sale_id,
            "product_id":product_id,
            "product_name" : product_name,
            "price" : price,
            "attendant" : attendant,
            "total_sale" :total_sale,
            "quantity": quantity}
            sales.append(sal)
            if not sal:
                return make_response(jsonify({"message": "No sale record found"}))
            return make_response(jsonify({"sales":sales}),201)
    # @jwt_required
    def post(self):
        sale_id = len(sales)+1
        product_id = request.json.get('product_id')
        product_name = request.json.get('product_name')
        price = request.json.get('price')
        total_sale= request.json.get('total_sale')
        attendant = request.json.get("attendant")
        quantity = request.json.get('quantity')
        if not product_name or product_name == "":
            return 404
        

        con =Database_Connection()
        cur=con.cursor()
        con.commit()
        query = "INSERT INTO sales(sale_id,product_id,product_name,price,attendant,total_sale,quantity) VALUES (%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(query,(sale_id,product_id,product_name,price,attendant,total_sale,quantity))
        con.commit()

        product = [product for product in products if product ["product_name"] == product_name]
        if not product:
            return {"message": "Product does not exist"}

        sale = Sale(sale_id,product_id,product_name,price,attendant,total_sale,quantity).create_sale()
        if quantity > product[0]["quantity"]:
            return {"message": "Out of stock"}
        product[0]["quantity"] = product[0]["quantity"] - quantity
        return make_response(jsonify({'sale':sale}),201)
class Get_sale_id(Resource):
    def get(self,sale_id):
        sal = [sale for sale in sales if sale['sale_id'] == sale_id] or None
        if sal:
            return make_response(jsonify({'sale':sal[0]}),200)
        else:
            return jsonify({'message': "specific sale not found"})
            

        return 404