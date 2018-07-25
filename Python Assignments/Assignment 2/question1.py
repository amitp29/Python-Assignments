#1.	Given a list, 
#url = [www.annauniv.edu, www.google.com, www.ndtv.com, www.website.org, www.bis.org.in, www.rbi.org.in];
#Sort the list based on the top level domain (edu, com, org, in) using custom sorting
import re

lst =[]
url = ['www.annauniv.edu', 'www.bis.org.in',  'www.google.com', 'www.ndtv.com', 'www.website.org', 'www.rbi.org.in']

for word in url:
    extract = word.split('.')
    #Appending rank
    if ((extract[len(extract)-1] == 'edu')):
        lst.append((word , 1))
    if ((extract[len(extract)-1] == 'com')):
        lst.append((word, 2))
    if ((extract[len(extract)-1] == 'org')):
        lst.append((word, 3))
    if ((extract[len(extract)-1] == 'in')):
        lst.append((word, 4))
    
# sort by rank
sorted_lst = sorted(lst, key=lambda url: url[1])   
#for tupl in sorted_lst:
 #   print tupl[0]

for (x,y) in sorted_lst:
    print x
