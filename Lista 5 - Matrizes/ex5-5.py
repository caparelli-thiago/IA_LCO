import numpy as np

# Escreva aqui o seu programa
M = np.zeros([5,5],dtype=int)
for i in range(5):
  for j in range(5):
    M[i,j] = int(input(f'Entre com um valor para a posição M[{i+1},{j+1}]: '))
valor = int(input("Entre com um valor: "))
achou = False
for i in range(5):
  for j in range(5):
    if M[i,j] == valor:
      achou = True
      print(f'Elemento "{valor}" na posição ({i+1},{j+1}).')
if not achou:
  print(f'Valor "{valor}" não encontrado.')