# given 4 params
# print the multiples of param 1 starting at param 2 and extending to param 3
# if a multiple is equal to param 4 then skip
#given( 3,5,17,9) expected (6,12,15)

def final_count(param1,param2,param3,param4):
    count = param3
    while count > param2:
        if count % param1 == 0 and count != param4:
            print count

        count = count - 1

print(final_count(3,5,17,9))
