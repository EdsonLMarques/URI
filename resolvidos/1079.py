N = int(input())
for i in range(0, N):
    A, B, C = map(float, input().split())
    media = (A*2 + B*3 + C*5)/10
    print("{:.1f}".format(media))