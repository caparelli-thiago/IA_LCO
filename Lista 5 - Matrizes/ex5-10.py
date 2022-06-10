import numpy as np

# Escreva aqui o seu programa
M = np.zeros([3,6],dtype=float)
for i in range(3):
  for j in range(6):
    M[i,j] = float(input(f'Entre com um número para a posição [{i+1},{j+1}]: '))  
print(M)

print()
soma = 0.0
for i in range(3):
  for j in range(0,6,2):
    soma += M[i,j]
# Outra forma de fazer, sem manipular a matriz
# soma = np.sum(M[0:3,0:6:2])
print(f'A soma de todos os elementos das colunas ímpares é: {soma}')

print()
soma = 0.0
cont = 0
for i in range(3):
  for j in range(1,4,2):
    soma += M[i,j]
    cont += 1
# Outra forma de fazer, sem manipular a matriz
# media = np.average(M[0:3,1:4:2])
media = soma / cont
print(f'A média aritmética dos elementos da segunda e quarta colunas é: {media}')

print()
for i in range(3):
  M[i,5] = M[i,0] + M[i,1]
# Outra forma de fazer, sem manipular a matriz
# M[0:3,5] = np.sum(M[0:3,0:2],1)
print(M)