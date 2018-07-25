Python L1 Assignments:

1. What will be the output of 'seclist' in print commands of below code?
mylist = range(4)
seclist = mylist
print seclist
mylist.append(4)
print seclist
seclist = mylist[:]
print seclist
mylist.append(5)
print seclist

2. What is the output of following code:
def f(n):
  for x in range(n):
    yield x**3

for x in f(6):
  print x

3. Write a program to receive a string from keybord and check if the string has two 'e' in the characters. 
   If yes return True else False.

4. What is the output of following code:
counter = 1
def dolots(count):
  global counter
  for i in (1, 2, 3):
    counter = count + i

print dolots(4)
print counter


5.	Write a code to read  the data from  input file called input.txt and count the number of characters per line, number of words per line and write these into output file called as output.txt 

6.	Create 3 Lists ( list1,list2,list3) with numbers and perform following operations
         a) Create Maxlist by taking 2 maximum elements from each list.
         b) Find average value from all the elements of Maxlist.
         c) Create a MinlIst by taking 2 minimum elements from each list 
         d) Find the average value from all the elements of Minlist


7.	Write program to convert prefix/net mask to IP
eg: input:16  output: 255.255.0.0


8.	Create a suitable data construct to read the data from an xml document as shown below:
<bookstore shelf="New Arrivals">
  <book category="COOKING">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="CHILDREN">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book category="WEB">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore>

9.	Create a suitable object type and  check for file size of 0 bytes of the directory contents as shown below
02/15/2016              10:49 PM               962                     switchfinal.py
02/15/2016             10:49 PM               943                       switchfinal.py.bak
01/27/2016             11:46 AM                15                        t.py
03/31/2016            12:39 PM               840                        t1.py
01/25/2016            10:34 AM             2,407                      tc1.py
02/14/2017           09:13 AM                 0                           teat.py
03/15/2016          05:52 PM                 5                             tes.py


10.Create a suitable object type to eliminate the duplicate elements
