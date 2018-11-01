from flask import request, jsonify, make_response
from flask_restful import Resource
from app.dbconn import Database_Connection
from app.api.v2.models.users_model import Users
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import re
from functools import wraps
from app.api.v2.utils.schemas import user_schema
from flask_expects_json import expects_json



def admin_only(f): 
    @wraps(f)
    def decorator_func(*args,**kwargs):
        user = Users.fetch_by_role(get_jwt_identity())
        print(user)

        if not user ==  "Admin":
            return{"message":"You must be logged in as Admin to add a product"},403
        else:
            return f(*args,**kwargs)

    return decorator_func

       
class UserRegistration(Resource):
    # @jwt_required
    # @admin_only
    @expects_json(user_schema)
    def post(self):

        data = request.get_json()
        username=data['username']
        email = data['email']
        role = data['role']
        raw_password = data['password']
        if not email or email =="":
            return {message:"Enter an email"}
        if not username or username =="":
            return {message:"Enter an email"}
            
        if not role or role =="":
            return {message:"Enter an email"}


            return make_response(jsonify({"message":"email cannot be empty"}))
        if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
            return {"message": "Enter correct email format"}
                    # generate hash value for rawpassword

        users =Users.get_users(self)
        if users:
            user_email = [user for user in users if user["email"] == email]
            if user_email:
                return {"message": "Email exists"}

        password = Users.generate_hash(raw_password)
       
        user = Users(username,email,password,role).create_user()
        
        response =jsonify({

            'message': 'User was created succesfully',
            'status': 'ok',
            
            })
        response.status_code = 201
        return response



class UserLogin(Resource):

    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        if not email or email =="":
            return {'message': 'email can not be empty'},400
        if not password or email == "":
            return {'message': 'password cannot be empty'},400
        query = "SELECT password FROM users WHERE email= '{}'".format(data['email'])
        con=Database_Connection()
        cur= con.cursor()
        cur.execute(query)
        dbusers= cur.fetchall()
        if len(dbusers) == 0:
            return {"message": "User does not exist"},404
        else:
            if Users.verify_hash(dbusers[0][0],password) == True:
                access_token = create_access_token(identity = email)
                refresh_token = create_refresh_token(identity = email)
                return {
                'message': 'User was logged in succesfully',
                'status': 'ok',
                'access_token': access_token,
                'refresh_token': refresh_token
                }, 200
            else:
                return {'message': 'Wrong credentials'},400
        # return dbusers
        