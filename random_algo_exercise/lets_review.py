
# Given a string, S , of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).
from __future__ import print_function
import sys



N = int(raw_input())

for i in range(0, N):
    string = raw_input()
    for j in range(0, len(string)):
        if j % 2 == 0:
            print(string[j], end='')
    print(" ", end='')

    for j in range(0, len(string)):
        if j % 2 == 1:
            print(string[j], end='')

    print("")
