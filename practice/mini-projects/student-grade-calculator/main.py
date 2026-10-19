# Student Grade Calculator
# Mini Project 01 - Python Foundations

def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")
mark = float(input("Enter mark: "))

grade = calculate_grade(mark)

print("\n--- Student Result ---")
print("Name:", name)
print("Mark:", mark)
print("Grade:", grade)
