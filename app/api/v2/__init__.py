from flask import Flask,Blueprint
from flask_restful import Api,Resource

# Register your resources here

blue = Blueprint("api", __name__, url_prefix="/api/v2")
api=Api(blue)

