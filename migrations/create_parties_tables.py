from config import connect
conn = connect()
cur = conn.cursor()


table_parties = """CREATE TABLE IF NOT EXISTS table_parties(
        id SERIAL PRIMARY KEY NOT NULL,
        party_name VARCHAR(250) NOT NULL,
        logo VARCHAR(250) NOT NULL,
        photo VARCHAR(250) NOT NULL,
        members INTEGER NOT NULL,
        address VARCHAR(250) NOT NULL,
        status INTEGER NOT NULL DEFAULT 1,
        UNIQUE(party_name)
    )"""


if __name__=="__main__":
    cur.execute(table_parties)