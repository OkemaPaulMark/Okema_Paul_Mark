#A simple university system with classes for Person, Student, Lecturer, and Staff
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    
    def display_info(self):
        print(f"\nName: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")

class Student(Person):
    def __init__(self, name, email, phone, student_id, major):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.major = major
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print("Role: Student")

class Lecturer(Person):
    def __init__(self, name, email, phone, employee_id, department):
        super().__init__(name, email, phone)
        self.employee_id = employee_id
        self.department = department
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print("Role: Lecturer")

class Staff(Person):
    def __init__(self, name, email, phone, employee_id, position):
        super().__init__(name, email, phone)
        self.employee_id = employee_id
        self.position = position
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print("Role: Staff Member")

# Example Usage
student1 = Student("Alice Johnson", "alice@uni.edu", "555-1234", "S1001", "Computer Science")
lecturer1 = Lecturer("Dr. Smith", "smith@uni.edu", "555-5678", "E2001", "Computer Science")
staff1 = Staff("Bob Wilson", "bob@uni.edu", "555-9012", "E3001", "Administrator")

# Display information
student1.display_info()
lecturer1.display_info()
staff1.display_info()