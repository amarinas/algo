# based on countdown by four
# given lowNum, highNum, mult
# print mult from highNum down to lowNum using For loop

def flexible(lowNum,highNum, mult):
    count = highNum
    while count > 0:
        if count % mult == 0:
            print count
        count = count - 1

print(flexible(2,9,3))
