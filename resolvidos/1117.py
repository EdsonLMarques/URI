notas_validas = 0
soma = 0
while notas_validas < 2:
    nota = float(input())
    if 0 <= nota <= 10:
        notas_validas += 1
        soma += nota
    else:
        print("nota invalida")
print("media = {}".format(soma/2))