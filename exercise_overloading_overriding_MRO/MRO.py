#MRO (Method Resolution Order) in Python determines the order in which 
#base classes are searched when a method is called on an instance of a class.
class Person:
    def greet(self):
        print("Hello from Person")

class Teacher(Person):
    def greet(self):
        print("Hello from Teacher")

class Student(Person):
    def greet(self):
        print("Hello from Student")

class TeachingAssistant(Student, Teacher):
    pass

# Check MRO
print(TeachingAssistant.mro())

ta = TeachingAssistant()
ta.greet()  # "Hello from Student" (because Student comes first in MRO)