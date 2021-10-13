INPUT = input().split()
A = int(INPUT[0])
B = float(INPUT[1])
C = INPUT[2]
D = ' '.join(INPUT[3:])
print("{}{:.6f}{}{}".format(A, B, C, D))
print("{}\t{:.6f}\t{}\t{}".format(A, B, C, D))
print("{:10}{:10.6f}{:10}{:10}".format(A, B, C, D))
