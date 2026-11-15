class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

student1 = Student("Muzammil")
student1.display()