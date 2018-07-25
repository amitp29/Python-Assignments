'''
3.	Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.  

i.	['axa', 'xyz', 'gg', 'x', 'yyy']
ii.	['x', 'cd', 'cnc', 'kk']
iii.	['bab', 'ce', 'cba', 'syanora']

'''
list1 = ['axa', 'xyz', 'gg', 'x', 'yyy']
list2 = ['x', 'cd', 'cnc', 'kk']
list3 = ['bab', 'ce', 'cba', 'syanora']

print "Let's find how many words are there in which the 'string length is 2 or more' & 'first and last chars are same'.\n"
super_list = [list1, list2, list3]

for lists in super_list:
    count = 0
    print 'The list is: ',lists
    for word in lists:
        if(len(word)>=2 and word[0]==word[-1]):
            print '1 such word is ',word
            count += 1
            
    if(count==1):  
        print 'The list has only %s such word \n'%(count)       
    if(count>1):   
        print 'The list has %s such words \n'%(count)    
