import math

def digit_sum(x):
  string_x = str(x)
  total = 0
  for char in string_x:
    total += int(char)
  return total



digit_sum("2thewahy34")
