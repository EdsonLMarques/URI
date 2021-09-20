operacao = []
acertou = ["inicio"]
errou = ["inicio"]
while True:
  try:
      operacao = []
      acertou = ["inicio"]
      errou = ["inicio"]
      while len(acertou) != 0:
          T = int(input())
          acertou.clear()
          errou.clear()
          operacao.clear()
          for i in range(0, T):
              operacao.append(input().replace('=', ' ').split())
          for i in range(0, T):
              resposta = input().split()
              operacao_aberta = operacao[int(resposta[1]) - 1]
              if resposta[2] == "+":
                  if int(operacao_aberta[0]) + int(operacao_aberta[1]) == int(operacao_aberta[2]):
                      acertou.append(resposta[0])
                  else:
                      errou.append(resposta[0])
              elif resposta[2] == "-":
                  if int(operacao_aberta[0]) - int(operacao_aberta[1]) == int(operacao_aberta[2]):
                      acertou.append(resposta[0])
                  else:
                      errou.append(resposta[0])
              elif resposta[2] == "*":
                  if int(operacao_aberta[0]) * int(operacao_aberta[1]) == int(operacao_aberta[2]):
                      acertou.append(resposta[0])
                  else:
                      errou.append(resposta[0])
              elif resposta[2] == "I":
                  if (int(operacao_aberta[0]) + int(operacao_aberta[1]) != int(operacao_aberta[2])) and \
                          (int(operacao_aberta[0]) - int(operacao_aberta[1]) != int(operacao_aberta[2])) and \
                          (int(operacao_aberta[0]) * int(operacao_aberta[1]) != int(operacao_aberta[2])):
                      acertou.append(resposta[0])
                  else:
                      errou.append(resposta[0])
          var_aux = ""
          if len(acertou) == T:
              print("You Shall All Pass!")
          elif len(acertou) != 0:
              errou.sort()
              for i in errou:
                  var_aux = var_aux + i + " "
              print(var_aux.strip())
      print("None Shall Pass!")
  except EOFError:
    break