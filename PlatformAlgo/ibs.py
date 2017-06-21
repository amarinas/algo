def ibs(arr, n):
    first = 0
    last = len(arr)-1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == n:
            return arr[mid]
        else:
            if n < arr[mid]:
                last = mid - 1
            else:
                first = mid +1
    return found

arr = [1,5,3,52,6,44,64,23]
arr.sort()
print(ibs(arr, 5))
print(ibs(arr, 33))
print(ibs(arr, 23))

#need the index instead of value
