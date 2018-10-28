from app.dbconn import Database_Connection

products = []


class Product():
    """docstring for ClassName"""
    def __init__(self,product_id,product_name,category, price, quantity):
        self.product_id=product_id
        self.product_name=product_name
        self.category=category
        self.price=price
        self.quantity=quantity
    def get_product(self):
        return products

    def create_product(self):
        product_id=len(products)+1
        product={"product_id":self.product_id,"product_name":self.product_name,"category":self.category,"price":self.price,"quantity":self.quantity}
        # product_id,product_name,category,price,quantity)
        return product
    
