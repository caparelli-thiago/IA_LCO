class arvore:
	valor = None
	altura = None
	filhos = None

	def __init__(self, valor = 0, altura = 0, filhos = None):
		self.valor = valor
		self.altura = altura
		self.filhos = []
		return

	def geraArvore(self):
		if self.altura >= 2:
			self.valor = int(input("Entre com uma nota para o nó: "))
			return

		else:
			valor_filhos = []
			for idx in range(3):
				novoFilho = arvore()
				novoFilho.altura = self.altura + 1
				novoFilho.geraArvore()
				self.filhos.append(novoFilho)
				valor_filhos.append(novoFilho.valor)
			self.valor = max(valor_filhos)
			return


	def exibe(self):
		if self.altura < 2:
			for idx in range(3):
				self.filhos[idx].exibe()
		print("%d  %d"%(self.altura,self.valor))
		return

g = arvore()
g.geraArvore()
g.exibe()
