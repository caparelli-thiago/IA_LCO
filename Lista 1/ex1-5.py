x = float(input("Entre com o número 'X': "))
a = float(input("Entre com o número 'A': "))
b = float(input("Entre com o número 'B': "))

if x > a and x < b:
	print(f"O valor {x} está entre {a} e {b}.")
else:
	print(f"O valor {x} não está entre {a} e {b}.")