# Python Dictionaries
# Day 8 - Python Foundations

student = {
    "name": "Harsha",
    "age": 18,
    "course": "CSE (AI)"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

# Adding a new key-value pair
student["college"] = "Yenepoya"

# Updating a value
student["age"] = 19

# Displaying the dictionary
print("Student details:", student)

# Looping through a dictionary
for key, value in student.items():
    print(key, ":", value)
