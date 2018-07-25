def isWhiteLine(str):
    if(str.split()==[]):
        return True
    return False
    
for line in open('Amit.txt'):
    if not isWhiteLine(line):
        print line





