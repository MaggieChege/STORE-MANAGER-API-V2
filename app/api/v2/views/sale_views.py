from datetime import datetime
from flask import request, jsonify, make_response
from flask_restful import Resource
from app.dbconn import Database_Connection
from app.api.v2.models.sale_models import Sale
from app.api.v2.views.products_views import Product
from app.api.v2.models.users_model import Users
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from app.api.v2.utils.schemas import sales_schema
from flask_expects_json import expects_json
from functools import wraps
from app.__init__ import *


class Sales(Resource):
    # def __init__(self):
    #     self.con=Database_Connection()
    #     self.cur=self.con.cursor()
    def get(self):
        sales = Sale.get_sales(self)
        if not sales:
            return make_response(jsonify({"message": "No sale record found"}))
        return make_response(jsonify({"sales":sales}),201)

    # @jwt_required
    def post(self):
        data =request.get_json()
        # sale_id = data['sale_id']
        user_email = get_jwt_identity()
        user=Users.fetch_by_email(user_email)
        product_id= data['product_id']
        quantity = data['quantity']
        attendant=data['attendant']

        if not product_id or not quantity or not attendant:
            return {"message": "All fields are required"},400


       

        product=Product.get_product_by_id(product_id)
        print("product",product)
        # print(product['quantity'])
        if not product:
            return {"message": "No product found"},404


        remaining_quantity=int(product[4]) - int(quantity)
        total_sale = int(product[3]) * int(quantity)
        price = product[3]
        date_created = datetime.now()
        product_id = product[0]


        if remaining_quantity < 0:
            return {"message": "Not enough in stock"}

        newsale = Sale(product_id,quantity,remaining_quantity,price,attendant,total_sale,date_created).create_sale()
       
        Sale.decrease_quantity(product_id,remaining_quantity)
        

        return make_response(jsonify(
            {"message":"Sale record created successfully"}), 201)


class DeleteSale(Resource):
    @jwt_required
    def delete(self,sale_id):
        claims = get_jwt_claims()
        if claims['role'] != 'Admin':
            return {"message":"Must be logged in as Admin"}

        Sale.delete_product(sale_id)
        return {"message":"Deleted successfully"}
    


class GetSaleId(Resource):
    def get(self,sale_id):
        
        sal = [sale for sale in sales if sale['sale_id'] == sale_id] or None
        if sal:
            return make_response(jsonify({'sale':sal[0]}),200)
        else:
            return jsonify({'message': "specific sale not found"})
            return 404