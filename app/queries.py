users = '''CREATE TABLE IF NOT EXISTS users(
		id serial PRIMARY KEY,
		username varchar(50) NOT NULL,
		email varchar(50) NOT NULL,
		password varchar(100) NOT NULL,
		role varchar(50));'''


products = '''CREATE TABLE IF NOT EXISTS products(
		product_id serial PRIMARY KEY,
		product_name varchar(50) NOT NULL,
		category varchar(50) NOT NULL,
		price varchar(50) NOT NULL,
		quantity varchar(50) NOT NULL);'''

sales = '''CREATE TABLE IF NOT EXISTS sales(
		product_id INT NOT NULL,
        quantity INT NOT NULL,
        remaining_quantity INT NOT NULL,
        price INT NOT NULL,
        name varchar(50),
        attendant varchar(50),
        date_created TIMESTAMP,  
        FOREIGN KEY (product_id) REFERENCES products(product_id)
        );'''
drop_users="DROP TABLE IF EXISTS users "
drop_products="DROP TABLE IF EXISTS products "
drop_sales = "DROP TABLE IF EXISTS sales "



queries = [users,products,sales]
drop_queries=[drop_users,drop_products,drop_sales]