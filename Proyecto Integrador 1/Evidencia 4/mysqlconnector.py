import mysql.connector

connection = mysql.connector.connect (
  host = 'localhost',
  user = 'root',
  password = 'Paemig.021802',
  database = 'proyectointegradorv01'
)

# Creación de la tabla propietarios en la base de datos existente
def create_table_compelectronico():
    cursor = connection.cursor()

    # Sentencia SQL para crear la tabla propietarios
    create_table_query = """
    CREATE TABLE IF NOT EXISTS compelectronico (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Producto VARCHAR(50),
        Marca VARCHAR(50),
        Modelo VARCHAR(100),
        Precio VARCHAR(20),
        Stock VARCHAR(20)
    )
    """

    # Ejecutar la sentencia SQL para crear la tabla
    cursor.execute(create_table_query)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Método de inserción de datos en la tabla Componentes Electronicos
def insert_compelectronico(producto, marca, modelo, precio, stock):
    cursor = connection.cursor()

    # Sentencia SQL para insertar un nuevo propietario en la tabla Componentes Electronicos
    insert_query = "INSERT INTO compelectronico (producto, marca, modelo, precio, stock) VALUES (%s, %s, %s, %s, %s)"
    values = (producto, marca, modelo, precio, stock)

    # Ejecutar la sentencia SQL de inserción
    cursor.execute(insert_query, values)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Método de selección de datos desde la tabla Componentes Electronicos
def select_compelectronico():
    cursor = connection.cursor()

    # Sentencia SQL para seleccionar todos los propietarios de la tabla Componentes Electronicos
    select_query = "SELECT * FROM compelectronico"

    # Ejecutar la sentencia SQL de selección
    cursor.execute(select_query)

    # Obtener todos los registros seleccionados
    compelectronico = cursor.fetchall()

    # Imprimir los registros
    for compelectronico in compelectronico:
        print(compelectronico)

    cursor.close()

# Llamar a la función para crear la tabla Componentes Electronicos
create_table_compelectronico()

# Llamar al método de inserción de datos
insert_compelectronico("Ethernet", "ETH1000", "TP-Link", "7030", "1000")

# Llamar al método de selección de datos
select_compelectronico()

# Cerrar la conexión a la base de datos
connection.close()