class Funcionario:
	nome = ""
	horas_trab = 0.0
	valor_hora = 0.0

	def calcularSalario(self):
		return self.horas_trab * self.valor_hora

f1 = Funcionario()
f1.nome = input("Entre com o nome do 1° funcionário: ")
f1.horas_trab = float(input("Entre com a quantidade de horas que %s trabalhou: "%f1.nome))
f1.valor_hora = float(input("Entre com o valor da hora trabalhada: "))

f2 = Funcionario()
f2.nome = input("Entre com o nome do 2° funcionário: ")
f2.horas_trab = float(input("Entre com a quantidade de horas que %s trabalhou: "%f2.nome))
f2.valor_hora = float(input("Entre com o valor da hora trabalhada: "))

f3 = Funcionario()
f3.nome = input("Entre com o nome do 3° funcionário: ")
f3.horas_trab = float(input("Entre com a quantidade de horas que %s trabalhou: "%f3.nome))
f3.valor_hora = float(input("Entre com o valor da hora trabalhada: "))

print("%s recebeu R$%2.2f de salário."%(f1.nome,f1.calcularSalario()))
print("%s recebeu R$%2.2f de salário."%(f2.nome,f2.calcularSalario()))
print("%s recebeu R$%2.2f de salário."%(f3.nome,f3.calcularSalario()))