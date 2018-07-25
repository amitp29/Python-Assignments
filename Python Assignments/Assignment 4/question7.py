#7. Write program to convert prefix/net mask to IP

subnet = 16
ones = [1]*subnet

b1 = ones[0:8]
b2 = ones[8:16]
b3 = ones[16:24]
b4 = ones[24:32]

lst = [b1, b2, b3, b4]


for j in range(4):
    if(len(lst[j]) < 8):
        x = 8 -len(lst[j])
        y = 0
        for i in range(x):
            lst[j].append(y)
lst2 = []

for k in range(len(lst)):
    add = 0
    for mul in range(8):
        add += lst[k][mul] * (2**(7-mul))
    lst2.append(add)
    
print ' The IP for Net mak = %d is --> %s.%s.%s.%s'%(subnet,lst2[0],lst2[1],lst2[2],lst2[3])
