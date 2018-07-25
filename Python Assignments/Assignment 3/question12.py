'''
Read 10 numbers from user and find the average of all.
a) Use comparison operator to check how many numbers are less than average and print them
b) Check how many numbers are more than average.
c) How many are equal to average.
'''
num_list = []
sum_of_num = 0

for i in range(10):
    while True:
        try:
            i = int(raw_input("Enter the numbers : "))
            break
        except:
            print "You entered incorrectly, Please eneter integers "
            continue
    sum_of_num += i
    num_list.append(i)

average =  sum_of_num/float(len(num_list))
print "Average of the numbers is :", sum_of_num/float(len(num_list))

smaller_num_list =[]
equal_num_list= []
bigger_num_list= []

for j in num_list:
    print j
    if(j<average):
        smaller_num_list.append(j)

    if(j==average):
        equal_num_list.append(j)

    if(j>average):
        bigger_num_list.append(j)


print " Total %s number/numbers are greater than average, they are: %s"%(len(bigger_num_list),bigger_num_list)
print " Total %s number/numbers are equal than average, they are: %s"%(len(equal_num_list),equal_num_list)
print " Total %s number/numbers are lesser than average, they are: %s"%(len(smaller_num_list),smaller_num_list)
