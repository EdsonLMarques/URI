A = int(input())
B = int(input())
soma = 0
if A >= B:
    menor = B
    maior = A
else:
    menor = A
    maior = B
for i in range(menor, maior+1):
    if i % 13 != 0:
        soma = soma + i
print(soma)