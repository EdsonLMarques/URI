# Ascending and Descending
# Adapted by Neilor Tonin, URI  Brazil
#
# Timelimit: 1
# Read an undetermined number of pairs of integer values. Write a message for each pair indicating if this two numbers are in ascending or descending order.
#
# Input
# The input file contains several test cases. Each test case contains two integer numbers X and Y. The input will finished when X = Y.
#
# Output
# For each test case print “Crescente”, if the values X and Y are in ascending order, otherwise print “Decrescente”.
#
#Solução por: Edson Marques

X, Y = map(int, input().split())
while X != Y:
    if X > Y:
        print("Decrescente")
    elif X < Y:
        print("Crescente")
    X, Y = map(int, input().split())