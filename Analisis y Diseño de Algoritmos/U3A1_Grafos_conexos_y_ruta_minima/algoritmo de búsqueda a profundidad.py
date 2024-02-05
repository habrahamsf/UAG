def busquedaProfundidad(grafo, inicio, reviwed):
    reviwed.add(inicio)
    for neighbor in grafo[inicio]:
        if neighbor not in reviwed:
            busquedaProfundidad(grafo, neighbor, reviwed)
'''utiliza la función "busquedaProfundidad" para encontrar 
   los componentes conectados en el grafo no dirigido "grafo".
'''
def busquedaComponentes(grafo):
    reviwed = set()
    components = []
    for node in grafo:
        if node not in reviwed:
            component = set()
            busquedaProfundidad(grafo, node, component)
            components.append(component)
            reviwed |= component
    return components

#vertices y aristas
nodes = list(range(50))
edges = [(0, 29), (0, 46), (0, 21), (0, 14), (0, 38), (0, 31), (1, 41), (1, 31), 
        (1, 21), (1, 17), (2, 9), (2, 26), (2, 5), (2, 25), (2, 4), (3, 18), (3, 30), 
        (3, 47), (4, 28), (4, 9), (4, 8), (5, 44), (5, 12), (6, 37), (6, 10), (7, 23), 
        (7, 22), (7, 39), (9, 19), (9, 28), (9, 27), (11, 33), (13, 25), (13, 38), (13, 29), 
        (14, 26), (14, 28), (14, 39), (15, 22), (15, 31), (15, 19), (15, 41), (16, 46), (16, 26), 
        (16, 38), (16, 27), (17, 40), (17, 29), (18, 45), (18, 42), (18, 35), (18, 33), (18, 47), 
        (20, 36), (20, 49), (20, 42), (22, 26), (22, 34), (23, 31), (23, 32), (23, 40), (24, 31), 
        (24, 44), (25, 38), (26, 31), (27, 32), (29, 48), (29, 41), (30, 47), (30, 37), (33, 36), 
        (33, 49), (34, 48), (35, 45), (36, 45), (37, 49), (37, 45), (37, 47), (38, 41), (40, 48), 
        (41, 44), (42, 49), (43, 48), (45, 47)]
#lista de adyacencia
grafo = {node: set() for node in nodes}
for edge in edges:
    grafo[edge[0]].add(edge[1])
    grafo[edge[1]].add(edge[0])

# Encontrar componentes conexos
components = busquedaComponentes(grafo)

# Imprimir vértices de cada componente
for i, component in enumerate(components):
    print(f"Subgrafo {i + 1}: {list(component)}")


