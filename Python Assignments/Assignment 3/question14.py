'''
Write a program to create two list A and B such that List A contains Employee Id, List B contains Employee name
     ( minimum 10 entries in each list ) and perform following operations
     a) Print all names on to screen
     b) Read the index from the  user and print the corresponding name from both list.
     c) Print the names from 4th position to 9th position
     d) Print all names from 3rd position till end of the list
     e) Repeat list elements by specified number of times ( N- times, where N is entered by user)
     f)  Concatenate two lists and print the output.
     g) Print element of list A and B side by side.( i.e.  List-A First element ,  List-B First element )

'''
listA = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
listB = ["Amit", "Monika", "Sachin", "Tushar", "Rohit", "Rakesh", "Sandeep", "Sharad", "Amol", "Avishek"]

#Print all names on to screen
for i in listB:
    print i

#Read the index from the  user and print the corresponding name from both list.
index = int(raw_input("Enter the index :"))
print "At index %s, the Employee Number is : %s, and the Employee Name is : %s"%(index,listA[index],listB[index])

#Print the names from 4th position to 9th position
print listB[4:9]


#Print all names from 3rd position till end of the list
print listB[3:]

#Repeat list elements by specified number of times ( N- times, where N is entered by user)
repetition = int(raw_input("How many times you want the list to be repeated?"))
print listA*repetition

#Concatenate two lists and print the output.
print listA+listB

#Print element of list A and B side by side.( i.e.  List-A First element ,  List-B First element )
for j in range(10):
        print "  List-A %s ,  List-B %s "%(listA[j], listB[j])
