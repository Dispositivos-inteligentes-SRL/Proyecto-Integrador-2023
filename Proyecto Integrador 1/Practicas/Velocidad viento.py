def calcular_velocidad_promedio(velocidades):
    if len(velocidades) == 0:
        return 0
    else:
        total = sum(velocidades)
        promedio = total / len(velocidades)
        return promedio

print = in(imput("Ingrese las velocidades del viento"))
velocidad_promedio = calcular_velocidad_promedio(velocidades)
print("La velocidad promedio del viento es:", velocidad_promedio, "m/s")