# -*- coding: utf-8 -*-
import sqlite3
import sys
import codecs
import cgi

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>
            eCarnet - Ajout d'un employé
        </title>
    </head>
    <body>
""")
form = cgi.FieldStorage()
id_service = str(form["service"].value)
name = str(form["name"].value)
first_name = str(form["first_name"].value)
registration_number = str(form["registration_number"].value)
cellphone_number = str(form["cellphone_number"].value)

db_connection = sqlite3.connect("database.sqlite3")
db_connection.row_factory = sqlite3.Row
cursor = db_connection.cursor()
cursor.execute("INSERT INTO Employee(registration_number, first_name, "
               "name, cellphone_number, id_service) VALUES (?, ?, ?, ?, ?)",
               (registration_number, first_name, name, cellphone_number, id_service))

db_connection.commit()
db_connection.close()

print("<h1>Ajout de l\'emplyé * " + first_name + " " + name + " *</h1>")
print("<p>" + first_name + " " + name + " a bien été ajouté dans la base de données.</p>")
print("""<p><a href="eCarnet_home.py">Retour au eCarnet.</a></p>
    </body>
</html>""")
