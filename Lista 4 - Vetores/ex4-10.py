import numpy as np

# Escreva aqui o seu programa
T = np.array([],dtype=int)
valor = int(input("entre com um valor inteiro positivo: "))
while valor < 1:
  print("O valor não é positivo.")
  valor = int(input("entre com um valor inteiro positivo: "))

for index in range(valor):
  T = np.append(T,1)
  if index > 1:
    U = np.copy(T)
    for jdex in range(1,len(T)-1):
      T[jdex] = U[jdex] + U[jdex-1]
  print(T)