x = 5  # variavel global


def funcao():
    x = 3  # variavel local
    print("Valor da variavel local: ", x)


funcao()
print("Valor da variavel global: ", x)
