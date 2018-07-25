#Program to find the greatest of 3 given numbers

a = 14
b = 10
c = 3

print "Let's find the greatest of these 3 numbers"

if(a>b):
    if(c>a):
        print 'c is greatest'
    else:
        if(a==c):
            print 'a and c is greatest'
        else:
            print 'a is greatest'

else:
    if(c>b):
        print 'c is greatest..'
    if(b==c):
        if(a==b):
            print 'All are equal'
        else:
            print 'b and c are greatest'

    else:
        if(a==b):
            print 'a and b is greatest'
        else:
            print 'b is greatest'
