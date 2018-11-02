from datetime import datetime
from flask import request, jsonify, make_response
from flask_restful import Resource
from app.dbconn import Database_Connection
from app.api.v2.models.sale_models import Sale
from app.api.v2.views.products_views import Product
from app.api.v2.views.users_views import admin_only
from app.api.v2.models.users_model import Users
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from app.api.v2.utils.schemas import sales_schema
from flask_expects_json import expects_json
from functools import wraps


class Sales(Resource):
    def get(self):
        sales = Sale.get_sales(self)
        if not sales:
            return make_response(jsonify({"message": "No sale record found"}))
        return make_response(jsonify({"sales":sales}),201)

    def post(self):
        data =request.get_json()
        # sale_id = data['sale_id']
        product_name= data['product_name']
        quantity = data['quantity']
        attendant=data['attendant']

       

        product=Product.get_product_name(product_name)
        if not product:
            return {"message": "No product found"},404


        price = product[1]
        remaining_quantity=int(product[4]) - int(quantity)
        total_sale = int(product[3]) * int(quantity)
        price = product[3]
        date_created = datetime.now()
        product_id = product[0]


        if remaining_quantity < 0:
            return {"message": "Not enough in stock"}

        newsale = Sale(product_id,quantity,remaining_quantity,price,product_name,attendant,date_created).create_sale()
        print(newsale)
        Sale.decrease_quantity(product_id,remaining_quantity)
        

        return make_response(jsonify(
            {"message":"Sale record created successfully"}), 201)

        # data =request.get_json()
        # product_id=data['product_id']
        # quantity = data['quantity']
        # attendant=data['attendant']

       

        # product=get_product_by_id(product_id)
        # print(product)
        

        # if product is None:
        #     return {"message":"Product is not available"},404

        # price = product[3]
        # remaining_quantity=int(product[4]) - int(quantity)
        # total_sale = int(product[3]) * int(quantity)
        # name = product[1]
        # date_created = datetime.now()


        # if remaining_quantity < 0:
        #     return {"message": "Not enough in stock"}

        # newsale = Sale(product_id,quantity,remaining_quantity,price,name,attendant,date_created).create_sale()
        # print(newsale)
        # Sale.decrease_quantity(product_id,remaining_quantity)
        

        # return make_response(jsonify(
        #     {"message":"Sale record created successfully"}
        #     ), 201)
        # "status":"created",
        #     "product":newsale 
    


class DeleteSale(Resource):
    def delete(self,sale_id):
        Sale.delete_product(sale_id)
        return {"message":"Deleted successfully"}
    


class Get_sale_id(Resource):
    def get(self,sale_id):
        
        sal = [sale for sale in sales if sale['sale_id'] == sale_id] or None
        if sal:
            return make_response(jsonify({'sale':sal[0]}),200)
        else:
            return jsonify({'message': "specific sale not found"})
            return 404