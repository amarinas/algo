def rbs(arr, n):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) //2
        loc = len(arr)
        if arr[mid] == n:
            return arr[mid]
        else:
            if n < arr[mid]:
                return rbs(arr[:mid], n)
            else:
                return rbs(arr[mid +1:], n)

arr = [1,5,3,52,6,44,64,23]
arr.sort()
print(rbs(arr, 5))
print(rbs(arr, 33))
print(rbs(arr, 23))
