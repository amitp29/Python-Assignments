#Program to add, subtract, multiply and divide 2 numbers

def addition(num1, num2):
    if(type(num1)==int and (type(num2)==int)):
        print 'The sum of the numbers is :',num1+num2
    else:
        print 'Cannot perform desired function, Please Enter integers'

def subtraction( num1, num2):
    if(type(num1)==int and (type(num2)==int)):
        if(num1>=num2):
            print 'The difference of the numbers is :',num1-num2
    if(num1<num2):
        print 'The difference of the numbers is negative:',num1-num2
    else:
        print 'Cannot perform desired function, Please Enter integers'

def multiplication( num1, num2):
    if(type(num1)==int and (type(num2)==int)):
        print 'The multiplication of the numbers is :',num1*num2
    else:
        print 'Cannot perform desired function, Please Enter integers'

def division( num1, num2):
    if(type(num1)==int and (type(num2)==int)):
        if(num2 == 0):
            print 'Second number is zero, Please Enter a different number to avoid "ZeroDivisionError"'
        else:
            print 'The division of the numbers is :',(num1/float(num2))
    else:
        print 'Cannot perform desired function, Please Enter integers'

addition(2,7)
subtraction(2,7)
multiplication(2,7)
division(1,2)
