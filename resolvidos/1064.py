positivo = 0
media = 0
for i in range(0, 6):
    n = float(input())
    if n > 0:
        positivo += 1
        media = media + n
print("{} valores positivos".format(positivo))
print("{:.1f}".format(media/positivo))