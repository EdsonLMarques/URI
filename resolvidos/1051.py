salario = float(input())
imposto_1 = 0
imposto_2 = 0
imposto_3 = 0
if salario <= 2000:
    print("Isento")
else:
    if 4500 < salario:
        imposto_3 = (salario - 4500) * 0.28
        salario = salario - (salario - 4500)
    if 3000 < salario:
        imposto_2 = (salario - 3000) * 0.18
        salario = salario - (salario - 3000)
    if 2000 < salario:
        imposto_1 = (salario - 2000)*0.08
        salario = salario - (salario - 2000)
    imposto = imposto_1 + imposto_2 + imposto_3
    print("R$ {:.2f}".format(imposto))


