def print_count():
# print integer multiple by 5
# print how may times this happens

    # set count to count the times it occur
    count = 0
    #loop through the range from 512 - 4096
    for i in range(512, 4096):
        # make sure its divisible by 5
        if i % 5 == 0:
            # print the existing looping
            print i
            #keep count
            count = count +1
    return "total interger multiples of 5 is ", count

print(print_count())
