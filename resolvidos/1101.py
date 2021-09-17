# Sequence of Numbers and Sum
# Adapted by Neilor Tonin, URI  Brazil
#
# Timelimit: 1
# Read an undetermined number of pairs values M and N (stop when any of these values is less or equal to zero). For each pair, print the sequence from the smallest to the biggest (including both) and the sum of consecutive integers between them (including both).
#
# Input
# The input file contains pairs of integer values M and N. The last line of the file contains a number zero or negative, or both.
#
# Output
# For each pair of numbers, print the sequence from the smallest to the biggest and the sum of these values, as shown below.
#
#Solução por: Edson Marques

M, N = map(int, input().split())
SOMA = 0
while not(M <= 0) and not(N <= 0):
    if M <= N:
        for i in range(M, N+1):
            print(i,end = " ")
            SOMA += i
    else:
        for i in range(N, M + 1):
            print(i,end = " ")
            SOMA += i
    print("Sum={}".format(SOMA))
    SOMA = 0
    M, N = map(int, input().split())