import mysql.connector

class   Conexion:
    def __init__(self, host, user, password, database):
        self.host= host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        
    def connect(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        if self.connection.is_connected():
            print("Conexion existosa")

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Paemig.021802",
    database="proyectointegradorv01"
)
print(midb)

cursor = midb.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)
