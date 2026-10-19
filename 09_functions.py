# Python Functions
# Day 9 - Python Foundations

def greet(name):
    print("Hello,", name)


def add_numbers(a, b):
    return a + b


def is_even(number):
    return number % 2 == 0


# Calling functions
greet("Harsha")

result = add_numbers(10, 20)
print("Sum:", result)

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))
