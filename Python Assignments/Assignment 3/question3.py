#Write a program to find  given number is odd or Even

while True:
    try:
        a = int(raw_input('Enter a number greater than 1, which is to be checked for odd or even...'))

    except:
        print 'You entered incorrectly! Please try again!'
        continue

    else:
        if( a%2==0 ):
            print "The number %s is even"%(a)
        else:
            print "The number %s is odd"%(a)
        break
