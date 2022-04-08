def conv_bin(numero):
	if int(numero / 2) == 0:
		return str(numero%2)
	else:
		return conv_bin(int(numero/2)) + str(numero%2)


num = int(input("Entre com o número: "))
print("%d em binário é representado por %s"%(num,conv_bin(num)))
