import math

class Circulo:
	raio = 0.0

	def calcularArea(self):
		return math.pi * self.raio ** 2

	def calcularPerimetro(self):
		return 2 * math.pi * self.raio
