#Given an array x (e.g. [1,5, 10, 7, -2]), create an algorithm (sets of instructions) that shifts each number by one (to the front).  For example when the program is done x (assuming it was [1,5,10,7,-2]) should become [5,10,7,-2, 0].

def shift_arr(arr):

    for i in range(len(arr)-1):
        arr[i] = arr[i +1]
    arr[len(arr)-1] = 0

    return arr

print(shift_arr([1,5, 10, 7, -2 , 4, 5]))
