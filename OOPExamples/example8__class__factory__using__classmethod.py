# -*- coding: utf-8 -*-

from datetime import date

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def from_birth_year(cls, name, birthyear):
        return cls(name, date.today().year - birthyear)
    
    def display(self):
        print(self.name , "age:", str(self.age))

person1 = Person('krsign', 22)
person1.display()

person2 = Person.from_birth_year('kr', 2008)
person2.display()
