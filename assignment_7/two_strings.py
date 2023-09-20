string1 = input("Enter the first string:")
string2 = input("Enter the second string: ")
match (string1, string2):
    case (string1,string2) if string1 == string2:
        print("The two strings are indetical")
    case (string1, string2) if string1 < string2:
        print(string1, string2)
    case (string1, string2) if string1 > string2:
        print(string2, string1)