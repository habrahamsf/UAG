import networkx as nx

# Se agrega un objeto Graph vacío
G = nx.Graph()

# Agregamos las aristas con peso
edges = [(0, 5, {'weight': 1}), (0, 7, {'weight': 9}), (0, 11, {'weight': 11}), (0, 16, {'weight': 11}),
         (0, 17, {'weight': 3}), (0, 18, {'weight': 9}), (1, 5, {'weight': 5}), (1, 7, {'weight': 1}),
         (1, 9, {'weight': 10}), (1, 15, {'weight': 1}), (1, 16, {'weight': 6}), (1, 19, {'weight': 12}),
         (2, 12, {'weight': 14}), (2, 16, {'weight': 4}), (2, 19, {'weight': 13}), (3, 7, {'weight': 5}),
         (3, 15, {'weight': 1}), (3, 16, {'weight': 10}), (3, 18, {'weight': 4}), (4, 7, {'weight': 3}),
         (4, 8, {'weight': 11}), (4, 11, {'weight': 12}), (4, 13, {'weight': 13}), (4, 16, {'weight': 9}),
         (4, 18, {'weight': 8}), (5, 7, {'weight': 2}), (5, 8, {'weight': 2}), (5, 9, {'weight': 13}),
         (5, 11, {'weight': 1}), (5, 14, {'weight': 12}), (6, 7, {'weight': 8}), (6, 10, {'weight': 6}),
         (6, 13, {'weight': 13}), (6, 15, {'weight': 5}), (6, 18, {'weight': 13}), (7, 8, {'weight': 2}),
         (7, 11, {'weight': 13}), (7, 16, {'weight': 4}), (7, 17, {'weight': 6}), (7, 19, {'weight': 7}),
         (8, 13, {'weight': 8}), (8, 14, {'weight': 10}), (8, 16, {'weight': 14}), (9, 16, {'weight': 9}),
         (10, 17, {'weight': 7}), (10, 19, {'weight': 5}), (11, 13, {'weight': 12}), (11, 14, {'weight': 13}),
         (11, 15, {'weight': 2}), (12, 13, {'weight': 9}), (12, 15, {'weight': 7}), (12, 17, {'weight': 8}),
         (13, 15, {'weight': 1}), (13, 18, {'weight': 9}), (13, 19, {'weight': 6}), (14, 18, {'weight': 9}),
         (15, 18, {'weight': 2}), (17, 18, {'weight': 14}), (17, 19, {'weight': 13})]
#se agregan las aristas al grafo
G.add_edges_from(edges)

# Utilizamos el algoritmo de Dijkstra para encontrar la ruta mínima desde el nodo 0 hasta el nodo 14
path = nx.dijkstra_path(G, source=0, target=14)

# Imprimimos la ruta mínima 
print("Ruta mínima:", path)
