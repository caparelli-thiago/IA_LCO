class Funcionario:
	nome = ""
	horas_trab = 0.0
	valor_hora = 0.0

	def calcularSalario(self):
		return self.horas_trab * self.valor_hora

f1 = Funcionario()
f1.nome = "João"
f1.horas_trab = 20
f1.valor_hora = 3.5

f2 = Funcionario()
f2.nome = "Mateus"
f2.horas_trab = 40
f2.valor_hora = 5.5

f3 = Funcionario()
f3.nome = "Lucas"
f3.horas_trab = 40
f3.valor_hora = 13.5

print("O %s recebeu R$%2.2f de salário."%(f1.nome,f1.calcularSalario()))
print("O %s recebeu R$%2.2f de salário."%(f2.nome,f2.calcularSalario()))
print("O %s recebeu R$%2.2f de salário."%(f3.nome,f3.calcularSalario()))