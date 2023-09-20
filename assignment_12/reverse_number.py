num = int(input("Enter the number:"))
reversed_num = ""
reversed_number = 0
while num != 0:
    r = num%10
    reversed_num = reversed_num + str(r)
    reversed_number = (reversed_number*10) + r
    num//=10
print(reversed_num)
print(reversed_number)



