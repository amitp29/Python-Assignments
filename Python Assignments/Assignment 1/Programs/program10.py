import sys
arg = [0,0]
arg[0] = int(sys.argv[1])
arg[1] = int(sys.argv[2])


arg[0] += arg[1]
print "\n Addition of two numbers is", arg[0]
arg[0] -= arg[1]
print "\n Subtraction of two numbers is", arg[0]
arg[0] *= arg[1]
print "\n Multiplication of two numbers is", arg[0]
arg[0] /= arg[1]
print "\n Division of two numbers is", arg[0]
arg[0] %= arg[1]
print "\n modulus of two numbers is", arg[0]
arg[0] **= arg[1]
print "\n Exponentiation of two numbers is", arg[0]
arg[0] //= arg[1]
print "\n Floor division of two numbers is", arg[0]
