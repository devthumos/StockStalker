import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    init_command="CREATE DATABASE action_stalker"
    )

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="action_stalker"
    )

cursor = connection.cursor()
cursor.execute("CREATE TABLE login(user VARCHAR(255), password VARCHAR(255))")
cursor.execute(f"CREATE TABLE registros(codigo VARCHAR(255), tipo VARCHAR(255), PRIMARY KEY(codigo))")
for i in range(1, 5):
    cursor.execute(f"ALTER TABLE registros ADD indicador_0{i} VARCHAR(255)")
for i in range(1, 5):
    cursor.execute(f"ALTER TABLE registros ADD label_0{i} VARCHAR(255)")
