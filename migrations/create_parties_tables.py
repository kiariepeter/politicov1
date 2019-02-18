from config import connect
conn = connect()
cur = conn.cursor()


table_parties = """CREATE TABLE IF NOT EXISTS tbl_parties(
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(250) NOT NULL,
        hqAddress VARCHAR(250) NOT NULL,
        logoUrl VARCHAR(250) NULL,
        slogan VARCHAR(250) NOT NULL,
        UNIQUE(name)
    )"""


if __name__=="__main__":
    cur.execute(table_parties)