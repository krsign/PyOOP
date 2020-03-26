# -*- coding: utf-8 -*-
class Person:
    age = 22
    def print_age(cls):
        print('Person Age :',cls.age)
        
Person.print_age = classmethod(Person.print_age)
Person.print_age()