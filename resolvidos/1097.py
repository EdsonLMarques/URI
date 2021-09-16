I = 1
J = 7
J_inicial = J
while I <= 9:
    print("I={} J={}".format(I, J))
    J -= 1
    if J == J_inicial - 3:
        I += 2
        J = J_inicial + 2
        J_inicial = J