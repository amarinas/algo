# Swap toward the center
#given an array
# sqap first and last, third to thrid to last

def swap_center(arr):
    size = len(arr) # getting the length of the sequence
    index = size -1
    iteration = size/2 # number of iteration required
    for i in range(0, iteration):
        # print arr[i]
        temp = arr[i]
        # print temp
        arr[i] = arr[index - i]
        # print arr[i]
        arr[index - i] = temp
        # print arr[index - i]
    return arr

print(swap_center(["true", 42, "Ada", 2, "pizza"]))
