import numpy as np

# Escreva aqui o seu programa

# Formato do gabarito: [MAT, Q1, Q2, .... Q9, Q10]

conv = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5}

GAB = np.zeros(11)
#Banco de dados da classe - 3 alunos, 11 linhas (mat + 10 q)
BDC = np.zeros([3,11])

for i in range(1,11):
  GAB[i] = conv[input(f'Entre com o gabarito da questão {i}: ')]
  #por simplicidade, não será verificado se a resposta é válida

for i in range(3):
  BDC[i,0] = int(input(f'Entre com o número de matrícula do aluno {i+1}: '))
  for j in range(1,11):
    BDC[i,j] = conv[input(f'Entre com a resposta da questão {j}: ')]

print()
cont = 0
nota = np.zeros([3,1])
for i in range(3):
  for j in range(1,11):
    if BDC[i,j] == GAB[j]:
      cont += 1
  nota[i,0] = cont
  print(f'Matrícula: {BDC[i,0]} - Nota da prova: {nota[i,0]}')
  cont = 0
for i in range(3):
  if nota[i,0] > 7 or nota[i,0] == 7:
    cont += 1
print(f'O percentual de aprovação da turma foi: {cont/3*100}%')