from config import connect
conn = connect()
cur = conn.cursor()


table_users = """CREATE TABLE IF NOT EXISTS tbl_users(
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(250) NOT NULL,
        phone VARCHAR(250) NOT NULL,
        photo VARCHAR(250) NOT NULL,
        national_id INTEGER NOT NULL,
        email VARCHAR(250) NOT NULL,
        password VARCHAR(250) NOT NULL,
        user_type INTEGER NOT NULL DEFAULT 1,
        status INTEGER NOT NULL DEFAULT 1,
        UNIQUE(email),
        UNIQUE(national_id)
    )"""


if __name__=="__main__":
    cur.execute(table_users)