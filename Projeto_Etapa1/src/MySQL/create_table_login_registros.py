import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",

    )
cursor = connection.cursor()
cursor.execute("CREATE DATABASE ACTION_STALKER_USERS")
cursor.execute("CREATE DATABASE ACTION_STALKER_CODES")

connection_users = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="ACTION_STALKER_USERS"
    )

connection_codes = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="ACTION_STALKER_CODES"
    )

cursor_users = connection_users.cursor()
# cursor_codes = connection_codes.cursor()

cursor_users.execute("CREATE TABLE login(user VARCHAR(255), password VARCHAR(255), id int NOT NULL AUTO_INCREMENT, PRIMARY KEY (id))")

# cursor_codes.execute(f"CREATE TABLE registros(codigo VARCHAR(255), tipo VARCHAR(255), PRIMARY KEY(codigo))")
# for i in range(1, 5):
#     cursor.execute(f"ALTER TABLE registros ADD indicador_0{i} VARCHAR(255)")
# for i in range(1, 5):
#     cursor.execute(f"ALTER TABLE registros ADD label_0{i} VARCHAR(255)")
