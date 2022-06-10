import numpy as np

# Escreva aqui o seu programa
A = np.zeros(20, dtype=int)
for index in range(20):
  A[index] = int(input("Entre com um número inteiro: "))
print(f'Vetor original: {A}')

B = np.array([], dtype=int)
for item in A:
  if item not in B:
    B = np.append(B, item)

# Outra forma de fazer, sem manipular o vetor
# B = np.unique(A)

print(f'Vetor com elementos únicos: {B}')