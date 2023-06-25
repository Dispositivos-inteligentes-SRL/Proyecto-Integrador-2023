import mysql.connector

class Conexion:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Conexión exitosa")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Desconexión")

    def leer_propietarios(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "SELECT * FROM Propietario"
            cursor.execute(query)
            propietarios = cursor.fetchall()
            cursor.close()
            return propietarios
        else:
            print("No hay conexión a la base de datos")

    def ingresar_propietario(self, id_propietario, nombre, apellido, direccion, telefono, mail):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "INSERT INTO propietario (id_propietario, Nombre, Apellido, Direccion, Telefono, Mail) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (id_propietario, nombre, apellido, direccion, telefono, mail)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            print("Datos insertados correctamente")
        else:
            print("No hay conexión a la base de datos")