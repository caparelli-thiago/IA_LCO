import numpy as np

# Escreva aqui o seu programa
A = np.zeros(10)
for index in range(10):
  A[index] = int(input("Entre com um número inteiro: "))
cont = 0
for item in A:
  if item % 2 == 0:
    cont += 1
print(f'Foram inseridos {cont} valores pares.')