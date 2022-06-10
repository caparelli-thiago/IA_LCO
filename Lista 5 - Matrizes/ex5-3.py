import numpy as np

# Escreva aqui o seu programa
qtd = int(input("Entre com o tamanho da matriz(linhas=colunas): "))
M = np.zeros([qtd,qtd])
for i in range(qtd):
  for j in range(qtd):
    M[i,j] = (i+1) * (j+1)
print(M)