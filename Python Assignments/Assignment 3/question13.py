'''
Write a program to find the biggest of 4 numbers.
   a)  Read 4 numbers from user using Input statement.
   b) extend the above program to find the biggest of 5 numbers.
( PS : Use IF and IF & Else , If and ELIf, and Nested IF )
'''
num_list = []
sum_of_num = 0

#biggest of 4 numbers
for i in range(4):
    while True:
        try:
            i = int(raw_input("Enter the numbers : "))
            break
        except:
            print "You entered incorrectly, Please eneter integers "
            continue

    num_list.append(i)

print 'biggest of 4 numbers ',max(num_list)


#biggest of 5 numbers
for i in range(5):
    while True:
        try:
            i = int(raw_input("Enter the numbers : "))
            break
        except:
            print "You entered incorrectly, Please eneter integers "
            continue

    num_list.append(i)

print 'biggest of 5 numbers ',max(num_list)
