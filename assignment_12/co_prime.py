import math
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

gcd = math.gcd(num1, num2)

if gcd == 1:
    print(f"{num1}, {num2} are co-prime")
else:
    print(f"{num1}, {num2} are not co-prime. Their gcd is {gcd}")
    