import sys

print 'There are %s arguments..'%(len(sys.argv))
print 'The arguments are: ', (sys.argv)

print 'The biggest number of the three is: ',max((sys.argv)[1:])
