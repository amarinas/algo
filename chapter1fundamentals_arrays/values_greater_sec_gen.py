#function that accept any array
#return a new array with values taht are greater than its 2nd values
#what will you do if array is only on element long

def value_greater(arr):
    newarr = []
    count = 0
    for i in arr:
        if len(arr) == 1:
            return "need more than one in an array"
        if arr[1] < i:
            newarr.append(i)
            count = count + 1
    return "values that are greater than its 2nd are ", newarr, "the amount of value greater than is ", count


print(value_greater([1,3,5,7,9,13]))
print(value_greater([1]))
