import os 
import psycopg2 
DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)
conn.autocommit = True
cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)



def start_db() -> object:
	querys = [table_users,table_offices,table_parties,tbl_candidates,table_votes]
	for query in querys:
		cur.execute(query)





table_users = """CREATE TABLE IF NOT EXISTS tbl_users(
        id SERIAL PRIMARY KEY NOT NULL,
        firstname VARCHAR(250) NOT NULL,
        lastname VARCHAR(250) NOT NULL,
        othername VARCHAR(250) NULL,
        email VARCHAR(250) NOT NULL,
        phoneNumber VARCHAR(250) NULL,
        password VARCHAR(250) NOT NULL,
        passportUrl VARCHAR(250) NULL,
        admin BOOLEAN NOT NULL DEFAULT FALSE,
        UNIQUE(email)
    )"""


table_offices = """CREATE TABLE IF NOT EXISTS tbl_offices(
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(250) NOT NULL,
        type VARCHAR(250) NOT NULL,
        UNIQUE(name)
    )"""

table_parties = """CREATE TABLE IF NOT EXISTS tbl_parties(
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(250) NOT NULL,
        hqAddress VARCHAR(250) NOT NULL,
        logoUrl VARCHAR(250) NULL,
        slogan VARCHAR(250) NOT NULL,
        UNIQUE(name)
    )"""

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

table_votes = """CREATE TABLE IF NOT EXISTS tbl_votes(
        id SERIAL NOT NULL,
        createdby INTEGER NOT NULL DEFAULT 0,
        office INTEGER NOT NULL DEFAULT 0,
        candidate INTEGER NOT NULL DEFAULT 0,
        createdOn  TIMESTAMP WITHOUT TIME ZONE \
        DEFAULT (NOW() AT TIME ZONE 'utc'),
        PRIMARY KEY (createdby, office),
        FOREIGN KEY (createdby) REFERENCES tbl_users(id) ON DELETE CASCADE,
        FOREIGN KEY (office) REFERENCES tbl_offices(id) ON DELETE CASCADE,
        FOREIGN KEY (candidate) REFERENCES tbl_candidates(id) ON DELETE CASCADE
    )"""


start_db()



