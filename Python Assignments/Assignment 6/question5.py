class Sqroot(object):        
    def sqroot(self, num):
        if(type(num)==int):
            print 'The square root of the number is ',num**0.5
        else:
            print 'Please Enter integers'
    

class Add(object):        
    def add(self, num1, num2):
        if(type(num1)==int and (type(num2)==int)):
            print 'The sum of the numbers is :',num1+num2
        else:
            print 'Please Enter integers'

class Sub(object):
    def sub(self, num1, num2):
        if(type(num1)==int and (type(num2)==int)):
            if(num1>=num2):
                print 'The difference of the numbers is :',num1-num2
        if(num1<num2):
            print 'The difference of the numbers is negative:',num1-num2
        else:
            print 'Please Enter integers'


class Mul(object):
    def mul(self, num1, num2):
        if(type(num1)==int and (type(num2)==int)):
            print 'The multiplication of the numbers is :',num1*num2
        else:
            print 'Please Enter integers'


class Div(object):
    def div(self, num1, num2):
        if(type(num1)==int and (type(num2)==int)):
            if(num2 == 0):
                print 'Second number is zero, Please Enter a different number to avoid "ZeroDivisionError"'
            else:
                print 'The division of the numbers is :',(num1/float(num2))
        else:
            print 'Please Enter integers'


class Mathnew(Add, Sub, Sqroot, Mul, Div):
    def __init__(self):
        super(Mathnew, self).__init__()
            
ob = Mathnew()
ob.sqroot(9)
ob.add(6,4)
ob.sub(3,5)
ob.mul(6,4)
ob.div('s',4)
