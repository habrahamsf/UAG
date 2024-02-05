import heapq

def huffmanCodes(frequencias):
    codigos = {}
    # Creamos un heap para almacenar los nodos del árbol
    heap = [[freq, [char, ""]] for char, freq in frequencias.items()]
    heapq.heapify(heap)
    # Unimos los nodos del heap hasta que solo quede un nodo raíz
    while len(heap) > 1:
        # Tomamos los dos nodos de menor frecuencia
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # agregamos "1" a el lado izquierdo
        for pair in left[1:]:
            pair[1] = "1" + pair[1]
        # agregamos "0" a el lado derecho
        for pair in right[1:]:
            pair[1] = "0" + pair[1]
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    for pair in heap[0][1:]:
        codigos[pair[0]] = pair[1]
    return codigos

frequencias = {'A': 5, 'B': 12, 'C': 35, 'D': 3, 'E': 8, 'F': 14, 'G': 21, 'H': 1, 'I': 39}
codigos = huffmanCodes(frequencias)

# Se imprimen los codigos
print("Simbolo\tCodigo")
for char, freq in frequencias.items():
    #print(f"{char}\t{freq}\t\t{codigos[char]}")
    print(f"{char}\t{codigos[char]}")
