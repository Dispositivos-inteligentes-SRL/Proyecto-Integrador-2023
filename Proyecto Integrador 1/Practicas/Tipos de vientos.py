def traducir_direccion_viento(numero):
    direccion_viento = {
        0: 'Norte',
        1: 'Noreste',
        2: 'Este',
        3: 'Sureste',
        4: 'Sur',
        5: 'Suroeste',
        6: 'Oeste',
        7: 'Noroeste'
    }
    
    if numero in direccion_viento:
        return direccion_viento[numero]
    else:
        return 'Dirección de viento inválida'

numero_direccion_viento = 7
direccion_texto = traducir_direccion_viento(numero_direccion_viento)
print(direccion_texto)  # Imprime "Sureste"