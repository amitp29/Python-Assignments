'''
Create a tuple with at least 10 elements in it :-
       print all elements
       perform slicing
       perform repetition with * operator
       Perform concatenation wiht other list.

'''

#perform repetition with * operator
tuple1 = (1,)*7
tuple2 = (4,5,6)

#Perform concatenation with other tuple
tuple3 = tuple1+tuple2
print tuple3

#print all elements
for i in tuple3:
    print i

#perform slicing
print "Sliced tuple",tuple3[2:]
