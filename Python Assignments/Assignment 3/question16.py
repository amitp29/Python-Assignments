'''
Write program to perform following:
     i) Check whether given number is prime or not.
    ii) Generate all the prime numbers between 1 to N where N is given number.

'''
temp = 0
#Program to check if the number is prime or not
while True:
    try:
        i = int(raw_input("Enter the number to check for prime : "))
        if(i<=0):
            print "Please enter positive integers!"
            continue
        break
    except:
        print "You entered incorrectly, Please eneter integers "
        continue


if(i==1):
    print "1 is neither prime nor composite"


for j in range(2,i):
    if(i%j==0):
        print "The number is not prime"
        temp += 1
        break
if(temp == 0 and i>1):
    print "The number is prime"


#Program to display prime numbers till the number input by user
print "\n************Let's start the next program to print prime numbers*************\n"
while True:
    try:
        n = int(raw_input("Enter the number till which prime numbers are to be displayed : "))
        if(i<=0):
            print "Please enter positive integers!"
            continue
        break
    except:
        print "You entered incorrectly, Please eneter integers "
        continue

if(n==1):
    print "1 is neither prime nor composite"
else:
    print "The prime numbers till '%s' list is hereunder: "%(n)

for p in range(2,n+1):
    temp = 0
    for q in range(2,p):
        if(p%q==0):
            temp += 1
            break
    if(temp == 0):
        print p
