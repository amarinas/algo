def linearSearch(key, arr):
    for i in range(len(arr)):
        if key == arr[i]:
            return 1
    return False



arr = [24, 8, 23, 3]
print(linearSearch(8, arr))
print(linearSearch(-99, arr))
