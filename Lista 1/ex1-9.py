count = 1
qtd = 0
while count <= 10:
	if float(input(f"Entre com o {count}o número: ")) < 0:
		qtd += 1
	count += 1
print(f"Foram inseridos {qtd} números negativos.")