import psycopg2
import os
from sys import modules
from instance.config import app_config
from app.queries import queries,drop_queries


environment = os.environ['ENVIRONMENT']

url = os.getenv('DATABASE_URL')

def Database_Connection():
	try:
		# if 'pytest' in modules:
		# 	connection = psycopg2.connect(
  #                   host="localhost", user="postgres", dbname="store_test", password="root")
		# 	return connection
		# else:
		con = psycopg2.connect(app_config[environment].DATABASE_URL)
		cur =con.cursor()
		return con
		# return conn

	except(Exception, psycopg2.DatabaseError) as error:
		print("Failed to connect", error)


def create_tables():
	try:
		con=Database_Connection()
		cur= con.cursor()
		for tables in queries:
			cur.execute(tables)
		cur.close()
		con.commit()
		print("Tables Created")
	except(Exception,psycopg2.DatabaseError) as error:
		print("Failed to connect", error)

	

def drop_tables():
	try:
		con=Database_Connection()
		cur= con.cursor()
		for drop in drop_queries:
			cur.execute(drop)

		print("Tables Deleted")
	except Exception as e:
		print(e)
		con.commit()
		cur.close()
		con.close