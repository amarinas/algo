# increment the seconds
#given an array
#add 1 to every second element odd index
# print each array value and return array
def increment_seconds(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] += 1
        print arr[i]

    return arr

print(increment_seconds([1, 2, 3, 8 ,4, 5, 6]))
