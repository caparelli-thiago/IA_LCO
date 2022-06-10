import numpy as np

# Escreva aqui o seu programa
A = np.zeros(10, dtype=int)
B = np.zeros(10, dtype=int)
C = np.zeros(20, dtype=int)

for index in range(10):
  A[index] = int(input("Entre com um valor para o vetor A: "))

for index in range(10):
  B[index] = int(input("Entre com um valor para o vetor B: "))

for index in range(20):
  if index % 2 == 0:
    C[index] = A[int(index/2)]
  else:
    C[index] = B[int(index/2)]
print(C)