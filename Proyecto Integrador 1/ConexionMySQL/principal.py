import conexion

# Crear una instancia del conector de base de datos
conexion_bd = conexion.Conexion(host="localhost", user="root", password="Paemig.021802", database="proyectointegradorv01")

# Conectar a la base de datos
conexion_bd.connect()

# Leer los propietarios desde la tablapython
propietarios = conexion_bd.leer_propietarios()
for propietarios in propietarios:
    print(propietarios)

print("Fin tabla Propietarios")

conexion_bd.ingresar_propietarios(id_propietarios=1, nombre="Ulises", apellido="Ale", direccion="Hernandez 379", telefono="3585480953", mail="ulisesaale@gmail.com")

# Leer los propietarios desde la tabla
propietarios = conexion_bd.leer_propietarios()
for propietarios in propietarios:
    print(propietarios)

print("Fin tabla Propietarios")

# Desconectar de la base de datos
conexion_bd.disconnect()