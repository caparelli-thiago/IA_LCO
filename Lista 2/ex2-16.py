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

n = input("Entre com o nome do 1° funcionário: ")
h = float(input("Entre com a quantidade de horas que %s trabalhou: "%(n)))
v = float(input("Entre com o valor da hora trabalhada: "))
f1 = Funcionario(n,h,v)

n = input("Entre com o nome do 2° funcionário: ")
h = float(input("Entre com a quantidade de horas que %s trabalhou: "%(n)))
v = float(input("Entre com o valor da hora trabalhada: "))
f2 = Funcionario(n,h,v)

n = input("Entre com o nome do 3° funcionário: ")
h = float(input("Entre com a quantidade de horas que %s trabalhou: "%(n)))
v = float(input("Entre com o valor da hora trabalhada: "))
f3 = Funcionario(n,h,v)

print("%s recebeu R$%2.2f de salário."%(f1.nome,f1.calcularSalario()))
print("%s recebeu R$%2.2f de salário."%(f2.nome,f2.calcularSalario()))
print("%s recebeu R$%2.2f de salário."%(f3.nome,f3.calcularSalario()))