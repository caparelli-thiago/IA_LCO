# exemplo de recursão - cálculo do fatorial


# sem passagem de parâmetros (não usa valores auxiliares)
def fatorial1(num):
        if num == 1:
                return 1
        else:
                return num * fatorial1(num-1)

# com passagem de parâmetros (usa valores auxiliares - cálculo parcial a cada chamada)
def fatorial2(num, parcial = 1):
        if num == 1:
                return parcial
        else:
                return fatorial2(num-1,parcial * num)


meu_num = int(input("Entre com um número: "))
print("O fatorial de %d calculado pela função sem parâmetros é: %d"%(meu_num,fatorial1(meu_num)))
print("O fatorial de %d calculado pela função com parâmetros é: %d"%(meu_num,fatorial2(meu_num)))