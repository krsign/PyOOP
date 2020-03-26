# -*- coding: utf-8 -*-

import math

class Point:
    'Represents a point in two-dimentional geometric co-ordinates'
    
    def __init__(self, x = 0, y = 0):
        '''Initialize the position of a new point. the x and y
           co-ordinates can be specified. if they are not, the point default to the origins'''
        self.move(x, y)
        
    def move(self, x, y):
        "Move the point to a new point location in two-dimention space"
        self.x = x
        self.y = y
        
    def reset(self):
        'Reset the point back to the geometric origins: 0, 0 '
        self.move(0,0)
        
    def calculate__distance(self, other__points):
        
        '''
        Calculate the distance from this point to the second point  passed as paramter 
        
        This function uses pythagorean Theorem to calculate the distance between the two points

        '''
        return math.sqrt((self.x - other__points.x)**2 + (self.y - other__points.y)**2)
    
    