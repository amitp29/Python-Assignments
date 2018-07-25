'''
4.	Given a list of strings, return a list with the strings in sorted order, except 
                group all the strings that begin with 'x' first.  
                e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
                ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']. 
Hint: this can be done by making 2 lists and sorting each of them before combining them.
i.	['bbb', 'ccc', 'axx', 'xzz', 'xaa']
ii.	['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

'''

list1 = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
list2 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

super_list = [list1, list2]

#Iterating through both lists
for lists in super_list:
    lst = []
    lst2 = []
    #Sorting the list
    lists = sorted(lists)
    for word in lists:
            if(word[0]=='x'):
                lst.append(word)
            else:
                lst2.append(word)
    #Combining the lists
    lists = lst+lst2
    print lists
    


