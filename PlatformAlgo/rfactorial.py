def rfactorial(num):
    if num == 1:
        return 1
    else:
        return num * rfactorial(num - 1)


print(rfactorial(5))
