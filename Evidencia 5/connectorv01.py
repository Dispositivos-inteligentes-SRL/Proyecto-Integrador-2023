import mysql.connector

# Configuración de la conexión a la base de datos
connection = mysql.connector.connect(
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
    for propietario in propietarios:
        print(propietario)

    cursor.close()

# Método de actualización de datos en la tabla propietarios
def update_propietario(prop_id, nombre, apellido, direccion, telefono, mail):
    cursor = connection.cursor()

    # Sentencia SQL para actualizar un propietario en la tabla propietarios
    update_query = "UPDATE propietarios SET Nombre=%s, Apellido=%s, Direccion=%s, Telefono=%s, Mail=%s WHERE idpropietarios=%s"
    values = (nombre, apellido, direccion, telefono, mail, prop_id)

    # Ejecutar la sentencia SQL de actualización
    cursor.execute(update_query, values)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Método de eliminación de un propietario en la tabla propietarios
def delete_propietario(prop_id):
    cursor = connection.cursor()

    # Sentencia SQL para eliminar un propietario de la tabla propietarios
    delete_query = "DELETE FROM propietarios WHERE idpropietarios=%s"
    value = (prop_id,)

    # Ejecutar la sentencia SQL de eliminación
    cursor.execute(delete_query, value)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Función para mostrar el menú y obtener la opción seleccionada
def mostrar_menu():
    print("1. Insertar un nuevo propietario")
    print("2. Mostrar propietarios")
    print("3. Actualizar información de un propietario")
    print("4. Eliminar un propietario")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función para manejar la interacción del usuario con el menú
def ejecutar_menu():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del propietario: ")
            apellido = input("Ingrese el apellido del propietario: ")
            direccion = input("Ingrese la dirección del propietario: ")
            telefono = input("Ingrese el teléfono del propietario: ")
            mail = input("Ingrese el correo electrónico del propietario: ")
            insert_propietario(nombre, apellido, direccion, telefono, mail)
            print("Propietario insertado exitosamente.\n")
        
        elif opcion == "2":
            print("Listado de propietarios:")
            select_propietarios()
            print()
        
        elif opcion == "3":
            prop_id = input("Ingrese el ID del propietario que desea actualizar: ")
            nombre = input("Ingrese el nuevo nombre del propietario: ")
            apellido = input("Ingrese el nuevo apellido del propietario: ")
            direccion = input("Ingrese la nueva dirección del propietario: ")
            telefono = input("Ingrese el nuevo teléfono del propietario: ")
            mail = input("Ingrese el nuevo correo electrónico del propietario: ")
            update_propietario(prop_id, nombre, apellido, direccion, telefono, mail)
            print("Propietario actualizado exitosamente.\n")
        
        elif opcion == "4":
            prop_id = input("Ingrese el ID del propietario que desea eliminar: ")
            delete_propietario(prop_id)
            print("Propietario eliminado exitosamente.\n")
        
        elif opcion == "5":
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.\n")

# Llamar a la función para crear la tabla propietarios
create_table_propietarios()

# Llamar a la función para ejecutar el menú
ejecutar_menu()

# Cerrar la conexión a la base de datos
connection.close()
