import math

class Circulo:
	raio = 0.0

	def calcularArea(self):
		return math.pi * self.raio ** 2

	def calcularPerimetro(self):
		return 2 * math.pi * self.raio

c1 = Circulo()
c1.raio = int(input("Entre com o raio do 1° círculo: "))

c2 = Circulo()
c2.raio = int(input("Entre com o raio do 2° círculo: "))

c3 = Circulo()
c3.raio = int(input("Entre com o raio do 3° círculo: "))


print("A área e o Perímetro do Círculo 1 são respectivamente %2.2f e %2.2f"%(c1.calcularArea(), c1.calcularPerimetro()))
print("A área e o Perímetro do Círculo 2 são respectivamente %2.2f e %2.2f"%(c2.calcularArea(), c2.calcularPerimetro()))
print("A área e o Perímetro do Círculo 3 são respectivamente %2.2f e %2.2f"%(c3.calcularArea(), c3.calcularPerimetro()))