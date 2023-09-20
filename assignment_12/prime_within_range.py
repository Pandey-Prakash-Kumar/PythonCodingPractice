number = int(input("Enter a number:"))
number+=1
for i in range(2,number):
        if number % i == 0:
            number+=1
            continue
else:
    print("Next prime number:",number)
    