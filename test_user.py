import unittest
import requests
import pytest
from app import create_app
from flask import json
from app.dbconn import drop_tables,create_tables


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app=create_app("testing")
        self.client=self.app.test_client()
        self.context = self.app.app_context()
        with self.context:
            create_tables()=
        self.logged_in_admin={"email":'higi@gmail.com',"password":'12345'}
        self.register_user_without_email ={ "username":"joan", "password":"123450","role":"User"}
        self.register_user = { "username":"joan","email": "joan@gmail.com", "password":"123450","role":"User"}
        self.register_invalid_email = { "username":"joan","email": "joan23233il.com", "password":"123450","role":"User"}
        self.login_user = {  "email":'higi@gmail.com',"password":'12345' }
        self.login_user_empty_email= { "email": "", "password":"12345" }
        self.login_user_empty_password= { "email": "higi@gmail.com", "password":""}
        self.login_empty_email_password={"email":"","password":""}
        self.login_normal_user={"email":"ken@gmail.com","password":"12345"}


    


    def test_login(self):
        # REGISTER ADMIN
        
        response = self.client.post('/api/v2/users/login',
         data = json.dumps(dict(self.login_user)),
         content_type = 'application/json')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"User was logged in succesfully")
        self.assertEqual(response.status_code, 200)
    
    def test_empty_password(self):
        response = self.client.post('/api/v2/users/login',
         data = json.dumps(dict(self.login_user_empty_password)),
         content_type = 'application/json')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"password cannot be empty")
        self.assertEqual(response.status_code, 400)
    def test_empty_email(self):
        response = self.client.post('/api/v2/users/login',
            data = json.dumps(dict(self.login_user_empty_email)),
            content_type = 'application/json')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"email can not be empty")
        self.assertEqual(response.status_code, 400)
    def test_login_empty_email_password(self):
        response = self.client.post('/api/v2/users/login',
            data = json.dumps(dict(self.login_empty_email_password)),
            content_type = 'application/json')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"email can not be empty")
        self.assertEqual(response.status_code, 400)

    def register_user_empty_email(self):
        token = json.loads(response.data.decode())['access_token']
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps({}),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"Fields cannot be empty")
        self.assertEqual(response.status_code, 200)
    def test_Register_Valid_email(self):

        response = self.client.post(
        '/api/v2/users/login',
         data = json.dumps(dict(
            email='higi@gmail.com',password='12345')),
         content_type = 'application/json')
        response_data = json.loads(response.data.decode())

        token = json.loads(response.data.decode())['access_token']

        response = self.client.post(
        '/api/v2/auth/user',
        data = json.dumps(self.register_user),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"Email exists")
        self.assertEqual(response.status_code, 200)
    def test_Register_user(self):
        response = self.client.post(
        '/api/v2/users/login',
         data = json.dumps(dict(
            self.logged_in_admin)),
         content_type = 'application/json')
        response_data = json.loads(response.data.decode())

        token = json.loads(response.data.decode())['access_token']

        response = self.client.post('/api/v2/auth/user',
        data = json.dumps(self.register_invalid_email),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"Enter correct email format")
        self.assertEqual(response.status_code, 200)

    def test_Register_user_no_email(self):
        response = self.client.post(
        '/api/v2/users/login',
         data = json.dumps(dict(
            email='higi@gmail.com',password='12345')),
         content_type = 'application/json')
        response_data = json.loads(response.data.decode())

        token = json.loads(response.data.decode())['access_token']

        response = self.client.post('/api/v2/auth/user',
        data = json.dumps(self.register_user_without_email),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"'email' is a required property")
        self.assertEqual(response.status_code, 400)

    def test_Protected_Route(self):
        response = self.client.post(
        '/api/v2/users/login',
         data = json.dumps(dict(
            self.login_normal_user)),
         content_type = 'application/json')
        response_data = json.loads(response.data.decode())

        token = json.loads(response.data.decode())['access_token']

        response = self.client.post('/api/v2/auth/user',
        data = json.dumps(self.register_user),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],'You must be logged in as Admin to add a product')
        self.assertEqual(response.status_code, 403)


