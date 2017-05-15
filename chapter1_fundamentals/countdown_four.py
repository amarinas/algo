#log positive numbers starting at 2016 counting down by four excludes 0 without a for loop

def countdown_four():
    count = 2016
    while(count > 0):
        if count % 4 == 0:
            print count
        count = count - 1

countdown_four()
