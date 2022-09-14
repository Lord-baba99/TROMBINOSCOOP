# -*- coding: utf-8 -*-
import sqlite3
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

"""("Content-Type: application/xhtml+xml; charset=utf-8")"""

# partie statique de la page HTML

print("""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>eCarnet - home</title>
</head>
<body>
    <h1>Bienvenue sur l'eCarnet de l'ULB</h1>
    <h2>Employés</h2>
""")

# connection à la base de données

db_connection = sqlite3.connect('./database.sqlite3')
db_connection.row_factory = sqlite3.Row
cursor = db_connection.cursor()

# selection des enregistrements
cursor.execute("SELECT first_name, name, cellphone_number FROM Employee")

# creation de la liste des employés
rows = cursor.fetchall()
print("    <ol>")
for row in rows:
    print('<li>' + row['first_name'] + ' ' + row['name'] + ', ' + row['cellphone_number'] + '</li>')

print("    </ol>")

# formulaire de recherche des employés
print("""
<h2>Employés par service</h2>
<form action="eCarnet_service.py" method="get">
<p><select name="service">
""")
cursor.execute("SELECT id, name FROM Service")
rows = cursor.fetchall()
for row in rows:
    print('    <option value="' + str(row['id']) + '">' + row['name'] + '</option>')
print('    </select><input type="submit" value="Lister" /></p></form>')

#formulaire d'ajout d'un employé
print("""
<h2>Ajouter un nouvel employé</h2>
<form action="eCarnet_add_employee.py" method="get">
    <p>Prénom : <input type="text" name="first_name"/></p>
    <p>Nom : <input type="text" name="name" /></p>
    <p>Matricule : <input type="text" name="registration_number" /></p>
    <p>Tél. fixe : <input type="text" name="cellphone_number" /></p>
    <p>Service : <select name="service">
""")

for row in rows:
    print('    <option value=" ' + str(row['id']) + ' ">' + row['name'] + '</option>')

print("""
    </select></p>
    <p><input type="submit" value="Ajouter" /></p>
    </form>
    </body>
</html>
""")

db_connection.close()
