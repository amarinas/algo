n=int(input("Enter any number: "))
# a=list(map(int,str(n)))
# b=list(map(lambda x:x**3,a))
# if(sum(b)==n):
#     print("The number is an armstrong number. ")
# else:
#     print("The number isn't an arsmtrong number. ")

s =0
temp =n
while temp > 0:
    c = temp %10
    s += c**3
    temp //= 10
if n ==s:
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")
