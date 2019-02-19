# from config import connect
# conn = connect()
# cur = conn.cursor()


# table_users = """CREATE TABLE IF NOT EXISTS tbl_users(
#         id SERIAL PRIMARY KEY NOT NULL,
#         firstname VARCHAR(250) NOT NULL,
#         lastname VARCHAR(250) NOT NULL,
#         othername VARCHAR(250) NULL,
#         email VARCHAR(250) NOT NULL,
#         phoneNumber VARCHAR(250) NULL,
#         password VARCHAR(250) NOT NULL,
#         passportUrl VARCHAR(250) NULL,
#         admin BOOLEAN NOT NULL DEFAULT FALSE,
#         UNIQUE(email)
#     )"""


# if __name__=="__main__":
#     cur.execute(table_users)