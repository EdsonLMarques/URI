N = int(input())
coelhos = 0
ratos = 0
sapos = 0
for i in range(0, N):
    entrada = input().split()
    if entrada[1] == "C":
        coelhos = coelhos + int(entrada[0])
    elif entrada[1] == "R":
        ratos = ratos + int(entrada[0])
    else:
        sapos = sapos + int(entrada[0])
total = coelhos + ratos + sapos
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelhos))
print("Total de ratos: {}".format(ratos))
print("Total de sapos: {}".format(sapos))
print("Percentual de coelhos: {:.2f} %".format((coelhos/total)*100))
print("Percentual de ratos: {:.2f} %".format((ratos/total)*100))
print("Percentual de sapos: {:.2f} %".format((sapos/total)*100))