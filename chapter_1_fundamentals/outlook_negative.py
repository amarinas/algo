# given an array
# create and return a new containing all values of the provided array
#made negative(not simply multiplied by-1)
# given [1,-3,5] = [-1,-3,-5]
def outlook_negative(arr):
    newarr = []
    for i in arr:
        if i > 0:
            i = i * -1
            newarr.append(i)
        else:
            newarr.append(i)
    return newarr

print(outlook_negative([1,-3,5]))
