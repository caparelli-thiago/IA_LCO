class Paciente:
	nome = ""
	peso = 0.0
	altura = 0.0

	def calcularIMC(self):
		return self.peso / (self.altura ** 2)
