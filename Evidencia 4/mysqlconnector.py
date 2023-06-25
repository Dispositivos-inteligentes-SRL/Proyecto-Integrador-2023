import mysql.connector

connection = mysql.connector.connect (
  host = 'localhost',
  user = 'root',
  password = 'Paemig.021802',
  database = 'proyectointegradorv01'
)

# Creación de la tabla propietarios en la base de datos existente
def create_table_propietarios():
    cursor = connection.cursor()

    # Sentencia SQL para crear la tabla propietarios
    create_table_query = """
    CREATE TABLE IF NOT EXISTS propietarios (
        idpropietarios INT AUTO_INCREMENT PRIMARY KEY,
        Nombre VARCHAR(50),
        Apellido VARCHAR(50),
        Direccion VARCHAR(100),
        Telefono VARCHAR(20),
        Mail VARCHAR(50)
    )
    """

    # Ejecutar la sentencia SQL para crear la tabla
    cursor.execute(create_table_query)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Método de inserción de datos en la tabla propietarios
def insert_propietario(nombre, apellido, direccion, telefono, mail):
    cursor = connection.cursor()

    # Sentencia SQL para insertar un nuevo propietario en la tabla propietarios
    insert_query = "INSERT INTO propietarios (Nombre, Apellido, Direccion, Telefono, Mail) VALUES (%s, %s, %s, %s, %s)"
    values = (nombre, apellido, direccion, telefono, mail)

    # Ejecutar la sentencia SQL de inserción
    cursor.execute(insert_query, values)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Método de selección de datos desde la tabla propietarios
def select_propietarios():
    cursor = connection.cursor()

    # Sentencia SQL para seleccionar todos los propietarios de la tabla propietarios
    select_query = "SELECT * FROM propietarios"

    # Ejecutar la sentencia SQL de selección
    cursor.execute(select_query)

    # Obtener todos los registros seleccionados
    propietarios = cursor.fetchall()

    # Imprimir los registros
    for propietarios in propietarios:
        print(propietarios)

    cursor.close()

# Llamar a la función para crear la tabla propietarios
create_table_propietarios()

# Llamar al método de inserción de datos
insert_propietario("Guillermina", "Milet", "Hernandez 379", "3584303418", "guillerminamilet@gmail.com")

# Llamar al método de selección de datos
select_propietarios()

# Cerrar la conexión a la base de datos
connection.close()