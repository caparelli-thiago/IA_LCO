import numpy as np

# Escreva aqui o seu programa
A = np.zeros(10)
for index in range(10):
  A[index] = int(input("Entre com um número inteiro: "))
print(A)
#Encontrando o maior e menor valor operando o vetor
maior = A[0] # Inicia com o primeiro valor
posmaior = 0
menor = A[0]
posmenor = 0
for index, item in enumerate(A):
  if item > maior:
    maior = item
    posmaior = index
  if item < menor:
    menor = item
    posmenor = index

#  Outra forma de realizar o exercício é o seguinte:
# maior = max(A)
# posmaior = np.argmax(A)
# menor = min(A)
# posmenor = np.argmin(A)
#  A solução acima, porém, não exercita a operação sobre vetores.

print(f'O maior elemento é "{int(maior)}" na posição {posmaior + 1}')
print(f'O menor elemento é "{int(menor)}" na posição {posmenor + 1}')