import numpy as np

# Escreva aqui o seu programa

def soma_matrizes():
  C = A + B
  print(C)

def subtrai_matrizes():
  C = B - A
  print(C)

def adiciona_matrizes():
  cons = int(input(f'Entre com a constante a ser somada: '))
  C = A + cons
  D = B + cons
  print(C)
  print()
  print(D)

def multiplica_matrizes():
  C = np.dot(A,B)
  print(C)

def imprime_matrizes():
  print(A)
  print()
  print(B)


A = np.zeros([3,3],dtype=float)
B = np.zeros([3,3],dtype=float)

for i in range(3):
  for j in range(3):
    A[i,j] = float(input(f'Entre com um número para a posição A[{i+1},{j+1}]: '))  
for i in range(3):
  for j in range(3):
    B[i,j] = float(input(f'Entre com um número para a posição B[{i+1},{j+1}]: '))  

select = 0
while select != 6:
  print()
  print()
  print(f'Selecione uma opção:')
  print(f'1. Somar as duas matrizes')
  print(f'2. Subtrair a primeira matriz da segunda')
  print(f'3. Adicionar uma constante as duas matrizes')
  print(f'4. Multiplicar as duas matrizes')
  print(f'5. Imprimir as matrizes')
  print(f'6. Sair')
  select = int(input())
  print()
  if select == 1:
    soma_matrizes()
  elif select == 2:
    subtrai_matrizes()
  elif select == 3:
    adiciona_matrizes()
  elif select == 4:
    multiplica_matrizes()
  elif select == 5:
    imprime_matrizes()
  else:
    pass
print(f'Finalizando programa.')