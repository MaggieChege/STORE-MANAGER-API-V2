import psycopg2
# from instance.config import app_configuration
from app.queries import queries
def Database_Connection():
	try:
		url = "dbname='store' host='localhost' port='5432' user='postgres' password='root'"
		con = psycopg2.connect(url)
		cur =con.cursor()
		return con

	except(Exception, psycopg2.DatabaseError) as error:
		print("Failed to connect", error)
     

def create_tables():
	try:
		con=Database_Connection()
		cur= con.cursor()
		for tables in queries:
			cur.execute(tables)
		print("Tables Created")
	except (Exception,psycopg2.DatabaseError) as error:
		print("Failed to connect", error)

	finally:
		cur.close()
		con.commit()

def drop_tables():
	try:
		con=Database_Connection()
		cur= con.cursor()
		for drop in drop_queries:
			cur.execute(drop)
		con.commit()
		print("Tables Deleted")
	except Exception as e:
		print(e)





	# def save_details(tables):
# 	con = Database_Connection()
# 	cur= con.cursor()
# 	cur.execute(tables)
# 	cur.close()
# 	con.commit()
    
