#Scale the array
# given an arra and a number
# multiply all values in arr by nyumb
#return the changed arr

def scale_array(arr, num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr


print(scale_array([2,3,4,5,3,3,4,99], 4))
