a = int(input("Enter coefficient of a:"))
b = int(input("Enter coefficient of b:"))
c = int(input("Enter coefficient of c:"))

discriminant = b**2 - 4 * a * c

if(discriminant>0):
    print("Two real and distinct roots")
elif(discriminant==0):
    print("real & equal roots")
else:
    print("imaginary roots")

    
