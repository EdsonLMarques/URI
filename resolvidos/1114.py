acertou = False
while not(acertou):
    senha = input()
    if senha == "2002":
        acertou = True
        print("Acesso Permitido")
    else:
        print("Senha Invalida")