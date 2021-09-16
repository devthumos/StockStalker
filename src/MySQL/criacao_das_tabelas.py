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
cursor.execute("CREATE TABLE registros(codigo VARCHAR(255), tipo VARCHAR(255), empresa VARCHAR(255))")
