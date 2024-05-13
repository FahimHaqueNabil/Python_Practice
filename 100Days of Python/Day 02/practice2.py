age = input("What is your current age?\n")

age_int = int(age)

years_remaining = 90 - age_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days or {weeks_remaining} weeks or {months_remaining} months remaining...")