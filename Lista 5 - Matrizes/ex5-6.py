import numpy as np

# Escreva aqui o seu programa
A = np.zeros([4,4],dtype=int)
B = np.zeros([4,4],dtype=int)
C = np.zeros([4,4],dtype=int)

for i in range(4):
  for j in range(4):
    A[i,j] = int(input(f'Entre com um valor para A[{i+1},{j+1}]: '))
print()
for i in range(4):
  for j in range(4):
    B[i,j] = int(input(f'Entre com um valor para B[{i+1},{j+1}]: '))
print()
for i in range(4):
  for j in range(4):
    if A[i,j] > B[i,j]:
      C[i,j] = A[i,j]
    else:
      C[i,j] = B[i,j]
print(A)
print()
print(B)
print()
print(C)