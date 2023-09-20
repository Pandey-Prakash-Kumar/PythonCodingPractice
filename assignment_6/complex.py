real_part = float(input("Enter the real part of the complex number: "))
imaginary_part = float(input("Enter the imaginary part of the complex number: "))

# Create a complex number using the user input
complex_num = complex(real_part, imaginary_part)

# Compare the real and imaginary parts
if abs(complex_num.real) > abs(complex_num.imag):
    greater_part = "Real Part"
elif abs(complex_num.real) < abs(complex_num.imag):
    greater_part = "Imaginary Part"
else:
    greater_part = "Both Parts (Equal)"

# Print the result
print(f"The greater part of the complex number is: {greater_part}")