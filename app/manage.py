def reset_migrations():
    '''clear tables after tests'''
    from app import db
    con = db.con
    cur = db.cursor


    cur.execute("""DROP TABLE IF EXISTS users CASCADE:""")
    cur.execute("""DROP TABLE IF EXISTS sales CASCADE:""")
    cur.execute("""DROP TABLE IF EXISTS products CASCADE:""")

    con.commit()


def migrate():
	from app import db
	con = db.con
	cur = db.cursor
	cur.execute('''CREATE TABLE IF NOT EXISTS users(
		id serial PRIMARY KEY,
		username varchar(50) NOT NULL,
		email varchar(50) NOT NULL,
		password varchar(100) NOT NULL,
		role varchar(50));''')

	cur.execute( '''CREATE TABLE IF NOT EXISTS products(
		product_id serial PRIMARY KEY,
		product_name varchar(50) NOT NULL,
		category varchar(50) NOT NULL,
		price varchar(50) NOT NULL,
		quantity varchar(50) NOT NULL);''')

	cur.execute('''CREATE TABLE IF NOT EXISTS sales(
		id serial PRIMARY KEY,
		product_id INT NOT NULL,
        quantity INT NOT NULL,
        remaining_quantity INT NOT NULL,
        price INT NOT NULL,
        product_name varchar(50),
        attendant varchar(50),
        date_created TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products(product_id)
        );''')
	cur.execute(''' INSERT INTO users(username,email,password,role) VALUES('admin','higi@gmail.com','pbkdf2:sha256:50000$eKWEMRmn$02f208bd4c19b95fee6ec7627190f613934d645ee890d1f185b6db5bf0dd8b80','Admin')''')




	print("DATABASE CREATED")
	con.commit()