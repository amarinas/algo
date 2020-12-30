# given an array
# create a function to retrun a new array
# double its value
# do not change orginal array

# def double_vision(arr):
#     newarr = []
#     for i in arr:
#         newarr.append(i+i)
#     return newarr


array =[2,4,5,6]
# print(double_vision(array)) #newarr
print array # original
newarr =[array[i]*2 for i in range(len(array))]

print newarr
