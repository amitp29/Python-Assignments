'''
Create a list with at least 10 elements in it :-
       print all elements
       perform slicing
       perform repetition with * operator
       Perform concatenation wiht other list.

'''
#perform repetition with * operator
list1 = [1]*7
list2 = [4,5,6]

#Perform concatenation with other list
list3 = list1+list2
print list3

#print all elements
for i in list3:
    print i

#perform slicing
print "Sliced list",list3[2:]
