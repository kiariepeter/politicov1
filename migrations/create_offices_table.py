from config import connect
conn = connect()
cur = conn.cursor()


table_offices = """CREATE TABLE IF NOT EXISTS table_offices(
        id SERIAL PRIMARY KEY NOT NULL,
        office_name VARCHAR(250) NOT NULL,
        logo VARCHAR(250) NOT NULL,
        status INTEGER NOT NULL DEFAULT 1,
        UNIQUE(office_name)
    )"""


if __name__=="__main__":
    cur.execute(table_offices)