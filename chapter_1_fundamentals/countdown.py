# create a function that accepts a number as an input
# return a new array that counts down by one from the number

# def countdown(arr):
#     newarr = []
#     for i in range(arr, 0, -1):
#         newarr.append(i)
#     return newarr
#
# print(countdown(5))


n = 5
cdown = [x for x in range(n, 0, -1)]
print cdown
