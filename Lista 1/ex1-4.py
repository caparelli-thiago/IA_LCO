n1 = float(input("Entre com o primeiro número: "))
n2 = float(input("Entre com o segundo número: "))
n3 = float(input("Entre com o terceiro número: "))
n4 = float(input("Entre com o quarto número: "))
media = (n1+n2+n3+n4)/4
if media >=6:
	status = "aprovado"
else:
	status = "reprovado"
print("A média dos números é:",(media),status)