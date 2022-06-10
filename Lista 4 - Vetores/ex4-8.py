import numpy as np

# Escreva aqui o seu programa
X = np.array([])
Y = np.array([])

for index in range(5):
  valor = int(input("Entre com um valor para ""X"": "))
  while valor in X:
    print("O valor informado já existe em ""X"".")
    valor = int(input("Entre com outro valor para ""X"": "))
  X = np.append(X,valor)

for index in range(5):
  valor = int(input("Entre com um valor para ""Y"": "))
  while valor in Y:
    print("O valor informado já existe em ""Y"".")
    valor = int(input("Entre com outro valor para ""Y"": "))
  Y = np.append(Y,valor)

print(f'Vetor X: {X}')
print(f'Vetor Y: {Y}')
soma = X + Y
print(f'Soma entre X e Y: {soma}')
produto = X * Y
print(f'Produto entre X e Y: {produto}')

dif = np.array([])
for valor in X:
  if valor not in Y:
    dif = np.append(dif,valor)
#Outra forma de fazer, sem manipular vetores
#dif = list(set(X).difference(Y))    
print(f'A diferença entre X e Y é: {dif}')

intersec = np.array([])
for valor in X:
  if valor in Y:
    intersec = np.append(intersec,valor)
#Outra forma de fazer, sem manipular vetores
#intersec = list(set(X).intersection(Y))  
print(f'A interseção entre X e Y é: {intersec}')

uniao = np.copy(X)
for valor in Y:
  if valor not in X:
    uniao = np.append(uniao, valor)
#Outra forma de fazer, sem manipular vetores
#uniao = list(set(X).union(Y))  
print(f'A união entre X e Y é: {uniao}')