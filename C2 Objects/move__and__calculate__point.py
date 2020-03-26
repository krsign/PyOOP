# -*- coding: utf-8 -*-

# -*- krsign -*-
import math

class Point:
    def move(self,x,y):
        self.x = x
        self.y = y
        
    def reset(self):
        self.move(0, 0)
        
    def calculate__distance(self,other__point):
        return math.sqrt(
            (self.x - other__point.x) **2 + 
            (self.y - other__point.y) **2 )
    
# how to use it

point1 = Point()
point2 = Point()

point1.reset()
point2.move(5, 0)

print('Point2 To Point1 : ',point2.calculate__distance(point1))


assert(point1.calculate__distance(point2) == point2.calculate__distance(point1))

point1.move(3,4)

print('Point1 To Point2 : ', point1.calculate__distance(point2))
print('Point1 TO Point1 : ', point1.calculate__distance(point1))