def aprende(dados):
	pesos = [0, 0, 0] # W0, W1, b
	for w0, w1, T in dados:
		dw0 = w0 * T
		dw1 = w1 * T
		db = T
		pesos[0] += dw0
		pesos[1] += dw1
		pesos[2] += db
	return pesos


def calcula(entrada, pesos):
	soma = entrada[0] * pesos[0] + entrada[1] * pesos[1] + pesos[2]
	if soma < 2:
		return -1
	else:
		return 1

funcao_and = [[1,1,1],     #W0, W1, T
			  [1,-1,-1],
			  [-1,1,-1],
			  [-1,-1,-1]]

funcao_or = [[1,1,1],     #W0, W1, T
			  [1,-1,1],
			  [-1,1,1],
			  [-1,-1,-1]]

print('Aprendendo AND:')
pesos_and = aprende(funcao_and)

print('Calculando:')
entrada_1 = [1,1]
saida = calcula(entrada_1,pesos_and)
print(f'Entrada 1, 1: "{saida}"')

entrada_1 = [1,-1]
saida = calcula(entrada_1,pesos_and)
print(f'Entrada 1, -1: "{saida}"')

entrada_1 = [-1,1]
saida = calcula(entrada_1,pesos_and)
print(f'Entrada -1, 1: "{saida}"')

entrada_1 = [-1,-1]
saida = calcula(entrada_1,pesos_and)
print(f'Entrada -1, -1: "{saida}"')


print('Aprendendo OR:')
pesos_or = aprende(funcao_or)

print('Calculando:')
entrada_1 = [1,1]
saida = calcula(entrada_1,pesos_or)
print(f'Entrada 1, 1: "{saida}"')

entrada_1 = [1,-1]
saida = calcula(entrada_1,pesos_or)
print(f'Entrada 1, -1: "{saida}"')

entrada_1 = [-1,1]
saida = calcula(entrada_1,pesos_or)
print(f'Entrada -1, 1: "{saida}"')

entrada_1 = [-1,-1]
saida = calcula(entrada_1,pesos_or)
print(f'Entrada -1, -1: "{saida}"')

