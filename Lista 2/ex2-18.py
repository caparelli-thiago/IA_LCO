class Quadrado:
	lado = 0

	def __init__(self, lado = 0):
		self.lado = lado

	def area(self):
		return self.lado ** 2

	def perimetro(self):
		return self.lado * 4

q1 = Quadrado(3)
q2 = Quadrado(4)
q3 = Quadrado(5)

print("A área e o perímetro do 1° quadrado são, respectivamente, %2.2f e %2.2f"%(q1.area(),q1.perimetro()))
print("A área e o perímetro do 2° quadrado são, respectivamente, %2.2f e %2.2f"%(q2.area(),q2.perimetro()))
print("A área e o perímetro do 3° quadrado são, respectivamente, %2.2f e %2.2f"%(q3.area(),q3.perimetro()))
