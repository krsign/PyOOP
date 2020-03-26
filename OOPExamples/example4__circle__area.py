# -*- coding: utf-8 -*-

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (3.14 * (self.radius ** 2))

c1 = Circle(4)
print(c1.area())    
