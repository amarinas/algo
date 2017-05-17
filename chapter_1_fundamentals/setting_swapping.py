def setting_swapping():
    # swapping value
    # change myName value with myNumber  and vice versa
    myNumber = 42
    myName = 'Ali'
    print "my number before ", myNumber
    print "my name before ", myName
    temp = myNumber
    myNumber = myName
    myName = temp

    print "My Name after", myName
    print "My Number after", myNumber


print(setting_swapping())
