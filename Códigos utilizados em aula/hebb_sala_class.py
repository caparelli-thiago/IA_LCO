class neuronio_hebb:
	
	def __init__(self, pesos = None):
		if pesos is None:
			self.pesos = [0, 0, 0]
		else:
			self.pesos = pesos

	def aprende(self, dados):
		for w0, w1, T in dados:
			dw0 = w0 * T
			dw1 = w1 * T
			db = T
			self.pesos[0] += dw0
			self.pesos[1] += dw1
			self.pesos[2] += db

	def usa(self, entrada):
		soma = entrada[0] * self.pesos[0] + entrada[1] * self.pesos[1] + self.pesos[2]
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



# Criando o neurônio 1
n1 = neuronio_hebb()

# Ensinando a função AND ao neurônio 1
n1.aprende(funcao_and)

# Verificando o aprendizado do neurônio 1
print("Verificando o aprendizado da função AND")
entrada = [1,1]
saida = n1.usa(entrada)
print(f'Entrada  1,  1: "{saida:2}"')

entrada = [1,-1]
saida = n1.usa(entrada)
print(f'Entrada  1, -1: "{saida:2}"')

entrada = [-1,1]
saida = n1.usa(entrada)
print(f'Entrada -1,  1: "{saida:2}"')

entrada = [-1,-1]
saida = n1.usa(entrada)
print(f'Entrada -1, -1: "{saida:2}"')



# Criando o neurônio 2
n2 = neuronio_hebb()

# Ensinando a função OR ao neurônio 2
n2.aprende(funcao_or)

# Verificando o aprendizado do neurônio 2
print("Verificando o aprendizado da função OR")
entrada = [1,1]
saida = n2.usa(entrada)
print(f'Entrada  1,  1: "{saida:2}"')

entrada = [1,-1]
saida = n2.usa(entrada)
print(f'Entrada  1, -1: "{saida:2}"')

entrada = [-1,1]
saida = n2.usa(entrada)
print(f'Entrada -1,  1: "{saida:2}"')

entrada = [-1,-1]
saida = n2.usa(entrada)
print(f'Entrada -1, -1: "{saida:2}"')