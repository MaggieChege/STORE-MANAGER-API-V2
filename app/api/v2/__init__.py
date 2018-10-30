from flask import Flask,Blueprint
from flask_restful import Api,Resource
from app.api.v2.views.products_views import Products,Get_product_id
# Register your resources here

blue = Blueprint("api", __name__, url_prefix="/api/v2")
api=Api(blue)

api.add_resource(Products,"/products")
api.add_resource(Get_product_id,"/products/<int:product_id>")