# given an array
# if there are array has 3 odds value in a row print thats odds
# if there are 3 evens in a row print even nmore so!

def evens_odd(arr):
    even = 0
    odd = 0
    for i in arr:
        if arr[i] % 2 == 0:
            odd = 0
            even += 1
            if even == 3:
                even= 0
                print "Even more so!"
        else:
            even = 0
            odd += 1
            if odd == 3:
                odd= 0
                print "thats odd!"

evens_odd([1,1,1,4,3,4])
evens_odd([2,2,2,4,3,4])
