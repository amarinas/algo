# given an array
# write a function that reverese the value
# given reverse([3,1,6,4,2]) =[2,4,6,1,3]

def reverse_array(arr):
    size = len(arr) # getting the length of the sequence
    index = size -1
    iteration = size/2 # number of iteration required
    for i in range(0, iteration): # i is the low index pointer
        temp = arr[index] # temp to store a swap
        arr[index] = arr[i]
        arr[i] = temp
        index -= 1 # decrement the index pointer down
    return arr


print(reverse_array([2, 5, 8, 65, 1, 7, 24]))
