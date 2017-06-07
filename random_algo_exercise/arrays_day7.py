# Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
from __future__ import print_function
import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arr.reverse()
for num in arr:
    print(num + " ", end='')
