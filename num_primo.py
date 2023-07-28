print(30 * "-")

numero = int(input("Insira um numero para ver se ele é primo: "))

if numero > 1:
    for x in range(2, numero):
        if(numero % x) == 0:
            print("Esse não é um número primo")
            break
    else:
        print("Esse número é primo")
else:
    print('Esse número não é primo: num menor ou igual')

print(30 * "-")

