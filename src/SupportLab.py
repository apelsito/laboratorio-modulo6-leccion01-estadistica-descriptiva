def media_mediana_y_moda(datos):
    media = sum(datos) / len(datos)
    print(f"La media es: {media}")

    # Para la mediana
    if len(datos) % 2 == 0:
        datos_sorted = sorted(datos)
        mediana = (datos_sorted[len(datos)//2 - 1] + datos_sorted[len(datos)//2]) / 2
        print(f"La Mediana es: {mediana}")
    else:
        datos_sorted = sorted(datos)
        mediana = datos_sorted[len(datos)//2]
        print(f"La Mediana es: {mediana}")

    # Para la moda
    dictio_frecuencia = {}
    for dato in datos:
        if dato in dictio_frecuencia:
            dictio_frecuencia[dato] += 1
        else:
            dictio_frecuencia[dato] = 1

    moda = [dato for dato, frecuencia in dictio_frecuencia.items() if frecuencia == max(dictio_frecuencia.values())]
    print(f"La moda es: {moda}")