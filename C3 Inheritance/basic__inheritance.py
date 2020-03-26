# -*- coding: utf-8 -*-

class Contact:
    all_contacts = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
class Supplier(Contact):
    def order(self, order):
        print('If this were real system we could send' '{} order to {}'.format(order, self.name))
        
        
c = Contact('Git Hub', 'github@gmail.com')
s = Supplier('Sup Plier', 'supplier@gmail.com')

print(c.name, c.email, s.name, s.email)


c.all_contacts
print(c.all_contacts)

# contact class will not able to access the value of subclass
#c.order('Ineed pliers')

s.order(' I need plier')


