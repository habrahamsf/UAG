largo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
precios = [1, 4, 10, 12, 15, 20, 21, 32, 31, 41, 51]

def cortarCuerda(largo, precios):
    n = len(largo)
    r = [0] * (n + 1)
    cut = [0] * (n + 1)
    # itero sobre todas las longitudes posibles
    for j in range(1, n + 1):
        q = float('-inf')
        #se itera sobre los posibles cortes del largo actual
        for i in range(1, j):
            if q < precios[i] + r[j - i - 1]:
                q = precios[i] + r[j - i - 1]
                cut[j] = i + 1
        r[j] = q # se guarda el precio maximo

    descomposicion = []
    longitud = n
    while longitud > 0:
        descomposicion.append(cut[longitud])
        longitud -= cut[longitud]

    return r[n], descomposicion

# Llama a la funcion y guarda resultados
precioMax, descomposicionOptima = cortarCuerda(largo, precios)

print("Precio maximo para venderla:", precioMax)
print("Descomposicion optima:", "".join(str(x)for x in descomposicionOptima))
