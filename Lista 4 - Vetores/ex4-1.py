import numpy as np

# Escreva aqui o seu programa
A = np.array([1, 0, 5, -2, -5, 7])
S = A[0] + A[1] + A[5]
print(f'A soma dos valores da posição 0, 1 e 5 é: {S}')
A[3] = 100
for item in A:
  print(f'{item}')