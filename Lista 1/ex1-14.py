listnum = []
for x in range(1,6):
	listnum.append(int(input(f"Entre com o {x}o número: ")))
for num in listnum:
	if num < 0:
		print(num)
