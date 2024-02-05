import numpy as np

n = 10 # numero de objetos disponibles
pesos = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
valores = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
capacidadMax = 140

def mochila(n, pesos, valores, capacidadMax):
    # inicializo la matriz a ceros
    V = np.zeros((n + 1, capacidadMax + 1), dtype = int)

    #itero sobre los objetos
    for i in range(1, n + 1):
        #itero sobre la capacidad de la mochila
        for x in range(0, capacidadMax + 1):
            j = x - pesos[i - 1]
            if i == 0 or x == 0:
                V[i][x] = 0
            elif pesos[i - 1] <= x:
                V[i][x] = max(V[i - 1][x], V[i - 1][j] + valores[i - 1])
            else:
                V[i][x] = V[i - 1][x]
    return V

def objetosSeleccionados(V, pesos, n, capacidadMax):
    # Se inicializa una lista vacia para almacenar los objetos seleccionados
    objetos = [] 
    x = capacidadMax

    # Retrocedo en la matriz V para encontrar los objetos seleccionados
    for i in range(n, 0, -1):
        if V[i][x] != V[i - 1][x]:
            objetos.append(i)
            x -= pesos[i - 1]

    objetos.reverse()
    return objetos

V = mochila(n, pesos, valores, capacidadMax)
valorOptimo = V[n][capacidadMax]
objetosTomados = objetosSeleccionados(V, pesos, n, capacidadMax)

print(f"Valor optimo de la mochila: {valorOptimo}")
print(f"Objetos a tomar: {objetosTomados}")
