# -*- coding: utf-8 -*-
import sqlite3
import sys
import codecs
import cgi


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>eCarnet - Employés d'un service</title>
</head>
<body>
""")

form = cgi.FieldStorage()
service_id = str(form["service"].value)
db_connection = sqlite3.connect("database.sqlite3")
db_connection.row_factory = sqlite3.Row
cursor = db_connection.cursor()
cursor.execute("SELECT name FROM Service WHERE id=" + service_id)
row = cursor.fetchone()
service_name = str(row["name"])

print("    <h1>Employés du service " + service_name + "</h1>")

cursor.execute("SELECT first_name, name, cellphone_number FROM Employee WHERE id_service=" + service_id)
rows = cursor.fetchall()

print("        <ol>") 
for row in rows:
    print("    <li>" + row["first_name"] + ", " + row["name"] + ", " + row["cellphone_number"] + "</li>")
print("""</ol>
</body>
</html>""")
db_connection.close()
