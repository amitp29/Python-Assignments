'''
10. Given a number line from -infinity to +infinity.
            You start at 0 and can go either to the left or to the right.
            The condition is that in i’th move, you take i steps.
            In the first move take 1 step, second move 2 steps and so on. 
Hint: 3 can be reached in 2   steps (0, 1) (1, 3). 2 can be reached in 3 steps (0, 1) (1,-1) (-1, 2)
a) Find the optimal number of steps to reach position 1000000000 and -1000000000. 

'''

num = 0

step_counter = 0

pos1 = 1000000000
pos2 = -1000000000
lst = [pos1,pos2]

for val in lst:
    while(num != val):
        step_counter += 1
        a = num

        if((num+step_counter) > val):
            num = num - step_counter    

        else:
            num = num + step_counter

        b = num   
        print (a,b)

    print 'The number of steps to reach %s is : %s'%(val, step_counter)