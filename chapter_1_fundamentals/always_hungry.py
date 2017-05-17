# create a function witn given array
# print yummy
# if there is no food then then print im hungry

def always_hungry(arr):
    status = True
    for i in range(len(arr)):
        if arr[i] == "food":
            print "yummy"
            status = False

    if status == True:
        print "im hungry"





always_hungry(["tomatoe", "lop", 3, "sk" ,5])
always_hungry(["tomatoe", "food", 3, "food" ,5])
