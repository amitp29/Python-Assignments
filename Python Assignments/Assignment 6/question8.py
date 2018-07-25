import math 

class Circle(object):
    def area(self,radius):
            return math.pi*radius**2
        
    def circumference(self,radius):
        return 2* math.pi * radius
    
c = Circle()
c.area(3)
c.circumference(5)
