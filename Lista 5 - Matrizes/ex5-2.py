import numpy as np

# Escreva aqui o seu programa
M = np.zeros([5,5],dtype=int)
for i in range(5):
  M[i,i] = 1
print(M)