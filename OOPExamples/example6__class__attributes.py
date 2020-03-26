# -*- coding: utf-8 -*-

class Person:
    
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')
    
    def __init__(self, title, name, surname):
        if title not in self.TITLES:
            raise  ValueError('%s is not valid title' %title)
            
        self.title = title
        self.name = name
        self.surname = surname
        
person = Person('Mr','Krishna','Kumar')

print(person.title, person.name)


# we can access a class attribute from an instance
print(person.TITLES)

# but we can also access it from the class
print(Person.TITLES)



