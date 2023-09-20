print("Enter three number:")
x = int(input())
y = int(input())
z = int(input())

if(x>y and x>z):
    print(x, "is greater")
elif(y>x and y>z):
    print(y, "is greater")
else:
    print(z, "is greater")


