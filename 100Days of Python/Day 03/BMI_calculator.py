height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)
bmi_round = round(bmi, 1)

print(f"Your BMI is: {bmi_round}")

if bmi_round < 18.5:
    print("You're underweight")
elif bmi_round >= 18.5 and bmi_round < 25:
    print("You've normal weight")
elif bmi_round >= 25 and bmi_round < 30:
    print("You're overweight")
elif bmi_round >= 30 and bmi_round < 35:
    print("You're obese")
else:
    print("You're clinically obese")