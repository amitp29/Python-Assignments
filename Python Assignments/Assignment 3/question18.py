'''
Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1.( reverse printing)
     a) By using For loop
     b) By using while loop
    c) Let    mystring ="Hello world"
             print each character of  mystring in to separate line using appropriate  loop structure.

'''

'''Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1.( reverse printing)
     a) By using For loop
     b) By using while loop
    c) Let    mystring ="Hello world"
          print each character of  mystring in to separate line using appropriate  loop structure.
'''
#Printing Numbers using for loop
i=0
for i in range(1,101):
    print i

#Printing Numbers in reverse order using for loop
i=0
for i in range(100):
    print 100-i

#Printing Numbers using while loop
i=1
while(i<=100):
    print i
    i += 1

#Printing Numbers in reverse order using while loop
i=0
while(i<100):
    print 100-i
    i += 1

#Printing each character
mystring ="Hello world"
for i in mystring:
    print i
