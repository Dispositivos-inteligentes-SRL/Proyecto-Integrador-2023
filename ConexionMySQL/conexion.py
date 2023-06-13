import mysql.connector

class   Conexion:
    def __init__(self, host, user, password, database):
        self.host = host,
        self.user = user,
        self.password = password,
        self.database = database,
        self.connection = None
        
    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Conexion existosa")
