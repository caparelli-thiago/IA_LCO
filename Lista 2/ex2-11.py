import math

class Circulo:
	raio = 0.0

	def __init__(self, raio = 0):
		self.raio = raio

	def calcularArea(self):
		return math.pi * self.raio ** 2

	def calcularPerimetro(self):
		return 2 * math.pi * self.raio