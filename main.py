N = int(input())
lista = list(range(1, N*4+1))
lista_2 = []
for i in lista:
    if i % 4 == 0:
        i = 'PUM'
        print(i,end= "\n")
    else:
        print(i,end= " ")