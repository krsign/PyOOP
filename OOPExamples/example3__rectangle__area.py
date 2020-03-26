# -*- coding: utf-8 -*-

class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    
    def area(self):
        return self.lenght * self.width

r1 = Rectangle(5, 4)
print(r1.area())