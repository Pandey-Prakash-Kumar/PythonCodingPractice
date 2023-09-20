start = int(input("Enter initial no."))
end = int(input("Enter last no."))
for number in range(start, end+1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        print(number)      
