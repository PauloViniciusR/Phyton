media = 10.0

if media >= 7.0:
    situacao = "Aprovado"
elif media > 5.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

    print(f'O estudante esta: {situacao}')