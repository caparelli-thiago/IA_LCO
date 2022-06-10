import numpy as np

# Escreva aqui o seu programa
M = np.zeros([4,4],dtype=int)
for i in range(4):
  for j in range(4):
    M[i,j] = int(input(f'Entre com o número da posição M[{i+1},{j+1}]: '))
cont = 0
for linha in M:
  for item in linha:
    if item > 10:
      cont +=1
print(M)
if cont == 0:
  print(f'A matriz não possui valores maiores que dez.')
else:
  print(f'A matriz possui {cont} valores maiores que dez.')