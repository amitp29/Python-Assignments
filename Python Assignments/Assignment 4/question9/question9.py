f = open('dir_content.txt')
x = f.readlines()
lst = []

for line in x:
    lst.append( line.split())

for lines in lst:
    print 'Date - %s, Time - %s %s, Bytes - %s, Filename - %s '%(lines[0],lines[1],lines[2],lines[3],lines[4])
