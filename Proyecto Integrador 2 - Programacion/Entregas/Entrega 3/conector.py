import mysql.connector

# Configuracion de la Base de Datos
connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Paemig.021802',
        database='datos_sensor'
    )

if connection.is_connected():
        print("Conexión a MySQL exitosa.")
    

# Datos tomados de la carga de temperatura y humedad
def create_table_lectura_sensor():
    cursor = connection.cursor()

    # Sentencia SQL para crear la tabla del sensor DHT22
    create_table_query = """
    CREATE TABLE IF NOT EXISTS lectura_sensor (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Temperatura DECIMAL(5, 2),
        Humedad DECIMAL(5, 2),
        Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    # Ejecutar la sentencia SQL para crear la tabla
    cursor.execute(create_table_query)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Método de inserción de datos en la tabla
def insert_lectura_sensor(Temperatura, Humedad):
    cursor = connection.cursor()

    # Sentencia SQL para insertar un nuevo dato del sensor
    insert_query = "INSERT INTO lectura_sensor (Temperatura, Humedad) VALUES (%s, %s)"
    values = (Temperatura, Humedad)

    # Ejecutar la sentencia SQL de inserción
    cursor.execute(insert_query, values)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Método de selección de datos desde la tabla del sensor
def select_lectura_sensor():
    cursor = connection.cursor()

    # Sentencia SQL para seleccionar todos los datos de la tabla del sensor
    select_query = "SELECT * FROM lectura_sensor"

    # Ejecutar la sentencia SQL de selección
    cursor.execute(select_query)

    # Obtener todos los registros seleccionados
    lectura_sensor = cursor.fetchall()

    # Imprimir los registros
    for lectura_sensor in lectura_sensor:
        print(lectura_sensor)

    cursor.close()

# Método de actualización de datos en la tabla del sensor
def update_lectura_sensor(ID, Temperatura, Humedad):
    cursor = connection.cursor()

    # Sentencia SQL para actualizar un dato del sensor en la tabla
    update_query = "UPDATE lectura_sensor SET Temperatura=%s, Humedad=%s WHERE ID=%s"
    values = (Temperatura, Humedad, ID)

    # Ejecutar la sentencia SQL de actualización
    cursor.execute(update_query, values)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Método de eliminación de un dato de la tabla del sensor
def delete_lectura_sensor(ID):
    cursor = connection.cursor()

    # Sentencia SQL para eliminar un dato de la tabla del sensor
    delete_query = "DELETE FROM lectura_sensor WHERE ID=%s"
    value = (ID,)

    # Ejecutar la sentencia SQL de eliminación
    cursor.execute(delete_query, value)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Función para mostrar el menú y obtener la opción seleccionada
def mostrar_menu():
    print("1. Insertar Temperatura y Humedad")
    print("2. Mostrar datos")
    print("3. Actualizar información de datos")
    print("4. Eliminar un datos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función para manejar la interacción del usuario con el menú
def ejecutar_menu():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            Temperatura = input("Ingrese la Temperatura: ")
            Humedad = input("Ingrese la Humedad: ")
            insert_lectura_sensor(Temperatura, Humedad)
            print("Datos sensados insertado exitosamente.\n")
        
        elif opcion == "2":
            print("Datos ingresados :")
            select_lectura_sensor()
            print()
        
        elif opcion == "3":
            ID = input("Ingrese el ID que desea actualizar: ")
            Temperatura = input("Ingrese la Temperatura: ")
            Humedad = input("Ingrese la Humedad: ")
            update_lectura_sensor(ID, Temperatura, Humedad)
            print("Datos del sensor actualizado exitosamente.\n")
        
        elif opcion == "4":
            ID = input("Ingrese el ID que desea eliminar: ")
            delete_lectura_sensor(ID)
            print("Datos del sensor eliminado exitosamente.\n")
        
        elif opcion == "5":
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.\n")

# Llamar a la función para crear la tabla del sensor
create_table_lectura_sensor()

# Llamar a la función para ejecutar el menú
ejecutar_menu()

# Cerrar la conexión a la base de datos
connection.close()

