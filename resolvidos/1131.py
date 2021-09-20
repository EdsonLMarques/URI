novo_grenal = True
inter = 0
gremio = 0
empate = 0
grenais = 0
while novo_grenal:
    grenais += 1
    I, G = map(int, input().split())
    if I > G:
        inter += 1
    elif G > I:
        gremio += 1
    else:
        empate += 1
    print("Novo grenal (1-sim 2-nao)")
    if input() == '2':
        novo_grenal = False
    else:
        novo_grenal = True
print("{} grenais".format(grenais))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empate))
if inter > gremio:
    print("Inter venceu mais")
elif inter < gremio:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")