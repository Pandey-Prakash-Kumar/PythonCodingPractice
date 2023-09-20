decimal_number = int(input("Enter a number:"))
octal_number = ""
while decimal_number > 0:
    remainder = decimal_number % 8
    octal_number = str(remainder) + octal_number
    decimal_number //= 8

print(octal_number)
