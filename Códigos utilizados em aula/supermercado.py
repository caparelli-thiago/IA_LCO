import prateleira    #Busca o código do arquivo "prateleira.py"

def geraCorredor(numCorredor):
	a = prateleira.prateleira(numCorredor,False)
	a.insereProduto(input("Entre com o primeiro produto da prateleira esquerda do corredor %d: "%(numCorredor)))
	a.insereProduto(input("Entre com o segundo produto da prateleira esquerda do corredor %d: "%(numCorredor)))
	b = prateleira.prateleira(numCorredor,True)
	b.insereProduto(input("Entre com o primeiro produto da prateleira direita do corredor %d: "%(numCorredor)))
	b.insereProduto(input("Entre com o segundo produto da prateleira direita do corredor %d: "%(numCorredor)))
	return [[a,b]]

def geraSupermercado(tamanho):
	if tamanho == 1:
		return geraCorredor(1)
	else:
		return geraSupermercado(tamanho - 1) + geraCorredor(tamanho)

s = geraSupermercado(3)
print(s)