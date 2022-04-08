def pot(base, expoente):
	if expoente == 0:
		return 1
	else:
		return base * pot(base, expoente - 1)

num = int(input("Entre com a base: "))
exp = int(input("Entre com o expoente: "))
print("%d elevado a %d é: %d"%(num,exp,pot(num,exp)))