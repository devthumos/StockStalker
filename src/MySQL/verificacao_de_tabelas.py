import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="action_stalker"
    )

cursor = connection.cursor()
cursor.execute("SHOW TABLES")

for i in cursor:
    print(i)