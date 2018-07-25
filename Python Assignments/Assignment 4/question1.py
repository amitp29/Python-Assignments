#Question 1

#1. What will be the output of 'seclist' in print commands of below code?

mylist = range(4)
seclist = mylist
print seclist
mylist.append(4)
print seclist
seclist = mylist[:]
print 'mylist[:]------------',seclist
mylist.append(5)
print seclist
print mylist


'''
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
mylist[:]------------ [0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
'''
