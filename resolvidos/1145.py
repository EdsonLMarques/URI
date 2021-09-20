quantidade, final = map(int, input().split())
i = 1
cont = 1
while i <= final:
    if cont == quantidade:
        print(i)
        cont = 0
    else:
        print(i, end=" ")
    i += 1
    cont += 1