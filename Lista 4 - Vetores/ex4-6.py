import numpy as np

# Escreva aqui o seu programa
A = np.zeros(10)
for index in range(10):
  A[index] = float(input("Entre com um número: "))
print("---")
val = float(input("Entre com outro número: "))
cont = 0
valores = "["
for item in A:
  if item % val == 0:
    cont += 1
    valores += str(item)
    valores += ","
valores = valores[:-1] #remove o último caracter da string, no caso ","
valores += "]"
print(f'O vetor contem {cont} multiplos de {val}: {valores}')