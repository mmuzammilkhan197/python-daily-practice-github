def greet(name="Student"):
    print("Hello", name)

greet("Muzammil")
greet()


def add(*numbers):
    print("Total:", sum(numbers))

add(10, 20, 30)