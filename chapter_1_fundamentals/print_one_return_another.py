# build a function that takes array of numbers
# the function should print second to last value
# and return first odd value in the array
def print_one_return_another(arr):
    first_odd = []
    print "the second to the last value is(as print) ", arr[-2]
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            first_odd.append(arr[i])

    return first_odd[0]


print_one_return_another([2,4,5,3,56,7,6,4,2,99,32])
print(print_one_return_another([2,4,5,3,56,7,6,4,2,44,32]))
