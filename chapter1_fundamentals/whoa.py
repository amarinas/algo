def whoa():
    #add odd intergers from -3000 to 3000 and console log sum
    sum = 0
    for i in range(-300000, 300000):
        if i % 2 == 1:
            sum = sum + i
    return sum


print(whoa())
