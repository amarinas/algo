def print_count():
    count = 0
    for i in range(512, 4096):
        if i % 5 == 0:
            print i
            count = count +1
    return "total interger multiples of 5 is ", count

print(print_count())
