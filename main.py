I = 0
J = 1
extra = 0
J_anterior = J + 3
while I <= 2:
    print("I={} J={}".format(I, J + extra))
    J = J + 1
    if J == 4:
        I = I + 0.2
        J = 1
        extra += 0.2
        if extra >= 1:
            extra = 0