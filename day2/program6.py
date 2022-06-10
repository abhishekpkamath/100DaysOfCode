age = int(input("Enter your age: "))
age_in_days = 90 * 365 - age * 365
age_in_weeks = 90 * 52 - age * 52
age_in_months = 90 * 12 - age * 12
print(f"You have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left.")