#7.	Write a code to compare two string data based on the length of the string hint; __gt__ method
import re

class Comp():
    def __init__(self, values):
        self.__values = values

    def __gt__(self,strng):
        if(self.__values==strng.__values):
            print "You entered same strings"
            return False
        else:    
            if(len(self.__values)>len(strng.__values)):
                print 'The first string : "'+self.__values+'" is a bigger string based on length'
                return True

            elif(len(self.__values)==len(strng.__values)):
                if((self.__values)>(strng.__values)):
                    print 'The first string : "'+self.__values+'" is a bigger string based on alphabetical/numeric order, preference starting from first values'
                    return True
                else:
                    print 'The second string : "'+strng.__values+'" is a bigger string based on alphabetical/numeric order, preference starting from first values'    
                    return False
            else:
                print 'The second string : "'+strng.__values+'" is a bigger string based on length'
                return False

print 'Enter 2 values, You can enter any value but it would be treated as STRING'
while(True):
    a = raw_input('Enter first string ').lower()
    str1 = Comp(a)
    matchObj = re.search( r'\W', a, re.M|re.I)
    if matchObj:
        print 'You have entered symbols or whitespaces'
        break

    b = raw_input('Enter second string ').lower()
    str2 = Comp(b)
    matchObj = re.search( r'\W', b, re.M|re.I)
    if matchObj:
        print 'You have entered symbols or whitespaces'
        break

    print str1>str2 #Operator Overloading
