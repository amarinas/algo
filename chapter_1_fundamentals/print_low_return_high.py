# given an array of numbers
# print the lowest value in the array
#return the highest value in the array

def print_low_return_high(arr):
    low = arr[0]
    high = arr[0]
    for i in range(len(arr)):
        if arr[i] < low:
            low = arr[i]
        if arr[i] > high:
            high = arr[i]
    print "the lowest number is(print) ", low
    return "the highest number is (return)", high,



print_low_return_high([3,5,6,3,6,8,88,55])
print(print_low_return_high([3,5,6,3,6,8,88,55]))
