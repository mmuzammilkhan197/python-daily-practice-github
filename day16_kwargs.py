def student(**details):
    for key, value in details.items():
        print(key, ":", value)

student(name="Muzammil", age=22, city="Karachi")