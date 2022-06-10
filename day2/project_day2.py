print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
to_be_payed = total_bill * (1 + tip/100) /num_people
print("Each person should pay: ${:.2f}".format(to_be_payed))