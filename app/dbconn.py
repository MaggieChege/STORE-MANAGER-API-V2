import psycopg2
import os
from sys import modules
from instance.config import app_config
from app.queries import queries,drop_queries


environment = os.environ['ENVIRONMENT']

url = os.getenv('DATABASE_URL')

def Database_Connection(url):
	try:
		DATABASE_URL = os.environ['DATABASE_URL']
		con = psycopg2.connect(DATABASE_URL, sslmode='require')
		return con
		# return conn

	except(Exception, psycopg2.DatabaseError) as error:
		print("Failed to connect!!!", error)

def init_db():
	con = Database_Connection(url)
	return con
def create_tables():
	try:
		con=Database_Connection(url)
		cur= con.cursor()
		for tables in queries:
			cur.execute(tables)
		# cur.close()
		con.commit()
		print("Tables Created")
	except(Exception,psycopg2.DatabaseError) as error:
		print("Failed to connect", error)

	

def drop_tables():
	try:
		con=Database_Connection(url)
		cur= con.cursor()
		for drop in drop_queries:
			cur.execute(drop)

		print("Tables Deleted")
	except Exception as e:
		print(e)
		con.commit()
		cur.close()
		con.close