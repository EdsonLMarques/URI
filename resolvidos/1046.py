hora_inicial, hora_final = map(int, input().split())

if hora_final < hora_inicial:
    duracao = 24 - hora_inicial + hora_final
elif hora_inicial == hora_final:
    duracao = 24
else:
    duracao = hora_final-hora_inicial

print("O JOGO DUROU {} HORA(S)".format(duracao))