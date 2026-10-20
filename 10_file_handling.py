# Python File Handling
# Learning how to write and read files

# Write data to a file
with open("example.txt", "w") as file:
    file.write("Hello, Harsha!")

# Read data from the file
with open("example.txt", "r") as file:
    content = file.read()

print(content)
