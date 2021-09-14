entrada_1 = input().split()
entrada_2 = input().split()
entrada_3 = input().split()
entrada_4 = input().split()

dia_inicial, dia_final = int(entrada_1[1]), int(entrada_3[1])
hora_inicial, minuto_inicial, segundo_inicial = int(entrada_2[0]), int(entrada_2[2]), int(entrada_2[4])
hora_final, minuto_final, segundo_final = int(entrada_4[0]), int(entrada_4[2]), int(entrada_4[4])

tempo_inicial = dia_inicial*86400 + hora_inicial*3600 + minuto_inicial*60 + segundo_inicial
tempo_final = dia_final*86400 + hora_final*3600 + minuto_final*60 + segundo_final
duracao = tempo_final - tempo_inicial
W = duracao //86400
ws = (duracao % 86400)
X = ws//3600
xs = (ws%3600)
Y = xs//60
Z = xs%60

print("{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)".format(W, X, Y, Z))