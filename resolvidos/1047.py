hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

tempo_inicial = 60*hora_inicial + minuto_inicial
tempo_final = 60*hora_final + minuto_final

if tempo_final < tempo_inicial:
    duracao = 24*60 - tempo_inicial + tempo_final
elif tempo_inicial == tempo_final:
    duracao = 24*60
else:
    duracao = tempo_final-tempo_inicial

duracao_hora = duracao//60
duracao_minuto = duracao%60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao_hora, duracao_minuto))