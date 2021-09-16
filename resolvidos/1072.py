N = int(input())
dentro = 0
fora = 0
for i in range(0, N):
    X = int(input())
    if 10 <= X <= 20:
        dentro += 1
    else:
        fora += 1
print("{} in\n{} out".format(dentro, fora))