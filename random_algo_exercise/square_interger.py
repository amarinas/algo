# An Interger S is a whole square if it is a square of some interger B. Write a function that returns the number of whole squares within the interval[A..B]
# Assume B>=A

import math

def solution(A,B):
    a= int(math.ceil(math.sqrt(abs(A))))
    b= int(math.floor(math.sqrt(abs(B))))
    return b-a + 1



a= 4
b= 17

print solution(a, b)
