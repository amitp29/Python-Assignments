import sys

a = sys.argv[0] and sys.argv[1]
b = sys.argv[0] or sys.argv[1]
c = not(sys.argv[0] and sys.argv[1])

print a
print b
print c
