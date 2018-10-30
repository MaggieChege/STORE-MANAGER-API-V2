from flask import make_response, jsonify
from passlib.hash import pbkdf2_sha256 as sha256

# sales =[]

class Sale():
    def __init__(self,sale_id,product_id,product_name,price,attendant,total_sale,quantity):
        self.sale_id=(sale_id)
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.attendant=attendant
        self.total_sale=total_sale
        self.quantity=quantity
    @staticmethod
    def get_sales():
        return sales
    # @staticmethod
    def create_sale(self):
        sale_id= len(sales)+1
        sale ={"sale_id":self.sale_id,"product_id":self.product_id,"product_name" :self.product_name,"price" :self.price,"attendant" :self.attendant,"total_sale":self.total_sale,"quantity":self.quantity}
        # sales.append(sale)
        return sale
