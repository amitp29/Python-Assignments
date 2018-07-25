#10.	Create a class called First and two classes called Second  and Third 
#which inherit from First. Create class called Fourth which inherits 
#from Second and Third. Create a common method called method1 in all the classes and provide the Method Resolution Order

class First(object):
    def __init__(self):
        print 'Inside __init__ of First class'

    def method1(self):
        print 'Inside method1 of First class'


class Second(First):
    def __init__(self):
        print 'Inside __init__ of Second class'

    def method1(self):
        print 'Inside method1 of Second class'
        super(Second, self).method1()


class Third(First):
    def __init__(self):
        print 'Inside __init__ of Third class'

    
    def method1(self):
        print 'Inside method1 of Third class'
        super(Third, self).method1()


class Fourth(Second, Third):
    def __init__(self):
        print 'Inside __init__ of Fourth class'
        
    def method1(self):
        print 'Inside method1 of Fourth class'
        super(Fourth, self).method1()
    
    
obj = Fourth()
obj.method1()
