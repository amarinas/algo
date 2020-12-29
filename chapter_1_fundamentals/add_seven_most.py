#given an array
# retrun a new array will all values exept first
# adding 7 to each
# do not alter
# def add_seven_most(arr):
#     newarr = []
#     for i in range(1,len(arr)):
#         newarr.append(arr[i]+ 7)
#     return newarr
num = [3,44,5,6,4,3,4,33]
newArr = [num[i] + 7 for i in range(1,len(num))]

# print(add_seven_most([3,44,5,6,4,3,4,33]))


print newArr
