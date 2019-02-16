from config import connect
conn = connect()
cur = conn.cursor()


tbl_candidates = """CREATE TABLE IF NOT EXISTS tbl_candidates(
        id SERIAL PRIMARY KEY NOT NULL,
        party_id INTEGER NOT NULL DEFAULT 0,
        office_id INTEGER NOT NULL DEFAULT 0,
        candidate_id INTEGER NOT NULL DEFAULT 0,
        status INTEGER NOT NULL DEFAULT 1,
        createdOn  TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        FOREIGN KEY (party_id) REFERENCES tbl_parties(id) ON DELETE CASCADE,
        FOREIGN KEY (office_id) REFERENCES tbl_offices(id) ON DELETE CASCADE,
        FOREIGN KEY (candidate_id) REFERENCES tbl_users(id) ON DELETE CASCADE
    )"""


if __name__=="__main__":
    cur.execute(tbl_candidates)