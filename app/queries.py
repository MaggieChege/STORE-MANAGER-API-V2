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
		id serial PRIMARY KEY,
		product_id INT NOT NULL,
        quantity INT NOT NULL,
        remaining_quantity INT NOT NULL,
        price INT NOT NULL,
        attendant varchar(50),
        total_sale INT,
        date_created TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products(product_id)
        );'''
blacklist = '''CREATE TABLE IF NOT EXISTS blacklists(
			id  SERIAL PRIMARY KEY,
             access_token VARCHAR(500) NOT NULL,
             date_created  DATE
				)'''
create_admin =''' INSERT INTO users(username,email,password,role) VALUES('admin','higi@gmail.com','pbkdf2:sha256:50000$eKWEMRmn$02f208bd4c19b95fee6ec7627190f613934d645ee890d1f185b6db5bf0dd8b80','Admin')
'''
drop_users="DROP TABLE IF EXISTS users CASCADE"
drop_products="DROP TABLE IF EXISTS products CASCADE"
drop_sales = "DROP TABLE IF EXISTS sales CASCADE"



queries = [users,products,sales,create_admin,blacklist]
drop_queries=[drop_users,drop_products,drop_sales]
