print("Press + for addition")
print("Press - for subtraction")
print("Press * for multiplication")
print("Press / for division")

ch = str(input("Enter the instruction:"))
a=int(input("first number:"))
b=int(input("second number:"))
match ch:
    case '+':
        print(a, "+",b,"=",a+b)
    case '-':
        print(a, "-",b,"=",a-b)
    case '*':
        print(a, "*",b,"=",a*b)
    case '/':
        print(a, "/",b,"=",a/b)
    case _:
        print("Inavlid instruction")
    
