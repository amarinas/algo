# Write a program that would print the sum of all the odd numbers from 1 to 5000

def print_Sum():
    sum = 0
    for i in range(1, 5000):
        if i % 2 == 1:
            sum += i
    return sum


print(print_Sum())
