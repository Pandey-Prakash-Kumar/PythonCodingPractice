num = int(input("Enter a number:"))
print(f"first {num} Prime numbers:")
number = 2
count = 0
while count != num:
    for i in range(2,number):
        if number % i == 0:
            number+=1
            break
    else:
        print(number)
        number+=1
        count+=1