class Quadrado:
	lado = 0

	def __init__(self, lado = 0):
		self.lado = lado

	def area(self):
		return self.lado ** 2

	def perimetro(self):
		return self.lado * 4