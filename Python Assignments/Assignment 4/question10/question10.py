f = open('dir_content.txt')
x = f.readlines()
lst = []
j=0
lst_filename = []
lst_filename_copy = []

for line in x:
    lst.append( line.split())

for lines in lst:
    lst_filename.append(lines[4])
    lst_filename_copy.append(lines[4])

for i in range(len(lst_filename)):
    for j in range(i-1):
        if(lst_filename[i-1] == lst_filename_copy[j]):
            print 'Removing duplicate file...',lst_filename_copy[j]
            lst.remove(lst[lst_filename.index(lst_filename_copy[j])])
    j = 0

print '\nThe Entries are now as given below:- \n'
for lines in lst:
    print 'Date - %s, Time - %s %s, Bytes - %s,\tFilename - %s '%(lines[0],lines[1],lines[2],lines[3],lines[4])  
    
f.close()
