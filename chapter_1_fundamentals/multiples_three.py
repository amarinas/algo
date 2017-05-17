# print multiples of 3 from -300, 0 skip -3 and -6

def multiple_three():
    for i in range(-300,0):
        if i % 3 == 0:
            if i == -3 or i == -6:
                break
            else:
                print i


multiple_three()
