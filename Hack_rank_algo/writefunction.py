#Determine if a year is a leap yesar

def is_leap(year):
    leap = False
    #condition for a leap year
    if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
        return True

        #return leap if the above condition is false
    return leap




year = int(raw_input())
print is_leap(year)
