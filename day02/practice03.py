height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

BMI = float(weight) / float(height) ** 2

print(BMI)
print(int(BMI))

print(round(BMI))
print(round(BMI, 2))