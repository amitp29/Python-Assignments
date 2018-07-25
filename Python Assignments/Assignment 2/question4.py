'''
4.	Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple. 
e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
      Hint: use a custom key= function to extract the last element form each tuple.
i.	 [(1, 3), (3, 2), (2, 1)]
ii.	[(1, 7), (1, 3), (3, 4, 5), (2, 2)]

'''

list1 = [(1, 3), (3, 2), (2, 1)]
list2 = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]

super_list = [list1, list2]
for lists in super_list:
    sorted_list = sorted(lists, key=lambda url: url[-1])  
    print sorted_list

