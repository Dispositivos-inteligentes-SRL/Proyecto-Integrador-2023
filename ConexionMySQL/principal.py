import conexion

# Crear una instancia del conector de base de datos
conexion_bd = conexion.Conexion(host="localhost", user="root", password="Paemig.021802", database="proyectointegradorv01")

# Conectar a la base de datos
conexion_bd.connect()

# Leer los propietarios desde la tablapython
propietarios = conexion_bd.leer_propietarios()
for propietario in propietarios:
    print(propietario)

print("Fin tabla Propietarios")

conexion_bd.ingresar_propietario(id_propietario=1, nombre="Ulises", apellido="Ale", fecha_nacimiento="1979-10-19")

# Leer los propietarios desde la tabla
propietarios = conexion_bd.leer_propietarios()
for propietario in propietarios:
    print(propietario)

print("Fin tabla Propietarios")

# Desconectar de la base de datos
conexion_bd.disconnect()