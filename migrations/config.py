import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    try:
    	conn = None
    	#parsing the required database connection inputs
    	conn = psycopg2.connect(host='localhost', database='politico', user='root', password='root')
    	conn.autocommit = True
    except Exception as e:
    	print(e)
    return conn

