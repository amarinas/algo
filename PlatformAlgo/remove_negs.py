
# Given an array of multiple values (e.g. [0, -1, 2, -3, 4, -5, 6]), write a program that removes any negative values in that array.  Once your program is done, the array should be composed of only the non-negative numbers, in their original order.  Do this without creating a temporary array; only use the pop() method to remove values from the array.

def remove_negs(arr):
    num_neg=0
    for i in range(len(arr)):
        if arr[i] < 0:
            num_neg += 1
        else:
            arr[i - num_neg] = arr[i]

    while num_neg == True:
        arr.pop()

    return arr


print(remove_negs([0, -1, 2, -3, 4, -5, 6]))
