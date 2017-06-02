# only keep the last few
# given and arr and x, x as last x element and return arr
def only_keep(arr, x):
    if len(arr) > x:
        for i in range(len(arr)):
            print "this", arr[x -i], arr
            arr[i] = arr[ -x + i]
            print arr[i]
            # arr[i] = arr[len(arr[x-i])]
        # arr[len(arr)] = x
        return arr
    else:
        return "array is empty"

only_keep([2,4,6,8,10], 3)
