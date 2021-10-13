N, M, P = map(int, input().split())
palavras = []
for i in range(0, N):
    palavras.append(input())
linha = []
matriz = []
for i in range(0, M):
    linhas = input()
    for char in linhas:
        linha.append(char)
    matriz.append(linha[:])
    linha.clear()

PRINCIPAL = []
ACIMA = []
ABAIXO = []
DIAGONAL = []

COLUNA = 0
LINHA = 0
tem_palavra = False
for palavra in palavras:
    palavra.capitalize()

    # diagonal principal______________________________________________________
    for i in range(0, M):
        PRINCIPAL.append(matriz[i][i])
    diagonal_direta = ''.join(PRINCIPAL)
    diagonal_direta = diagonal_direta.capitalize()
    diagonal_reversa = diagonal_direta[::-1]
    if palavra in diagonal_direta or palavra in diagonal_reversa:
        print("1 Palavra \"{}\" na diagonal principal".format(palavra))
        tem_palavra = True
    PRINCIPAL.clear()

    # acima______________________________________________________
    for i in range(1, M):
        LINHA = 0
        for COLUNA in range(i, M):
            ACIMA.append(matriz[LINHA][COLUNA])
            LINHA += 1
        diagonal_direta = ''.join(ACIMA)
        diagonal_direta = diagonal_direta.capitalize()
        diagonal_reversa = diagonal_direta[::-1]
        if palavra in diagonal_direta or palavra in diagonal_reversa:
            print("2 Palavra \"{}\" acima da diagonal principal".format(palavra))
            tem_palavra = True
            break
        ACIMA.clear()

    # abaixo______________________________________________________
    for i in range(1, M):
        COLUNA = 0
        for LINHA in range(i, P):
            ABAIXO.append(matriz[LINHA][COLUNA])
            COLUNA += 1
        diagonal_direta = ''.join(ABAIXO)
        diagonal_direta = diagonal_direta.capitalize()
        diagonal_reversa = diagonal_direta[::-1]
        if palavra in diagonal_direta or palavra in diagonal_reversa:
            print("3 Palavra \"{}\" abaixo da diagonal principal".format(palavra))
            tem_palavra = True
            break
        ABAIXO.clear()

    if tem_palavra:
        tem_palavra = False
    else:
        tem_palavra = False
        print("4 Palavra \"{}\" inexistente".format(palavra))
