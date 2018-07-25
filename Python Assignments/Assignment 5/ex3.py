def isListOfInts(lst,ret=False):

        try:
            lst.append('')
                     
        except:
            print 'ValueError: ',lst,'- arg not of <list> type'
            

        else:
            lst.pop()
            temp = 0
            if not (lst==[]):
                
                for num in lst:
                
                    if (type(num)==int) :
                
                        temp += 1
            if (temp == len(lst) or lst==[]):
                
                x = True
            else:
                x = False
            return x
        
def testList(arg):
    print arg, isListOfInts(arg)
