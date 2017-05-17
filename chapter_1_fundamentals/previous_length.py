# pass an array containing strings
# working with the same array
# replace each string with a number
# the length of the string at previous array index
# return the array

def previous_length(arr):
    for i in range(len(arr)):
        if isinstance(arr[i], str):
            arr[i] = 9
            # print arr[i]
    return arr


print(previous_length([1,43,5,76,5, "toto", "make cake"]))
