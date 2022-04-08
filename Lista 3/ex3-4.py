def somalista(lista):
	if len(lista) == 0:
		return 0
	else:
		return lista.pop() + somalista(lista)

minhalista = []
for index in range(5):
	minhalista.append(int(input("Entre com o %do numero: "%(index+1))))
print("A soma dos elementos da lista é: %d"%(somalista(minhalista)))
