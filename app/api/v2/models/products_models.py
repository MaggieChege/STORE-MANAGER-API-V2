from app.dbconn import Database_Connection
from flask import request, jsonify, make_response

import psycopg2

products =[]
class Product():
    """docstring for ClassName"""
    def __init__(self,product_name,category, price, quantity):
        # self.product_id=product_id
        self.product_name=product_name
        self.category=category
        self.price=price
        self.quantity=quantity

    def create_product(self):
        try:
            product={"product_name":self.product_name,"category":self.category,"price":self.price,"quantity":self.quantity}
            return {"message": "Product Successful Added"}
            return product
        except Exception as e:
            print(e)
            return {"message": "Could not create a product"}
    def get_product(self):
        query="SELECT * FROM products"
        con=Database_Connection()
        cur= con.cursor()
        cur.execute(query)
        db_products= cur.fetchall()
        if db_products:
            prods = []
            for items in db_products:
                item ={
                'product_id':items[0],
                'product_name':items[1],
                'category':items[2],
                'price':items[3],
                'quantity':items[4]
                }
                prods.append(item)
            return prods

    def delete_product(product_id):
        con=Database_Connection()
        cur= con.cursor()
        query = "DELETE FROM products where product_id = %s;"
        update =cur.execute(query, (str(product_id)))
        con.commit()
        return query
    def get_by_id(product_id):
        if product_id:
            query = "SELECT * FROM products where product_id = '%s';" % product_id
            con=Database_Connection()
            con.cursor()
            cur.execute(query)
            return cur.fetchone()
        else:
            return {"message":"No product found"}

    def update(self, product_id):

        query="UPDATE products SET product_name=%s,category=%s,price=%s,quantity=%s where product_id = %s" 
        con=Database_Connection()
        con.cursor()
        cur= con.cursor()
        update =cur.execute(query, (self.product_name, self.category, self.price, self.quantity, product_id))
        con.commit()
        return {"message":"successfully updated"},
