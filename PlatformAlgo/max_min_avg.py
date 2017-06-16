#Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that prints the maximum number in the array, minimum value in the array as well as the average values in the array.


def max_min_avg(arr):
    max = arr[0]
    min = arr[0]
    sum = 0
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
        if min > arr[i]:
            min = arr[i]

        sum += arr[i]
    return sum / len(arr)


print(max_min_avg([1 ,5, 10, -2, 33]))
