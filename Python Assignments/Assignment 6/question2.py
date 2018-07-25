#question 2 - write a regular  expression to extract  a. email id  b. domain name  c. time
import re
email='From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016'
#Regex
regex = re.search(r'From (.*)@(.*)\.com (.*)', email, re.M|re.I)
print 'Email ID : '+regex.group(1)+'@'+regex.group(2)+'.com'
print 'Domain Name : ',regex.group(2)

num = re.sub(r'\D', "", email) 
print 'Time : '+num[2:4]+':'+num[4:6]+':'+num[6:8]
