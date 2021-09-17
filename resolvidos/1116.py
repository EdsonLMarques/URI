N = int(input())
for i in range(0, N):
    X, Y = map(int, input().split())
    if Y == 0:
        print("divisao impossivel")
    else:
        R = X / Y
        print("{:.1f}".format(R))