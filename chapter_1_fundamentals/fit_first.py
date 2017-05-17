#accept an array
# if value at [0] is greater than arrays length print too big
#if value is less than arrays length print too small
# otherwise print just right

def fit_first(arr):
    if arr[0] > len(arr):
        print "thats too big"
    elif arr[0] < len(arr):
        print "thats too small"
    else:
        print "just right"

fit_first([3,4,5])
fit_first([2,4,5,6,7,7,8])
fit_first([9,4,5,6,7,7,8])
