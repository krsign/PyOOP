# -*- coding: utf-8 -*-
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @staticmethod
    def adult(age):
        if age > 18:
            return True
        else:
            return False
        
    @classmethod
    def from_birth_year(cls, name, birthyear):
        return cls(name, date.today().year - birthyear)
    
    def display(self):
        print('{} age :{}'.format(self.name, self.age))
   
# accessing instance variable
person1 = Person('krsign', 22)
person1.display()

# accessing classmethod 
person2 = Person.from_birth_year('kr', 2008)
person2.display()

# staticmethod
print(Person.adult(22))
print(Person.adult(17))


# we can check what properties objects holds using dir
#print(dir(person1))

# using help we can see how to access
#print(help(person1))
