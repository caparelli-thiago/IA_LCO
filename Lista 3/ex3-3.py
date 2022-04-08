def pa(base, razao, elemento):
	return base + (razao * (elemento - 1))


num = int(input("Entre com a base: "))
raz = int(input("Entre com a razão: "))

for index in range(1,11):
	print(pa(num,raz,index))
