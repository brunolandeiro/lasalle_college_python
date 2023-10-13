#  Write a program in python that calculates the Amount after interest according to the 
# equation (you can assume m = 1):

principal = float(input("Enter principal value: "))
annual_rate = float(input("Enter annual rate value: "))
time_in_years = float(input("Enter time in years value: "))

amount = principal * (1 + annual_rate) ** time_in_years
print("Amount: ", amount)