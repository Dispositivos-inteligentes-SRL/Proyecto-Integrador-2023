def estado_bateria(porcentaje_carga):
    if porcentaje_carga >= 80:
        return "Cargada"
    elif 30 <= porcentaje_carga <= 79:
        return "Mediana carga"
    else:
        return "Baja carga, REEMPLAZAR"


porcentaje_carga = 80
estado = estado_bateria(porcentaje_carga)
print(estado)
