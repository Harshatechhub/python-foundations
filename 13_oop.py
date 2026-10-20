# Python Object-Oriented Programming
# Learning classes and objects


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")


# Create an object
student1 = Student("Harsha", 18)

# Use the object's method
student1.introduce()
