from config import connect
conn = connect()
cur = conn.cursor()


table_votes = """CREATE TABLE IF NOT EXISTS table_votes(
        id SERIAL PRIMARY KEY NOT NULL,
        createdby INTEGER NOT NULL,
        office_id INTEGER NOT NULL,
        party_id INTEGER NOT NULL,
        candidate_id INTEGER NOT NULL,
        status INTEGER NOT NULL DEFAULT 1,
        createdOn  TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        FOREIGN KEY (createdby) REFERENCES tbl_users(id) ON DELETE CASCADE,
    )"""


if __name__=="__main__":
    cur.execute(table_votes)