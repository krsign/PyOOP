# -*- coding: utf-8 -*-

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def get_details(self):
        return self.username, self.email
    
    
user1 = User('krsign','nowimkr@gmail.com','kr#00432')

user2 = User('rocky','rocky@gmail.com','rocky@00432')

user3 = User('stanlee','stan@gmail.com','1029@stanlee')

user4 = User('Kobebryant','basketball@gmail.com','kobe#bryant')

user5 = User('lewis','hamilton@gmail.com','f1racing@f1')

' to access all object and get the details using loops'
users = [user1, user2, user3, user4, user5]

for user in users:
    print(user.get_details())