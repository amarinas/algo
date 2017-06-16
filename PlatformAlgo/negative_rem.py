#Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that replaces any negative number with the value of 0.  When the program is done x should have no negative values (e.g. [1, 5, 10, 0]).


def remove_Negative(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    return arr


print(remove_Negative([1, 5, 10, 0, -2, -3]))
