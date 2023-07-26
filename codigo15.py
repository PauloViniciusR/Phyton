def taximetro(distancia):
    def calcMult():
        if distancia < 5:
            return 1.2
        else:
            return 1
        
    multiplicador = calcMult()
    largada = 2
    km_rodado = 3
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor

dist = eval(input('Insira o KM a ser percorrido: \n'))
pagamento = taximetro(dist)
print(f'O valor percorrido será de R${pagamento}')