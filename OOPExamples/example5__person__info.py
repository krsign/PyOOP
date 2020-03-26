# -*- coding: utf-8 -*-
import datetime

class Person:
    
    def __init__(self, fname, lname, dob, phone, email, address):
        
        self.fname = fname
        self.lname = lname
        self.dob = dob
        
        self.phone = phone
        self.email = email
        self.address = address
        
    def find_age(self):
        
        now = datetime.date.today()
        age = now.year - self.dob.year
        return age
    
p1 = Person('Krishna','Kumar',datetime.date(1998, 10, 10), '91XXXXXXXX', 'nowimkr@gmail.com', 'Bangalore, India')


print('Name : ', p1.fname, p1.lname)
print('Birthdate :', p1.dob)
print('Age :', p1.find_age())
print('Phone Number :', p1.phone)
print('Email addresss :', p1.email)
print('Address : ', p1.address)
