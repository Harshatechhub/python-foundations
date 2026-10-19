# Student Grade Calculator
# Mini Project 01 - Python Foundations

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
percentage = (total / 500) * 100

grade = calculate_grade(percentage)

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total, "/ 500")
print("Average:", average)
print("Percentage:", percentage, "%")
print("Grade:", grade)
