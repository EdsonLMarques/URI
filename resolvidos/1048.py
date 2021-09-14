salario_inicial = float(input())

if 0 <= salario_inicial <= 400:
    novo_salario = salario_inicial * 1.15
    aumento = novo_salario - salario_inicial
    percentual = 15
elif 400 > salario_inicial <= 800:
    novo_salario = salario_inicial * 1.12
    aumento = novo_salario - salario_inicial
    percentual = 12
elif 800 < salario_inicial <= 1200:
    novo_salario = salario_inicial * 1.10
    aumento = novo_salario - salario_inicial
    percentual = 10
elif 1200 < salario_inicial <= 2000:
    novo_salario = salario_inicial * 1.07
    aumento = novo_salario - salario_inicial
    percentual = 7
else:
    novo_salario = salario_inicial * 1.04
    aumento = novo_salario - salario_inicial
    percentual = 4

print("Novo salario: {:.2f}".format(novo_salario))
print("Reajuste ganho: {:.2f}".format(aumento))
print("Em percentual: {} %".format(percentual))
