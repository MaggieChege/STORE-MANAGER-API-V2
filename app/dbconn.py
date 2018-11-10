import os
import psycopg2
from psycopg2.extras import RealDictCursor

class Database_Connection:
    con = None
    cursor = None
    app = None
    def init_app(self, app):
        '''create the database connection'''
        self.con = psycopg2.connect(
            dbname="d82kojevmkac9n",
            user="pnunuyfihqobek",
            host="ec2-54-204-14-96.compute-1.amazonaws.com",
            password="93c9437a1e270c0b5951d9421f7a27a0ba4d023e3e00a2df4e6451d30cb0e503"
            )
        self.cursor = self.con.cursor(cursor_factory=RealDictCursor)