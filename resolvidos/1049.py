palavra_1 = input()
palavra_2 = input()
palavra_3 = input()

if palavra_1 == "vertebrado" and palavra_2 == "ave" and palavra_3 == "carnivoro":
    resposta = "aguia"
elif palavra_1 == "vertebrado" and palavra_2 == "ave" and palavra_3 == "onivoro":
    resposta = "pomba"
elif palavra_1 == "vertebrado" and palavra_2 == "mamifero" and palavra_3 == "onivoro":
    resposta = "homem"
elif palavra_1 == "vertebrado" and palavra_2 == "mamifero" and palavra_3 == "herbivoro":
    resposta = "vaca"
elif palavra_1 == "invertebrado" and palavra_2 == "inseto" and palavra_3 == "hematofago":
    resposta = "pulga"
elif palavra_1 == "invertebrado" and palavra_2 == "inseto" and palavra_3 == "herbivoro":
    resposta = "lagarta"
elif palavra_1 == "invertebrado" and palavra_2 == "anelideo" and palavra_3 == "hematofago":
    resposta = "sanguessuga"
elif palavra_1 == "invertebrado" and palavra_2 == "anelideo" and palavra_3 == "onivoro":
    resposta = "minhoca"

print(resposta)