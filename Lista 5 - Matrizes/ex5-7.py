import numpy as np

# Escreva aqui o seu programa
from random import seed
from random import randint

M = np.zeros([4,4],dtype=int)
seed() # Inicializa o gerador de números aleatórios
for i in range(4):
  for j in range(4):
    M[i,j] = randint(1,20)

print(f'Matriz original:')
print(M)

for i in range(4):
  for j in range(4):
    if j > i:
      M[i,j] = 0
print()
print(f'Matriz transformada:')
print(M)