class Funcionario:
	nome = ""
	horas_trab = 0.0
	valor_hora = 0.0

	def calcularSalario(self):
		return self.horas_trab * self.valor_hora
