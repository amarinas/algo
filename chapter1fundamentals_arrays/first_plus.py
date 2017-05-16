#given an array
#return the sum of the first value in the array
#also the arrays length
#do a check for a string

def first_plus(arr):
    sum = 0
    length = len(arr)
    for i in arr:
        if isinstance(i, str):
            return "only digits in this array"
        else:
            sum = sum + i
    return "the sum is ", sum, "the length is ", length

    print "length of the array is ", length


print(first_plus([2,4,5,7,7,5,3,24,66]))
print(first_plus(["what?",4,5,7,7,5,3,24,66]))
