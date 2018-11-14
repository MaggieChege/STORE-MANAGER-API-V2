from flask import request, jsonify, make_response
from flask_restful import Resource
from app.dbconn import Database_Connection
from app.api.v2.models.users_model import Users
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import (verify_jwt_in_request,get_jwt_claims,create_access_token, get_jwt_identity,jwt_required,get_raw_jwt)
import re
from functools import wraps
from app.api.v2.utils.schemas import user_schema
from flask_expects_json import expects_json
import datetime
from app.api.v2.views.blacklist import add_to_blacklist
from app import dbconn



def admin_required(f): 
    @wraps(f)
    def decorator_func(*args,**kwargs):
        token = None
        if 'access_token' in request.headers:
            token = request.headers['access_token']
            print(request.headers)
        elif token:
            return make_response(jsonify({
                "message": "Token is required"
                }),499)
        try:
            user = Users.fetch_by_email(get_jwt_identity())
            
            if not user ==  "Admin":
                return{"message":"You must be logged in as Admin "},403
            else:
                return f(*args,**kwargs)
        except Exception as e:
            print(e)
            # raise ExpiredSignatureError('Signature has expired')

    return decorator_func

# try:
#     pass
# except Exception as e:
#     raise
# else:
#     pass
# finally:
#     pass

class UserRegistration(Resource):
    @jwt_required
    @admin_required
    @expects_json(user_schema)
    def post(self):

        data = request.get_json()
        username=data['username']
        email = data['email']
        role = data['role']
        raw_password = data['password']

        if not username or not email or not role or not raw_password:
            return make_response(jsonify({
                "message": "All fields are required"
                }),400)
        if not email or email =="":
            return jsonify({"message":"Enter an email"})
        if not username or username =="":
            return jsonify({"message":"Enter an username"})
            
        if not role or role =="":
            return jsonify({"message":"Enter an email"})


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
        
        return make_response(jsonify({

            'message': 'User was created succesfully',
            'status': 'ok',
            
            }),201)
        



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
     
        # print(dbusers[0][0])
        if len(dbusers) == 0:
            return {"message": "User does not exist"},404
        else:
            user2 =(email,password)
            print(user2,"user2")
            if Users.verify_hash(dbusers[0][0],password) == True:
                exp=datetime.timedelta(minutes=30)
                # logged_user = user2.get_one_user()
                # names = logged_user["names"]
                # role = logged_user["role"]
                access_token = create_access_token(identity =email)


                # refresh_token = create_refresh_token(identity = email)
                return {
                'message': 'User was logged in succesfully',
                'status': 'ok',
                'access_token': access_token,
                # 'refresh_token': refresh_token
                }, 200
            else:
                return {'message': 'Wrong credentials'},400

class Logout(Resource):

    # @jwt_required
    @jwt_required
    def delete(self):
        # blacklist = set()
        jti = get_raw_jwt()['jti']
        add_to_blacklist(jti)
        return {"message":"Successfully Logged out"},200