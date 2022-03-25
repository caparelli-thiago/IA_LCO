def fatorial(numero):
    if numero ==1:
        return 1
    else:
        return numero * fatorial(numero-1)

num = int(input("Entre com o numero: "))
if num > 0:
    if num < 20:
        print("O fatorial de %d é: %d"%(num,fatorial(num)))
    else:
        print("O numero deve ser maior que zero e menor que 20.")
else:
    print("O numero deve ser maior que zero e menor que 20.")