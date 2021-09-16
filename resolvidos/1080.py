X = 0
maior = 0
for i in range(0, 100):
    X = int(input())
    if X > maior:
        maior = X
        posicao = i + 1

print(maior)
print(posicao)