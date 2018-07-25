'''
Create a list of 5 names and check given name exist in the List.
        a) Use membership operator ( IN ) to check the presence of an element.
        b) Perform above task without using membership operator.
        c) Print the elements of the list in reverse direction.

'''
'''
Create a list of 5 names and check given name exist in the List.
        a) Use membership operator ( IN ) to check the presence of an element.
        b) Perform above task without using membership operator.
        c) Print the elements of the list in reverse direction.
'''
name_list = ["Monika", "Sachin","Amit", "Tushar", "Rohit"]
name_list2 = ["Monika", "Sachin", "Tushar", "Rohit"]

#USING "IN" operator
if("Amit" in name_list):
    print "It is present in the list"
else:
    print "Not Present"

#Without using "IN"
temp=0
i=0
while(i <len(name_list)):
    if("Amit" == name_list[i]):
        temp += 1
    i += 1

if(temp==0):
    print "Not Present"
else:
    print "It is present in the list"


#Reversing the list        
print "In reverse ",name_list[-1::-1]
