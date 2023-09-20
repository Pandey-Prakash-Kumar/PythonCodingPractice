terms = int(input("Enter the number of Fibonacci terms to generate : "))
a, b = 0,1
count = 0
if terms <= 0:
    print("Please enter a positive inetger: ")
elif terms == 1:
    print("Fibonacci series (first term)")
    print(a)
else:
    while count < terms:
        print(a, end=" ")
        a, b = b, a + b
        count+=1
   
    