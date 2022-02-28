class Funcionario:
	nome = ""
	horas_trab = 0.0
	valor_hora = 0.0

	def __init__(self, nome = "", horas_trab = 0, valor_hora = 0):
		self.nome = nome
		self.horas_trab = horas_trab
		self.valor_hora = valor_hora

	def calcularSalario(self):
		return self.horas_trab * self.valor_hora
