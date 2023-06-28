import mysql.connector

# Configuración de la conexión a la base de datos
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Paemig.021802',
    database = 'proyectointegradorv01'
)

# Creación de la tabla Componentes Electronicos en la base de datos existente
def create_table_compelectronico():
    cursor = connection.cursor()

    # Sentencia SQL para crear la tabla Componentes Electronicos
    create_table_query = """
    CREATE TABLE IF NOT EXISTS compelectronico (
        Id INT AUTO_INCREMENT PRIMARY KEY,
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

    # Sentencia SQL para insertar un nuevo insumo en la tabla Componentes Electronicos
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

    # Sentencia SQL para seleccionar todos los insumos de la tabla Componentes Electronicos
    select_query = "SELECT * FROM compelectronico"

    # Ejecutar la sentencia SQL de selección
    cursor.execute(select_query)

    # Obtener todos los registros seleccionados
    compelectronico = cursor.fetchall()

    # Imprimir los registros
    for compelectronico in compelectronico:
        print(compelectronico)

    cursor.close()

# Método de actualización de datos en la tabla de Componentes Electronicos
def update_compelectronico(prod_id, producto, marca, modelo, precio, stock):
    cursor = connection.cursor()

    # Sentencia SQL para actualizar un insumo en la tabla de Componentes Electronicos
    update_query = "UPDATE compelectronico SET Producto=%s, Marca=%s, Modelo=%s, Precio=%s, Stock=%s WHERE prod_id=%s"
    values = (producto, marca, modelo, precio, stock, prod_id)

    # Ejecutar la sentencia SQL de actualización
    cursor.execute(update_query, values)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Método de eliminación de un insumo en la tabla de Componentes Electronicos
def delete_compelectronico(prod_id):
    cursor = connection.cursor()

    # Sentencia SQL para eliminar un insumo de la tabla Componentes Electronicos
    delete_query = "DELETE FROM compelectronico WHERE prod_id=%s"
    value = (prod_id,)

    # Ejecutar la sentencia SQL de eliminación
    cursor.execute(delete_query, value)

    # Confirmar los cambios en la base de datos
    connection.commit()

    cursor.close()

# Función para mostrar el menú y obtener la opción seleccionada
def mostrar_menu():
    print("1. Insertar un nuevo insumo")
    print("2. Mostrar materiales")
    print("3. Actualizar información de un insumo")
    print("4. Eliminar un insumo")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función para manejar la interacción del usuario con el menú
def ejecutar_menu():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            producto = input("Ingrese el componente electronico: ")
            marca = input("Ingrese la marca del componente electronico: ")
            modelo = input("Ingrese el modelo del componente electronico: ")
            precio = input("Ingrese el precio del componente electronico: ")
            stock = input("Ingrese el stock del componente electronico: ")
            insert_compelectronico(producto, marca, modelo, precio, stock)
            print("Componente electronico insertado exitosamente.\n")
        
        elif opcion == "2":
            print("Listado de :")
            select_compelectronico()
            print()
        
        elif opcion == "3":
            prod_id = input("Ingrese el ID del insumo que desea actualizar: ")
            producto = input("Ingrese el componente electronico: ")
            marca = input("Ingrese la marca del componente electronico: ")
            modelo = input("Ingrese el modelo del componente electronico: ")
            precio = input("Ingrese el precio del componente electronico: ")
            stock = input("Ingrese el stock del componente electronico: ")
            update_compelectronico(prod_id, producto, marca, modelo, precio, stock)
            print("Componente electronico actualizado exitosamente.\n")
        
        elif opcion == "4":
            prod_id = input("Ingrese el ID del componente electronico que desea eliminar: ")
            delete_compelectronico(prod_id)
            print("Componente electronico eliminado exitosamente.\n")
        
        elif opcion == "5":
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.\n")

# Llamar a la función para crear la tabla componentes electronicos
create_table_compelectronico()

# Llamar a la función para ejecutar el menú
ejecutar_menu()

# Cerrar la conexión a la base de datos
connection.close()
