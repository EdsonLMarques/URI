novo_calculo = True
soma = 0
notas_validas = 0
while novo_calculo:
    while notas_validas < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            notas_validas += 1
            soma += nota
        else:
            print("nota invalida")
    print("media = {:.2f}".format(soma / 2))
    soma = 0
    notas_validas = 0
    resposta = 0
    while resposta != 1 and resposta != 2:
        print("novo calculo (1-sim 2-nao)")
        resposta = int(input())
        if resposta == 1:
            novo_calculo = True
        elif resposta == 2:
            novo_calculo = False
        else:
            novo_calculo = 0