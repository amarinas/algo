#given an array
# create a function that changes all positive number in the array to "big"
#makeitbig([-1,2,5,-3,2,-7])
# def makeItBig(arr):
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             arr[i] = "big"
#     return arr
#
#
# print(makeItBig([-1,2,5,-3,2,-7]))
arr = [-1,2,5,-3,2,-7]

newArr = ["big" if arr[i] > 0  else arr[i] for i in range(len(arr)) ]

print newArr
