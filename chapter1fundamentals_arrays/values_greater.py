# values greater than second
# for [1,3,5,7,9,13] print the values that are greater than its 2nd values
# return how many values this is

def value_greater(arr):
    newarr = []
    count = 0
    for i in arr:
        if arr[1] < i:
            newarr.append(i)
            count = count + 1
    return "values that are greater than its 2nd are ", newarr, "the amount of value greater than is ", count


print(value_greater([1,3,5,7,9,13]))
