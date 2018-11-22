
import unittest
import requests
import pytest
from app import create_app
from instance.config import app_config
from flask import json
from app.dbconn import *
class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app=create_app("testing")
        self.client=self.app.test_client()
        Database_Connection()
        drop_tables()
        create_tables()
        self.login_user = {"email": "higi@gmail.com", "password":"12345"}
        self.login_user1 = {"email": "ken@gmail.com", "password":"12345"}
        self.test_sale= {              
                    "product_id":10,
                    "quantity":1,
                "attendant":"Trump"
                
                }
       
        self.test_empty_quantity={"product_id":3,
                        "quantity": 0,
                "attendant":"Trump"
                }
        self.test_empty_attendant={"product_id":3,
                        "quantity":2,
                "attendant":""
                }
        self.test_product_doesnt_exist={"product_id":33,
                                "quantity":2,
                "attendant":"Trump"
                }
        self.test_sale_excess_products={"product_id":33,
                        "quantity":200,
                "attendant":"Trump"
                }

    def test_get_sales(self):

        response = self.client.get(
            'api/v2/sales', content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_empty_attendant(self):
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.login_user),
        content_type = 'application/json'
        )
        token = json.loads(response.data.decode())['access_token']

        # #test product has been added
        response = self.client.post(
        '/api/v2/sales',
        data = json.dumps(self.test_empty_attendant),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"], 'All fields are required')
        self.assertEqual(response.status_code, 400)
    def test_product_doesnt_exist(self):
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.login_user),
        content_type = 'application/json'
        )
        token = json.loads(response.data.decode())['access_token']

        # #test product has been added
        response = self.client.post(
        '/api/v2/sales',
        data = json.dumps(self.test_product_doesnt_exist),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"], 'No product found')
        self.assertEqual(response.status_code, 404)

 