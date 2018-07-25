def ruler(num):
    rem = num %10
    div = num/10
    str1 = ''
    str2 = ''
    y = ''
    c=1
    for a in range(1,num+1):        
            b = a%10
            if (b!=0):
                b = ' '
                str2 = str2+str(b)
                
            else:
                str2 = str2+str(c)
                c +=1     
    print str2
    
    for x in range(1,num+1):
            y = x%10
            str1 = str1+str(y)
            
    print str1
    
ruler(51)
print ' '
ruler(43)
print ' '
ruler(5)
print ' '
ruler(10)
print ' '
ruler(80)





