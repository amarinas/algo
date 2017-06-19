# Write a Calculator class with a single method: int power(int,int). The power method takes two integers,  and , as parameters and returns the integer result of n ^p. If either n or p is negative, then the method must throw an exception with the message: n and p should be non-negative.


class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        return pow(n, p)

myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e
