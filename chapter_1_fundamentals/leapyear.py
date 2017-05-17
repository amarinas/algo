# write a function that determines whether a given year is a leap year
# if the year is divisible by four, its a leap year
# unless its divisible by 100
# if it is divisible by 400 than it is


def leapyear(year):
    if year % 4 == 0:
        print "it is a leap year"
    elif year % 100 ==0:
        print "not a leap year buddy!"
    elif year % 400 == 0:
        print "it is a leap year"
    else:
        print "not a leap year"




print(leapyear(1901))
print(leapyear(2000))
