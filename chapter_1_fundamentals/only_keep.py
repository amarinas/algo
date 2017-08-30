# only keep the last few
# given and arr and x, x as last x element and return arr
def only_keep(arr, x):
    if len(arr) > x:
        for i in range len(arr):
            arr[i] = arr[len(arr) - x + i]
            print i

        return arr
    else:
        return 0

print(only_keep([2,4,6,8,10], 3))

print(only_keep([], 3))
