import numpy as np

# Escreva aqui o seu programa
from random import seed
from random import randint

M = np.zeros([5,5],dtype=int)
seed() # Inicializa o gerador de números aleatórios
for i in range(5):
  for j in range(5):
    valor = randint(0,99)
    while valor in M:
      valor = randint(0,99)
    M[i,j] = valor
print(M)

# Caso queira uma cartela mais bonita e funcional,
# podemos ordenar os números
# O = np.sort(M, axis=None)
# O = np.reshape(O, (5,5))
# print()
# print(O)