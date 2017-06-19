#Remove duplicates in an array arr = [4,4,3,3,2,2,1,1];

def remove_dup(arr):
    slow = 0
    count = len(arr)
    for i in range(1, len(arr)):
        if arr[i] != slow:
            slow += 1
            print slow
            arr[slow]= arr[i]

    count = slow + 1
    return count



print(remove_dup([4,4,3,3,2,2,1,1]))
