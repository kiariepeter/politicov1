# from config import connect
# conn = connect()
# cur = conn.cursor()


# table_votes = """CREATE TABLE IF NOT EXISTS tbl_votes(
#         id SERIAL NOT NULL,
#         createdby INTEGER NOT NULL DEFAULT 0,
#         office INTEGER NOT NULL DEFAULT 0,
#         candidate INTEGER NOT NULL DEFAULT 0,
#         createdOn  TIMESTAMP WITHOUT TIME ZONE \
#         DEFAULT (NOW() AT TIME ZONE 'utc'),
#         PRIMARY KEY (createdby, office),
#         FOREIGN KEY (createdby) REFERENCES tbl_users(id) ON DELETE CASCADE,
#         FOREIGN KEY (office) REFERENCES tbl_offices(id) ON DELETE CASCADE,
#         FOREIGN KEY (candidate) REFERENCES tbl_candidates(id) ON DELETE CASCADE
#     )"""


# if __name__=="__main__":
#     cur.execute(table_votes)