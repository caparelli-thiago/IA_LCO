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

f1 = Funcionario("João",20,3.5)
f2 = Funcionario("Mateus",40,5.5)
f3 = Funcionario("Lucas",40,13.5)

print("%s recebeu R$%2.2f de salário."%(f1.nome,f1.calcularSalario()))
print("%s recebeu R$%2.2f de salário."%(f2.nome,f2.calcularSalario()))
print("%s recebeu R$%2.2f de salário."%(f3.nome,f3.calcularSalario()))