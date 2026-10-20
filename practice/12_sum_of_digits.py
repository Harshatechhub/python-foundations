# Find the sum of digits of a number

number = int(input("Enter a number: "))

total = 0
temp = abs(number)

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print("Sum of digits:", total)
