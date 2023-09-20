year = int(input("Enter a year"))

match year:
    case year if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        print("Non century leap year")
    case year if year % 100 == 0:
        print("century leap year")
    case _:
        print("Non-century non-leap year") 
