month = int(input("Enter the month (numeric format, 1-12):"))

days_in_month = None

if month == 1:
    days_in_month = 31
elif month == 2:
    #if 
    days_in_month = 28
elif month == 3:
    days_in_month = 31
elif month == 4:
    days_in_month = 30
elif month == 5:
    days_in_month = 31
elif month == 6:
    days_in_month = 30
elif month == 7:
    days_in_month = 31
elif month == 8:
    days_in_month = 31
elif month == 9:
    days_in_month = 30
elif month == 10:
    days_in_month = 31
elif month == 11:
    days_in_month = 30
elif month == 12:
    days_in_month = 31
else:
    print("Invalid Number")

if days_in_month is not None:
    print(f"{month}: {days_in_month} days")