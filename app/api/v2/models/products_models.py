from app.dbconn import Database_Connection
from flask import request, jsonify, make_response
# from app.api.v2.views.products_views import Products_update

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
        self.con=Database_Connection()
        self.cur=self.con.cursor()

    def create_product(self):
        try:
            product={"product_name":self.product_name,"category":self.category,"price":self.price,"quantity":self.quantity}
            return {"message": "Product successfully Added"},201
            return product
        except Exception as e:
            print(e)
            return {"message": "Could not create a product"}
    def get_product(self):
        # query="SELECT * FROM products"
        # con=Database_Connection()
        # cur= con.cursor()
        self.cur.execute(query)
        db_products= self.cur.fetchall()
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
        # con=Database_Connection()
        # cur= con.cursor()
        query = "DELETE FROM products where product_id = %s;"
        self.cur.execute(query, (str(product_id),))
        con.commit()
        return query

    def update(self, product_id):
        query="UPDATE products SET product_name=%s,category=%s,price=%s,quantity=%s where product_id = %s" 
        # con=Database_Connection()
        # con.cursor()
        # cur= con.cursor()
        update =self.cur.execute(query, (self.product_name, self.category, self.price, self.quantity, product_id))
        con.commit()
        return {"message":"Product Successfully updated","Product":update},
    def get_product_by_id(product_id):
        # con=Database_Connection()
        # cur= con.cursor()
        self.cur.execute("SELECT * FROM products WHERE product_id =%s", (product_id,))
        print("iddddddddddd",product_id)
        product =self.cur.fetchone()
        return product
       

        # if product:
        #     prods = []
        #     for items in product:
        #         item ={
        #         'product_id':items[0],
        #         'product_name':items[1],
        #         'category':items[2],
        #         'price':items[3],
        #         'quantity':items[4]
        #         }
        #         prods.append(item)

            
    def get_product_name(product_name):
        # con=Database_Connection()
        # cur= con.cursor()
        self.cur.execute("SELECT * FROM products WHERE product_name = %s", (product_name,))
        productname = cur.fetchone()
        return productname
       
    # def get_total_products(quantity):
    #     # con=Database_Connection()
    #     # cur= con.cursor()
    #     self.cur.execute("SELECT quantity FROM products")
    #     quantity = self.cur.fetchall()
    #     prods = []
    #     if quantity:
    #         for items in quantity:
    #             item ={
    #             items[0]
    #             }
    #             prods.append(item)
    #     # print(type(prods))

    #     return prods