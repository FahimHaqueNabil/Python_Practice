print("Welcome to the rollercoaster....")

height = int(input("Enter your height: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age >= 18:
        bill = 12
        print("Adult tickets are $12")
    elif age >= 12 and age <18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 5
        print("Child tickets are $5")

    photo = input("Do you want a photo taken? Y or N: ")

    if photo == "Y" or photo == 'y':
        bill += 3

    print(f"Your final bill ${bill}")

else:
    print("Sorry... You're not tall enough...")