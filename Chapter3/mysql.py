import pymysql
from random import randint

connection_params = {
    "user": "root",
    "password": "123456",
    "host": "localhost",
    "port": 3122,
}

cnx = pymysql.Connect(**connection_params)

cur = cnx.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS isp;")
cnx.select_db("isp")

cur.execute("select @@version")
output = cur.fetchall()
print(output)

cur.execute("CREATE TABLE IF NOT EXISTS person (person_id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20) NOT NULL, age INTEGER);")

names = ["John", "Brohn", "James", "Ren", "Felix"]

for name in names:
    age = randint(15, 32)
    cur.execute(f"INSERT INTO person (name, age) VALUES ('{name}', {age});")

cnx.commit()

cur.execute("SELECT * FROM person")
output = cur.fetchall()

for elem in output:
    print(elem)

cnx.close()