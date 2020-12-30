def palindrome(num):
    cnum = num
    rev = 0
    if num < 0:
        return False
        
    while cnum:
        rev = rev * 10 + cnum %10
        cnum /= 10
    return rev == num

print(palindrome(11211))
print(palindrome(-15251))
