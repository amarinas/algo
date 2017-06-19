# fibbanachi recursion
# base case:
# if fib 0, return 0
# if fib 1, return 1
# fib(2) = fib(0) +fib(1) = 1
# fib(3) = fib(1) + fib(2) = 2
# [0,1,1,2,3,5,8,13......]

def fib(n):
    print "the current", n
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)



print(fib(2))
