import sys
a = complex(int(sys.argv[1]), int(sys.argv[2]))
b = complex (int(sys.argv[3]), int(sys.argv[4]))
c = a + b
print "\n Addition of two numbers is", c
c = a - b
print "\n Subtraction of two numbers is", c
c = a * b
print "\n Multiplication of two numbers is", c
c = a / b
print "\n Division of two numbers is", c
