class Estoque:
	nome = ""
	qtdAtual = 0
	qtdMinima = 0

	def __init__(self, nome = "", qtdAtual = 0, qtdMinima = 0):
		self.nome = nome
		self.qtdAtual = qtdAtual
		self.qtdMinima = qtdMinima

	def reporEstoque(self, qtd):
		self.qtdAtual += qtd

	def darBaixa(self, qtd):
		if (self.qtdAtual - qtd) >= 0:
			self.qtdAtual -= qtd
		else:
			print("Quantidade de itens em estoque insuficiente.")

	def descricao(self):
		print("%s, mínimo de %2.2f unidades em estoque, %2.2f armazenadas no momento."%(self.nome, self.qtdMinima, self.qtdAtual))

	def precisaRepor(self):
		if self.qtdAtual <= self.qtdMinima:
			return True
		else:
			return False
