#Write a program to find the number is Prime or not.

while True:
    try:
        a = int(raw_input('Enter a number greater than 1, which is to be checked for prime or composite...'))

    except:
        print 'You entered incorrectly! Please try again!'
        continue

    else:
        temp = 0
        if(a==1):
            print '1 is neither prime nor composite'
            break

        if(a<=0):
            print "You entered a number less than or equal to zero"
            break

        else:
            for i in range(2,a):
                if(a%i==0):
                    temp += 1

        if( temp==0 ):
            print "The number %s is prime"%(a)
        else:
            print "The number %s is not prime"%(a)
        break
