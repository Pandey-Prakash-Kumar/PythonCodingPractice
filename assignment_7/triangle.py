while True:
    print("1. Check for isoscles triangle ")
    print("2. Check for right angle triangle ")
    print("3. Check for equilateral triangle ")
    print("4. Exit")

    choice = int(input("Enter the choice:"))
    match choice:
        case 1:
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            c = int(input("Enter third number:"))
            if a == b or b == c or c == a:
                print("Isosceles traingle")
            else:
                print("This is not an Isosceles traingle")
        case 2:
            a= int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            c = int(input("Enter third number:"))
            if a == b == c:
                print("Equilateral traingle")