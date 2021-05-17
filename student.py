#1st student is file 2nd is class
from classes_and_objects import student
student1=student("jim","business",3.1,False)
student2=student("pam","psychology",4.8,False)
student3=student("charlie","phys.ed.",3.8,True)
print(student1.name)
print(student1.gpa)
print(student2.is_on_probation)
print(student3.gpa)
print(student1.on_honor_roll())
print(student2.on_honor_roll())