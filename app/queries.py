users = '''CREATE TABLE IF NOT EXISTS users(
		id serial PRIMARY KEY,
		username varchar(10) NOT NULL,
		email varchar(50) NOT NULL,
		password varchar(10) NOT NULL);'''


products = '''CREATE TABLE IF NOT EXISTS products(
		product_id serial PRIMARY KEY,
		product_name varchar(50) NOT NULL,
		price varchar(10) NOT NULL,
		quantity varchar(10) NOT NULL);'''

sales = '''CREATE TABLE IF NOT EXISTS sales(
		sale_id serial PRIMARY KEY,
		product_id varchar(10) 	NOT NULL,
		product_name varchar(10) NOT NULL,
		price varchar(10) NOT NULL,
		total_sale varchar(10) NOT NULL,
		attendant varchar(10) NOT NULL,
		quntity varchar(10) NOT NULL);'''




queries = [users,products,sales]