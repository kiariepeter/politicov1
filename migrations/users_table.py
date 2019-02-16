table_users = """CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(250) NOT NULL,
        phone VARCHAR(250) NOT NULL,
        national_id VARCHAR(250) NULL,
        email VARCHAR(250) NOT NULL,
        phonenumber VARCHAR(250) NULL,
        password VARCHAR(250) NOT NULL,
        user_type BOOLEAN NOT NULL DEFAULT FALSE,
        status BOOLEAN NOT NULL DEFAULT TRUE,
        UNIQUE(email),
        UNIQUE(national_id)
    )"""