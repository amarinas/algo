# Write a factorial function that takes a positive integer, N as a parameter and prints the result of N!  (N factorial).


def factorial(num):
    return 1 if num ==1 else factorial(num - 1)* num

print(factorial(int(raw_input())))
