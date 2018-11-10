from flask import make_response, jsonify
from passlib.hash import pbkdf2_sha256 as sha256
from app.dbconn import Database_Connection

# sales =[]
from app import db
con = db.con
cur = db.cursor
class Sale():

    def __init__(self, product_id, quantity, remaining_quantity, price, product_name,attendant, date_created):
        self.product_id = product_id
        self.quantity = quantity
        self.remaining_quantity = remaining_quantity
        self.price = price
        self.product_name = product_name
        self.attendant=attendant
        self.date_created = date_created
 
    def create_sale(self):
        sale={"product_id":self.product_id,"quantity":self.quantity,"remaining_quantity":self.remaining_quantity,"price":self.price,"product_name":self.product_name, "attendant":self.attendant,"date_created":self.date_created}
        try:
            # con=Database_Connection()
            # cur= con.cursor()
            data = cur.execute("INSERT INTO sales(product_id, quantity, remaining_quantity, price, product_name,attendant,date_created) VALUES('{}','{}','{}','{}','{}','{}','{}');".format(self.product_id,self.quantity,self.remaining_quantity,self.price,self.product_name, self.attendant,self.date_created))
            print(data)
            con.commit()
        except Exception as e:
            print(e)
        return sale
        
    def get_sales(self):
        query="SELECT * FROM sales"
        # con=Database_Connection()
        # cur= con.cursor()
        cur.execute(query)
        db_sales= cur.fetchall()
        if db_sales:
            sales = []
            for items in db_sales:
                item ={
                'sale_id':items[0],
                'products_id':items[1],
                'quantity':items[2],
                'remaining_quantity':items[3],
                'price':items[4],
                'product_name':items[5],
                'attendant':items[6],
                'date_created':items[7],
                }
                sales.append(item)
            return sales

    
    def decrease_quantity(product_id, remaining_quantity):
        # con=Database_Connection()
        # cur= con.cursor()
        cur.execute("UPDATE products SET quantity = %s WHERE product_id = %s", (remaining_quantity,product_id))
        con.commit()