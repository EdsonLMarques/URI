# Sum of Consecutive Odd Numbers II
# Adapted by Neilor Tonin, URI  Brazil
#
# Timelimit: 1
# Read an integer N that is the number of test cases. Each test case is a line containing two integer numbers X and Y. Print the sum of all odd values between them, not including X and Y.
#
# Input
# The first line of input is an integer N that is the number of test cases that follow. Each test case is a line containing two integer X and Y.
#
# Output
# Print the sum of all odd numbers between X and Y
#
#Solução Por Edson Marques

N = int(input())
SOMA = 0
for i in range(0, N):
    A, B = map(int, input().split())
    if(A <= B):
        for x in range(A+1, B):
            if x % 2 != 0:
                SOMA += x
    else:
        for x in range(B+1, A):
            if x % 2 != 0:
                SOMA += x
    print(SOMA)
    SOMA = 0
