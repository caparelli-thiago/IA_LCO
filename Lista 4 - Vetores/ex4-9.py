from copy import deepcopy
import numpy as np

# Escreva aqui o seu programa
def ordena(vetor):
  if len(vetor) > 1:
    for qtd in range(len(vetor)):
      for index in range(len(vetor)-1):
        if vetor[index] > vetor[index+1]:
          temp = vetor[index]
          vetor[index] = vetor[index+1]
          vetor[index+1] = temp

A = np.array([],dtype=int)
for index in range(10):
  valor = int(input("Entre com um valor: "))
  A = np.append(A,valor)
  print(f'Vetor com elemento inserido: {A}')
  B = deepcopy(A)
  ordena(B) # Se passar o vetor A, vai modificá-lo
  # Outra forma de fazer, sem manipular o vetor
  # B = np.sort(B)
  print(f'Vetor ordenado: {B}')