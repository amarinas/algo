#Create an array X and fill the array with 10 values, each value being a random integer between 0 to 100.  For example when your program is done, X could be something like this: [35, 15, 3, 39, 53, 93, 25, 39, 59, 21].
from random import randint

def random_arr():
    newarr = []
    for i in range(1,11):
        newarr.append(randint(1,100))
    return newarr



print(random_arr())
