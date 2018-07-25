#question 3 - Mymath class without init method

class Mymath(object):
    
    def sqroot(self, num):
        print 'Inside sqroot method'
        if(type(num)==int):
            print 'The square root of the number is ',num**0.5
        else:
            print 'Please Enter integers'
            
    def addition(self, num1, num2):
        print 'Inside addition method'
        if(type(num1)==int and (type(num2)==int)):
            print 'The sum of the numbers is :',num1+num2
        else:
            print 'Please Enter integers'
    
    def subtraction(self, num1, num2):
        print 'Inside subtraction method'
        if(type(num1)==int and (type(num2)==int)):
            if(num1>=num2):
                print 'The difference of the numbers is :',num1-num2
        if(num1<num2):
            print 'The difference of the numbers is negative:',num1-num2
        else:
            print 'Please Enter integers'
    
    def multiplication(self, num1, num2):
        print 'Inside multiplication method'
        if(type(num1)==int and (type(num2)==int)):
            print 'The multiplication of the numbers is :',num1*num2
        else:
            print 'Please Enter integers'
    
    def division(self, num1, num2):
        print 'Inside division method'
        if(type(num1)==int and (type(num2)==int)):
            if(num2 == 0):
                print 'Second number is zero, Please Enter a different number to avoid "ZeroDivisionError"'
            else:
                print 'The division of the numbers is :',(num1/float(num2))
        else:
            print 'Please Enter integers'
    

    
m = Mymath()
m.sqroot('s')
m.addition(2,7)
m.addition(2,7)
m.multiplication(2,7)
m.division(1,2)
