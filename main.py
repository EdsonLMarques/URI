lista = input().split()
pontos = [float(i) for i in lista]
pontos.sort(reverse=True)

A = pontos[0]
B = pontos[1]
C = pontos[2]

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
elif A**2 == (B**2 + C**2):
    print("TRIANGULO RETANGULO")
elif A ** 2 > (B ** 2 + C ** 2):
    print("TRIANGULO OBTUSANGULO")
elif A ** 2 < (B ** 2 + C ** 2):
    print("TRIANGULO ACUTANGULO")
if A == B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or A == C or B == C:
    print("TRIANGULO ISOSCELES")