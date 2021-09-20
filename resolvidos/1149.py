entrada = list(map(int, input().split()))
A = entrada[0]
cont = 0
soma = 0
for i in entrada:
    cont += 1
    if i > 0 and cont > 0:
        N = i
for i in range(A, A+N):
    soma = soma + i
print(soma)
