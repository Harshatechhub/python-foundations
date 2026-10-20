# Count the number of digits in a number

number = int(input("Enter a number: "))

number = abs(number)

if number == 0:
    count = 1
else:
    count = 0

    while number > 0:
        number //= 10
        count += 1

print("Number of digits:", count)
