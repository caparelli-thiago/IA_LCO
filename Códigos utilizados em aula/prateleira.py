class prateleira:
	idCorredor = None
	idLado = None
	lproduto = None

	def __init__(self, corredor = 0, lado = True, produto = None):
		self.idCorredor = corredor
		self.idLado = lado
		if produto is None:
			self.lproduto = []
		else:
			self.lproduto = produto


	def mudaCorredor(self, corredor):
		self.idCorredor = corredor


	def mudaLado(self, lado):
		self.idLado = lado


	def exibeProdutos(self):
		if self.idLado:
			print("A prateleira está no lado direito do corredor %d"%(self.idCorredor))
		else:
			print("A prateleira está no lado esquerdo do corredor %d"%(self.idCorredor))
		if len(self.lproduto) == 0:
			print("A prateleira está vazia.")
		elif len(self.lproduto) == 1:
			print("A prateleira contém apenas %s."%(self.lproduto[0]))
		else:
			print("A prateleira contém os seguintes produtos: ")
			for item in self.lproduto:
				print(" - %s"%(item))


	def insereProduto(self, produto):
		if (produto in self.lproduto):
			print("Produto já está na prateleira.")
		else:
			self.lproduto.append(produto)
			print("%s inserido na prateleira."%(produto))


	def removeProduto(self, produto):
		if not (produto in self.lproduto):
			print("Não há %s na prateleira."%(produto))
		else:
			self.lproduto.remove(produto)
			print("%s foi removido da prateleira."%(produto))