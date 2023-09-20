string = input("Enter the string:")

match string:
    case string if ' ' in string:
        print("Multiword String")
    case _:
        print("Singleword string")