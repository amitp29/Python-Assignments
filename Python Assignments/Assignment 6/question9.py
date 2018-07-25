import math 

class Circle(object):
    #Setting default radius as 1
    def __init__(self, radius=1):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
    
    def area(self):
            return math.pi* self.radius**2
        
    def circumference(self):
        return 2* math.pi * self.radius

print 'CASE 1 - AREA & CIRCUMFERENCE OF A DEFAULT CIRCLE...'   
c = Circle()
print 'The radius of default circle is',c.getRadius()
print 'The area of default circle is',c.area()
print 'The circumference of default circle is',c.circumference()

#radius changed of a default circle
print 'CASE 2 - AREA & CIRCUMFERENCE OF AFTER CHANGING A DEFAULT CIRCLE...' 
c = Circle()
print 'Changing the radius of the circle to 3....'
c.setRadius(3)
print 'The radius of new circle is',c.getRadius()
print 'The area of new circle is',c.area()
print 'The circumference of new circle is',c.circumference()

#radius set initially
print 'CASE 3 - AREA & CIRCUMFERENCE OF A NEW CIRCLE...' 
c = Circle(4)
print 'The radius of new circle is',c.getRadius()
print 'The area of new circle is',c.area()
print 'The circumference of new circle is',c.circumference()

