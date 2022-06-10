import numpy as np

# Escreva aqui o seu programa
M = np.zeros([4,4],dtype=int)
for i in range(4):
  for j in range(4):
    M[i,j] = int(input(f'Entre com um valor para a posição M[{i+1},{j+1}]: '))
selec = np.NINF
for i in range(4):
  for j in range(4):
    if M[i,j] > selec:
      selec = M[i,j]
      pos = (i+1,j+1)
print(f'O maior valor é "{selec}", na posição {pos}.')