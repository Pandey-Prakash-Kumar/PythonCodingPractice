color = input("Which color do you like:")
match color:
    case color if "yellow" or "Yellow" in color:
        print("Monday")
    case color if "Blue" or "blue" in color:
        print("Tuesday")

