def taximetro(distancia, multiplicador=2):
    largada = 5
    km_rodado = 5

    valor = (distancia + largada * km_rodado) * multiplicador
    return valor


pagamento = taximetro(3.5)
print(pagamento)
