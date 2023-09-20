principal = float(input("Enter the principal amount:"))
rate_of_interest = float(input("Enter the annual interest rate:"))
time_period = float(input("Enter the time period(in years):"))

rate_of_interest = rate_of_interest / 100
simple_interest = (principal * rate_of_interest * time_period) / 100
print(f"Simple Interest:{simple_interest:.2f}")
