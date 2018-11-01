# import unittest
# import os
# import json
# from app import create_app
# from instance.config import app_config
# from connection import Database_Connection
# db = Database_Connection()

# class TestBase(unittest.TestCase):
#     db.dropTables()
#     def setUp(self):
#         self.app=create_app("testing")
#         self.client=self.app.test_client()
#         self.register_user={ "username":"ken","email": "ken@gmail.com", "password":"12345","role":"Admin"}
#         self.register_user_empty_email = { "email": "", "password":"1234567890"}
#         self.login_user = {"email": "ken@gmail.com", "password":"12345"}
#         self.login_user_empty_email= { "email": "", "password":"1234567890" }
#         self.login_user_empty_password= { "email": "higi@gmail.com", "password":""}



#         self.test_product=dict( 
#             product_id = "2",
#             product_name = "New Nikes",
#             price = 2000,
#             category = "Men",
#             quantity = 10)