numero = int(input("Insira um número: "))

fatorial = 1

if numero < 0:
    print('Não existe fatorial para numeros negativos')

elif numero == 0:
    print(f'O fatorial de {numero} é 1')
else:
    for x in range(1, numero + 1):
        fatorial *= x
    print(f'O fatorial de {numero} é {fatorial}')
