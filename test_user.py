import unittest
import requests
import pytest
from app import create_app
from flask import json


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app=create_app("testing")
        self.client=self.app.test_client()
        self.register_user={ "username":"ken","email": "ken@gmail.com", "password":"12345","role":"Admin"}
        self.register_user_empty_email = { "email": "", "password":"1234567890"}
        self.login_user = { "email": "higi@gmail.com", "password":"1234567890" }
        self.login_user_empty_email= { "email": "", "password":"1234567890" }
        self.login_user_empty_password= { "email": "higi@gmail.com", "password":""}

    def test_Registration(self):
        
        response = self.client.post(
        '/api/v2/users/login',
         data = json.dumps(dict(
            email='ken@gmail.com',password='12345')),
         content_type = 'application/json'
         )
        token = json.loads(response.data.decode())['access_token']

        response = self.client.post(
        '/api/v2/auth/user',
        data = json.dumps(self.register_user),
        headers=dict(Authorization="Bearer " + token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"User was created succesfully")
        self.assertEqual(response.status_code, 201)
        # self.as



    def test_login(self):
        response = self.client.post(
        '/api/v2/users/login',
         data = json.dumps(dict(
            email='ken@gmail.com',password='12345')),
         content_type = 'application/json'
         )
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"User was logged in succesfully")
        self.assertEqual(response.status_code, 200)

    def no_user_data(self):
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

    def user_exists(self):
        token = json.loads(response.data.decode())['access_token']
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user1),
        headers=dict(Authorization="Bearer " + self.token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"User account succesfuly created")
        self.assertEqual(response.status_code, 201)

