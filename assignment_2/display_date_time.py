import datetime

current_datetime = datetime.datetime.now()
print(current_datetime)

formatted_datetime1 = current_datetime.strftime("%m/%d/%Y %H:%M:%S")
formatted_datetime2 = current_datetime.strftime("%m/%d/%y %I:%M:%S")
formatted_datetime3 = current_datetime.strftime("%m/%d/%y %I:%M %p")

print("Current date time: ", formatted_datetime1)
print("Current date time: ", formatted_datetime2)
print("Current date time: ", formatted_datetime3)
