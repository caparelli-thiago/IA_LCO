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
		return "%s, mínimo de %2.2f unidades em estoque, %2.2f armazenadas no momento."%(self.nome, self.qtdMinima, self.qtdAtual)

	def precisaRepor(self):
		if self.qtdAtual > self.qtdMinima:
			return False
		else:
			return True

estoque1 = Estoque("Impressora Jato de Tinta",13,6)
estoque2 = Estoque("Monitor LCD 17 polegadas",11,13)
estoque3 = Estoque("Mouse Ótico",6,2)

estoque1.darBaixa(5)
estoque2.reporEstoque(7)
estoque3.darBaixa(4)

print("Precisa repor o estoque 1? ",estoque1.precisaRepor())
print("Precisa repor o estoque 2? ",estoque2.precisaRepor())
print("Precisa repor o estoque 3? ",estoque3.precisaRepor())

print(estoque1.descricao())
print(estoque2.descricao())
print(estoque3.descricao())