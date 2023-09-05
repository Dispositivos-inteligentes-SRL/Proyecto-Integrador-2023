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

# Simula la lectura de datos
datos_manuales = [           
    (25.5, 45.2),
    (26.0, 44.8),
    (24.8, 46.5),
]

for temperatura, humedad in datos_manuales:
    # Inserta los datos en la base de datos
    insert_query = "INSERT INTO lectura_sensor (temperatura, humedad) VALUES (%s, %s)"
    cursor.execute(insert_query, (temperatura, humedad))
    conn.commit()

    print(f"Datos insertados: Temperatura={temperatura}, Humedad={humedad}")

cursor.close()
conn.close()