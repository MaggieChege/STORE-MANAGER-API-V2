from app.dbconn import Database_Connection
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)
import psycopg2
# from app.api.v2.views.users_views import User

class Users():
    def __init__(self,username=None,email=None,password=None,role=None):
        self.username=username
        self.email=email
        self.password=password
        self.role=role

    def get_users(self):
        query="SELECT * FROM users"
        con=Database_Connection()
        cur= con.cursor()
        cur.execute(query)
        db_users= cur.fetchall()
       
        if db_users:
            users = []
            for items in db_users:
                item ={
                'id':items[0],
                'username':items[1],
                'email':items[2],
                'password':items[3],
                'role':items[4]
                }
                users.append(item)
            return users

    def create_user(self):
        user = {"username":self.username,"email":self.email,"password":self.password,"role":self.role}
        try:
            con =Database_Connection()
            cur=con.cursor()
            query = "INSERT INTO users(username,email,password,role) VALUES('{}','{}','{}','{}');".format(self.username,self.email,self.password,self.role)
            cur.execute(query)
            con.commit()
        except Exception as e:
            print (e)
        return user


    def generate_hash(raw_password):
        return generate_password_hash(raw_password)


    def verify_hash(hash_password,password):
        return check_password_hash(hash_password,password)

    def get_one_user(self):
        con =Database_Connection()
        cur=con.cursor()
        n = cur.execute("SELECT id,email,names,role FROM users where email =%s",(email,))
        return n

  

    @staticmethod
    def fetch_by_email(email):
        "Fetch a user through email"
        con =Database_Connection()
        cur=con.cursor()
        cur.execute("SELECT * FROM users WHERE email =%s", (email,))
        logged_in =cur.fetchone()
        if not logged_in:
            return jsonify("No user logged_in")
        return logged_in

       

    @staticmethod
    def get_by_id(user_id):
        "Fetch a user through email"
        if user_id:
            con =Database_Connection()
            cur=con.cursor()
            cur.execute("SELECT * FROM users WHERE id ='%s';" % user_id)
            return  cur.fetchone()
    
    def add_to_blacklist(self,access_token):
        try:
            con =Database_Connection()
            cur=con.cursor()
            cur.execute("INSERT INTO blacklists(access_token) VALUES(%s)",(access_token,))
            con.commit()

        except Exception as e:
            print (e)

    def check_blacklist(self,access_token):
        try:
            con =Database_Connection()
            cur=con.cursor()
            cur.execute("SELECT * FROM blacklists WHERE access_token  = %s",(access_token,))
            return cur.fetchone()

        except Exception as e:
            raise
        
