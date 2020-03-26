# -*- coding: utf-8 -*-

""" 
    Student :
        roll_no
        class
        marks : {'sub':30....}
        
Total Marks : 500
1. Calculate Percentage for every student
2. if percent is less than 40 : result : Pass/ Fail
3. All failed student and their details
4. Top 3 student
"""

class Student:
    
    def __init__(self, roll_no, marks, std):
        self.roll_no = roll_no
        self.marks = marks
        self.std = std
        
        
    
    def cal_result(self):
        self.per = (sum(self.marks.values()) / 500) * 100
        
        if self.per < 40 :
            self.result = 'Fail'
        else:
            self.result = 'Pass'
            
    def get_details(self):
        return '{} {} {} '.format(self.roll_no, self.per, self.result)
    

class Std:
    def __init__(self, name, class_teacher_name):
        self.name = name
        self.class_teacher_name = class_teacher_name
        
std1 = Std('1', 'ABC')
std2 = Std('2', 'PSR')
std3 = Std('3', 'RST')  




stud1 = Student(1, {'eng': 75, 'phy': 56, 'chem': 80, 'computer': 76, 'evs': 90}, std1)
stud2 = Student(2, {'eng': 71, 'phy': 40, 'chem': 49, 'computer': 26, 'evs': 90}, std2)
stud3 = Student(3, {'eng': 35, 'phy': 41, 'chem': 39, 'computer': 50, 'evs': 33}, std3)
stud4 = Student(4, {'eng': 73, 'phy': 34, 'chem': 67, 'computer': 40, 'evs': 40}, std1)
stud5 = Student(5, {'eng': 30, 'phy': 40, 'chem': 30, 'computer': 30, 'evs': 30}, std1)

# IF YOU WANT TO GET THE VALUE OF OBJECT USE __dict__
# print(stud1.__dict__)

# TO get the teacher name
print(stud1.std.class_teacher_name)

students = [stud1, stud2, stud3, stud4, stud5]

#   calculte the result of all students
print('Result of all students->')
for student in students:
    student.cal_result()
    print(student.get_details())
    
    
    
# All Failed Student
print('\n')
print('All Fail Students->') 
for student in students:
    if student.result == 'Fail':
        print(student.get_details())
        
        
# top 3 student   
print('\n')
print('List of top 3 students ->')
l1 = sorted(students, key = lambda student : student.per)
l2 = l1[-3:]
for student in l2:
    print(student.get_details())
    
