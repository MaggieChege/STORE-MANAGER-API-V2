import psycopg2
import os
from instance.config import app_configuration
from app.queries import queries


enviroment = os.environ['ENV']

url = os.getenv('DATABASE_URL')

def Database_Connection():
	try:

		con = psycopg2.connect("dbname='store' host='localhost' port='5432' user='postgres' password='root'")
		cur =con.cursor()
		# conn = psycopg2.connect(app_configuration[enviroment].connectionVariables)
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
		print("Tables Created")
	except (Exception,psycopg2.DatabaseError) as error:
		print("Failed to connect", error)

	finally:
		cur.close()
		con.commit()

# def create_admin():
	

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