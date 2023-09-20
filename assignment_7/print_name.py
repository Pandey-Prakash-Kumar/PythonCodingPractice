num = int(input("Enter a number:"))
match num:
    case num if num%2 == 0:
        print("Saurabh Shukla")
    case num if num%2 != 0:
        if num < 0:
            print("Prateek Jain")
        else:
            print("Aditya Chaudhary")
