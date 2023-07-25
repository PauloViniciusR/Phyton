escolha = input("Escolha um número entre 1 e 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)

else:
    def func2(x):
        return x / 2
    s = func2(50)

print(s)
