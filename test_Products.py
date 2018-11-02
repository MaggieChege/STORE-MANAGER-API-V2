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
        self.login_user = {"email": "higi@gmail.com", "password":"12345"}
        self.test_product= {
            "category": "Men",
            "price": "5500",
            "product_id": 3,
            "product_name": "Nikes Old School ",
            "quantity": "2"
        }
        self.test_empty_product_name={"product_name":"",
                        "category":"Men oneqwrewrly",
                        "quantity":2,
                        "price":5000}
        self.all_products = {
            "category": "Men oneqwrewrly wewqeqw",
            "price": "5000",
            "product_id": 1,
            "product_name": "Nikes Old School shoes 2020 ",
            "quantity": "2"}

    def test_create_product(self):
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.login_user),
        content_type = 'application/json'
        )
        token = json.loads(response.data.decode())['access_token']

        # #test product has been added
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json')
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"Product Successful Added")
        self.assertEqual(response.status_code, 201)

    def test_empty_product(self):
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.login_user),
        content_type = 'application/json'
        )
        token = json.loads(response.data.decode())['access_token']
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_empty_product_name),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        print(response_data)
        self.assertEqual(response_data["message"],"Product Name is required")
        self.assertEqual(response.status_code, 200)


    

    
    def test_get_product(self):

        """This method tests wheather all products are  retrieved.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post('/api/v2/users/login',
         data = json.dumps(dict(self.login_user)),
         content_type = 'application/json')
        token = json.loads(response.data.decode())['access_token']
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.login_user),
        content_type = 'application/json'
        )
        
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.all_products),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json'
        )


    def test_delete_product(self):
        """This method tests the method for deleting a product.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.login_user),
        content_type = 'application/json'
        )
        token = json.loads(response.data.decode())['access_token']

        response = self.client.delete(
        '/api/v2/products/2',
        headers=dict(Authorization="Bearer " + token)
        )
        self.assertEqual(response.status_code, 200)


        response = self.client.get(
        '/api/v2/products/2',
        headers=dict(Authorization="Bearer " + token))
        response_data = json.loads(response.data)
        self.assertEqual('Product Does not exist',response_data["message"])