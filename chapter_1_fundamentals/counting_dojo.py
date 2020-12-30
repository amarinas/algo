def count_dojo():
    #print 1-100 if divisible by 5 print coding if iby 10 then print Dojo
    for i in range(0,101):
        if i % 5 == 0:
            print "Coding"

            if i % 5 == 0 and i % 10 == 0:
                print "dojo"

        else:
            print i


count_dojo()
