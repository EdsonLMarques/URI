X = int(input())
Y = int(input())
if X >= Y:
    menor = Y
    maior = X
else:
    menor = X
    maior = Y
for i in range(menor+1, maior):
    if i % 5 == 2 or i % 5 == 3:
        print(i)

