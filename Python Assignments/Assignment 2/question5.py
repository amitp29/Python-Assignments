'''
5.	Given a list of numbers, 
            return a list where all adjacent == elements have been reduced to a single element,
            so [1, 2, 2, 3] returns [1, 2, 3]. 
        You may create a new list or modify the passed in list.
i.	 [1, 2, 2, 3], [2, 2, 3, 3, 3]

'''
lst = [[1, 2, 2, 3], [ 2, 2, 3, 3, 3]]


for lists in lst:
    lst2 = []
    for i in range(len(lists)):
        if(i==0):
            lst2.append(lists[i])
        
        elif(i != len(lists) and i>0):
            if(lists[i] == lists[i-1]):
                continue
            else:
                lst2.append(lists[i])
            
    print 'for the list %s the output will be reduced to: %s'%(lists, lst2)
