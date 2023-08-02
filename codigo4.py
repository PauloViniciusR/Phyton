""" nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for nome in nomes:
    print(nome)

lista1 = list(range(10))
print(lista1)

lista2 = list('phyton')
print(lista2)

elemento = 8
if elemento in lista1:
    print("O elemento {} esta dentro da lista".format(elemento))""" 

"""animals = ["gato", "girafa", "elefante", "tubarão", "passaro", "leão"]
print(animals)

animals[1] = 'cachorro'
print(animals)

animals[1:4] = ["agia", "morcego", "tigre"]
print(animals) """

veiculos = ["carro", "barco", "avião"]
print(veiculos)

veiculos.insert(1, "bicicleta")
print(veiculos)

veiculos.extend(["navio", "caminhão"])
print(veiculos)

veiculos.append('moto')
print(veiculos)

#veiculos.pop()
#print(veiculos)

#veiculos.remove("avião")
#print(veiculos)

veiculos.sort()
print(veiculos)

print(len(veiculos))

for x in range(len(veiculos)):
    print(x, veiculos[x])

