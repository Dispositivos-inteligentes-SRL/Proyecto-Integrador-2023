import mysql.connector

connection = mysql.connector.connect (
  host = 'localhost',
  user = 'root',
  password = 'Paemig.021802',
  database = 'proyectointegradorv01'
)

if connection.is_connected():
    print('Conexión exitosa a la base de datos')

# Realizar operaciones en la base de datos...

# Cerrar la conexión
connection.close()