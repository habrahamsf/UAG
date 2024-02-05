p = [5, 10, 3, 12, 5, 50, 6]

def matrixOrder(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def PrintOptimal(s, i, j):
    if i == j:
        return f"A{i}"
    else:
        return f"({PrintOptimal(s, i, s[i][j])}{PrintOptimal(s, s[i][j] + 1, j)})"

m, s = matrixOrder(p)
minCost = m[1][-1]
optimalP = PrintOptimal(s, 1, len(p) - 1)

print(f"Minimo de multiplicaciones escalares: {minCost}")
print(f"Parentizacion: {optimalP}")
