import pymysql

"""
Aqui é criado todos os bancos de dados e tabelas inicias, com exceção das tabelas do banco action_stalker_codes
"""

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

cursor_users.execute("CREATE TABLE login(user VARCHAR(255), password VARCHAR(255), id int NOT NULL AUTO_INCREMENT, PRIMARY KEY (id))")
