print("Welcome to the rollercoaster....")

height = int(input("Enter your height: "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Your ticket costs $12")
    elif age >= 12 and age <18:
        print("Your ticket costs $7")
    else:
        print("Your ticket costs $5")
else:
    print("Sorry... You're not tall enough...")