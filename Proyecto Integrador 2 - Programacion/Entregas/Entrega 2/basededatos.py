import mysql.connector

# Configuracion de la Base de Datos
db_config = {
    "host": "localhost",
    "user": "admin",
    "password": "Paemig.021802",
    "database": "datos_sensor",  
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

datos_manuales = [           # Simula la lectura de datos
    (25.5, 45.2),
    (26.0, 44.8),
    (24.8, 46.5),
]

for Temperatura, Humedad in datos_manuales:
    # Inserta los datos en la base de datos
    insert_query = "INSERT INTO lectura_sensor (Temperatura, Humedad) VALUES (%s, %s)"
    cursor.execute(insert_query, (Temperatura, Humedad))
    conn.commit()

    print(f"Datos insertados: Temperatura={Temperatura}, Humedad={Humedad}")

cursor.close()
conn.close()
