# given an array
# create a function replace the last value with number of positives
# ex [-1,2,2,2] = [-1,2,2,3]
def count_posivites(arr):
    count = 0
    last = len(arr)-1
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
    arr[last] = count # assign last index to a count
    # print count
    return arr

print(count_posivites([-1,2,2,2]))
print(count_posivites([-1,2,2,6,8,3]))
