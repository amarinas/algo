# given two numbers
# return array length num1
# with each value num2
# ptint junx if they are the same

def this_length(num1, num2):
    newarr =[]
    if num1 == num2:
        print "jinx its the same number"
    else:
        for i in range(0, num1):
            newarr.append(num2)
        return newarr


print(this_length(4, 4))
print(this_length(7, 8))
