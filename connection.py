import psycopg2

 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        conn = psycopg2.connect(host="localhost",database="ch2", user="root", password="root")
        conn.autocommit = True
    except (Exception, psycopg2.DatabaseError) as error:
        # print(error)
    return conn