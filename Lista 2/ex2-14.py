import math

class Circulo:
	raio = 0.0

	def __init__(self, raio = 0):
		self.raio = raio

	def calcularArea(self):
		return math.pi * self.raio ** 2

	def calcularPerimetro(self):
		return 2 * math.pi * self.raio



r1 = int(input("Entre com o raio do 1° círculo: "))
c1 = Circulo(r1)

r2 = int(input("Entre com o raio do 2° círculo: "))
c2 = Circulo(r2)

r3 = int(input("Entre com o raio do 3° círculo: "))
c3 = Circulo(r3)


print("A área e o Perímetro do Círculo 1 são respectivamente %2.2f e %2.2f"%(c1.calcularArea(), c1.calcularPerimetro()))
print("A área e o Perímetro do Círculo 2 são respectivamente %2.2f e %2.2f"%(c2.calcularArea(), c2.calcularPerimetro()))
print("A área e o Perímetro do Círculo 3 são respectivamente %2.2f e %2.2f"%(c3.calcularArea(), c3.calcularPerimetro()))