class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Muzammil", 19)
student2 = Student("Ali", 22)

print(student1.name, student1.age)
print(student2.name, student2.age)