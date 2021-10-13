3 20 20
google
morosidade
coragem
LjUtSbDvScXhVgVrMkBh
UaOoRvArAuAmWdBcUaLb
QiNcXwIxVcVxUxAdTkJh
AfWeDwVcMfLjQwFhTuBp
MmTxerSbTjWpMcJqMfWk
WdRgMdGwUtWoNmJfRrBw
GtIaGwAaMcThVeOfQdHe
UxOdCdPDDjobGmGqJmSj
GrUsTlGwiaHRGjBoHwEt
PoPsXpGpQSGmauXkNmTa
UrVgWoFwGhOaPGLoSwAt
OaKwDxLuUrSRJiEpHaCb
DbOqOpJwMoCfonXmUmPs
EoLbKjHeTdGgAMJsQsQb
HiEbDqSxEpLiAfMhCwBu
WaIvJdPfHmHmOiUbBdDd
UtFpLbVkLcFhLmAvIkPa
WcGqFrCkBkBeBsUwHwFr
CjCsUjMeIgHkRfCtFgMm
HxThEqQsRxKkPfXgEsUk


def teste(DIAGONAL, palavra):
    diagonal_direta = ''.join(DIAGONAL)
    diagonal_direta = diagonal_direta.capitalize()
    diagonal_reversa = diagonal_direta[::-1]
    if palavra in diagonal_direta or palavra in diagonal_reversa:
        return True
    else:
        return False


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
    resposta = teste(PRINCIPAL, palavra)
    if resposta:
        print("1 Palavra \"{}\" na diagonal principal".format(palavra))
        tem_palavra = True
    PRINCIPAL.clear()

    # acima______________________________________________________
    for i in range(1, M):
        LINHA = 0
        for COLUNA in range(i, M):
            ACIMA.append(matriz[LINHA][COLUNA])
            LINHA += 1
        resposta = teste(ACIMA, palavra)
        if resposta:
            print("2 Palavra \"{}\" acima da diagonal principal".format(palavra))
            tem_palavra = True
        ACIMA.clear()

    # abaixo______________________________________________________
    for i in range(1, M):
        COLUNA = 0
        for LINHA in range(i, P):
            ABAIXO.append(matriz[LINHA][COLUNA])
            COLUNA += 1
        resposta = teste(ABAIXO, palavra)
        if resposta:
            print("3 Palavra \"{}\" abaixo da diagonal principal".format(palavra))
            tem_palavra = True
        ABAIXO.clear()

    if tem_palavra:
        tem_palavra = False
    else:
        tem_palavra = False
        print("4 Palavra \"{}\" inexistente".format(palavra))
