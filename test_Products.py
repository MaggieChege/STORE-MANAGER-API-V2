import unittest
import requests
import pytest
from app import create_app
from instance.config import app_configuration
from flask import json
from app.dbconn import *

class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app=create_app("testing")
        self.client=self.app.test_client()
        Database_Connection()
        drop_tables()
        create_tables()
        self.login_user = {"email": "ken@gmail.com", "password":"12345"}

#         self.register_user={ "username":"ken","email": "ken@gmail.com", "password":"12345","role":"Admin"}
#         self.register_user_empty_email = { "email": "", "password":"1234567890"}
        
#         self.login_user_empty_email= { "email": "", "password":"1234567890" }
#         self.login_user_empty_password= { "email": "higi@gmail.com", "password":""}




#         self.test_product=dict( 
#             product_id = "2",
#             product_name = "New Nikes",
#             price = 2000,
#             category = "Men",
#             quantity = 10)
#     def test_create_product(self):
#         response = self.client.post(
#         '/api/v2/users/login',
#         data = json.dumps(self.login_user),
#         content_type = 'application/json'
#         )
#         token = json.loads(response.data.decode())['access_token']

#         # #test product has been added
#         response = self.client.post(
#         '/api/v2/products',
#         data = json.dumps(self.test_product),
#         headers=dict(Authorization="Bearer " + token),
#         content_type = 'application/json'
#         )

#         response_data = json.loads(response.data)
#         # self.assertEqual("Product Successful Added",response_data["message"])
#         self.assertEqual(response.status_code, 200)

    def test_empty_product(self):
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.login_user),
        content_type = 'application/json'
        )
        token = json.loads(response.data.decode())['access_token']
        # response_data = json.loads(response.data)
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps({}),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        print(response_data)
        # self.assertEqual(response_data["message"],"Products data cannot be empty")
        self.assertEqual(response.status_code, 400)

