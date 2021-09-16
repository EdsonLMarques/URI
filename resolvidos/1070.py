x = int(input())
y = int(input())
soma = 0

if x > y:
    for n in range(y, x):
        if n % 2 != 0:
            soma = soma + n
            print(n)
else:
    for n in range(x, y):
        if n % 2 != 0:
            soma = soma + n
print(soma)