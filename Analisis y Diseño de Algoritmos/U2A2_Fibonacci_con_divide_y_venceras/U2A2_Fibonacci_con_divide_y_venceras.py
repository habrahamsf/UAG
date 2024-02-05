def Fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    F = [[0,1],[1,1]]
    Fexp = exp(F, n-1)
    return Fexp[1][1]

def M_Multiplicacion(A, B):
  C = [[0,0],[0,0]]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        C[i][j] += A[i][k] * B[k][j]
  return C

def exp(F, n):

    if n == 1:
        return F
    elif (n % 2 == 0):
        Fexp = exp(F, n/2)
        return M_Multiplicacion(Fexp, Fexp)
    else:
        Fexp = exp(F, (n-1)/2)
        return M_Multiplicacion(M_Multiplicacion(Fexp, Fexp), F)

if __name__ == '__main__':

    n = int(input('Escribe el valor de n: '))
    
    result = Fibo(n)
    print(result)
