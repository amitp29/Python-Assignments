'''
Question6.  Create 3 Lists ( list1,list2,list3) with numbers and perform following operations :-
                         a) Create Maxlist by taking 2 maximum elements from each list.
                         b) Find average value from all the elements of Maxlist.
                         c) Create a MinlIst by taking 2 minimum elements from each list 
                         d) Find the average value from all the elements of Minlist
'''

list1 = [4,2,1,3]
list2 = [8,6,7,9,5]
list3 = [15,11,10,12,13]

#Sorting all the lists
list1.sort()
list2.sort()
list3.sort()

Maxlist = []
Minlist = []

lst = [list1, list2, list3]

for i in range(len(lst)):
    for j in range(2):
        Maxlist.append(lst[i].pop())
        Minlist.append(lst[i][j])

print 'Maxlist : ',Maxlist
print 'Minlist : ',Minlist
    
#Calculating Average
avg_Maxlist = 0
avg_Minlist = 0

for num1 in Maxlist:
    avg_Maxlist += num1
    
for num2 in Minlist:
    avg_Minlist += num2
    
print avg_Maxlist/float(len(Maxlist))
print avg_Minlist/float(len(Minlist))
