import numpy as np

# Escreva aqui o seu programa
A = np.array([0,0,0,0,0,0])

for index in range(6):
  valor = int(input("Entre com um valor par: "))
  while valor % 2 != 0:
    valor = int(input("O valor não é par! Entre com um valor par: "))
  A[index] = valor
print(f'Vetor Original: {A}')

for index in range(3):
  temp = A[index]
  A[index] = A[5-index]
  A[5-index] = temp

# Outra forma de fazer, sem manipulação de vetor
# np.flip(A)

print(A)