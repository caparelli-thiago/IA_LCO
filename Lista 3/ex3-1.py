def fibonacci(index):
	if index == 1:
		return 0
	elif index == 2:
		return 1
	else:
		return fibonacci(index - 1) + fibonacci(index - 2)


num = int(input("Entre com o elemento que deseja calcular: "))
print("O %do elemento da série de fibonacci é: %d"%(num,fibonacci(num)))
