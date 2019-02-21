import psycopg2
import os
url =  os.getenv('DATABASE_URL')
def connect():
    """ Connect to the PostgreSQL database server """
    try:
    	conn = None
    	#parsing the required database connection inputs
    	conn = psycopg2.connect(url)
    	conn.autocommit = True
    	# print("connect")
    except Exception as e:
    	print(e)
    return conn

