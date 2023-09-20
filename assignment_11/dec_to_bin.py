decimal_number = int(input("Enter a number:"))
binary_number = ""
while decimal_number > 0:
    r = decimal_number % 2
    binary_number = str(r) + binary_number
    decimal_number = decimal_number // 2

print(binary_number)


