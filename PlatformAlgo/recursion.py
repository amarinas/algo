# def rsum(num):
#     if num == 1:
#         return 1
#     else:
#         return num + rsum(num - 1)
#
#
#
# print(rsum(5))

def isum(num):
    sum = 0
    for i in range(num +1):
        sum = sum + i
    return sum



print(isum(5))
