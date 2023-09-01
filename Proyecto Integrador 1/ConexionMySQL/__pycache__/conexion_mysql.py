import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Paemig.021802",
    database="proyectointegradorv01"
)
print(midb)

cursor = conexion.cursor()

cursor.execute("SHOW DATABASES")
for bd in cursor:  # type: ignore
    print(bd)