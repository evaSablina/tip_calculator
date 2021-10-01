print("Welcome to the tip calculator.")

total_bill = float(input("What was  the total bill? £"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

pay = (total_bill + (total_bill * (percentage / 100))) / people
final_amount = round(pay, 2)
final_amount = "{:.2f}".format(pay)

print(f"Each person should pay: £{final_amount}")
