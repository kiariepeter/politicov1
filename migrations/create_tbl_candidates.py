from config import connect
conn = connect()
cur = conn.cursor()


tbl_candidates = """CREATE TABLE IF NOT EXISTS tbl_candidates(
        id SERIAL  PRIMARY KEY  NOT NULL,
        party INTEGER NOT NULL DEFAULT 0,
        office INTEGER NOT NULL DEFAULT 0,
        candidate INTEGER NOT NULL DEFAULT 0,
        UNIQUE(candidate),
        FOREIGN KEY (party) REFERENCES tbl_parties(id) ON DELETE CASCADE,
        FOREIGN KEY (office) REFERENCES tbl_offices(id) ON DELETE CASCADE,
        FOREIGN KEY (candidate) REFERENCES tbl_users(id) ON DELETE CASCADE
    )"""


if __name__=="__main__":
    cur.execute(tbl_candidates)