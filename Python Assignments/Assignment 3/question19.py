'''
Using loop structures print even numbers between 1 to 100.
     a) By using For loop , use continue/ break/ pass statement to skip  odd numbers.
           i)  break the loop if the value is 50
           ii) Use continue for the values 10,20,30,40,50

     b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
            i)  break the loop if the value is 90
           ii) Use continue for the values 60,70,80,90
'''

for i in range(101):
    #even numbers
    if(i%2==0):
        print i

i=0
for i in range(101):
    if(i%2!=0):
        continue

    if(i==50):
        break

    if(i==10 or i==20 or i==30 or i==40 or i==50 ):
        continue

i=0
while(i<=100):
    if(i%2!=0):
        continue

    if(i==90):
        break

    if(i==60 or i==70 or i==80 or i==90):
        continue

    i += 1
