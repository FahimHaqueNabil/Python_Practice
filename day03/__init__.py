print("Welcome to the Roller Coaster!")
height = int(input("What's your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the Roller Coaster!")
    age = int(input("What's your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    # Add extra bill for photo
    photo = input("Do you want a photo taken? Y or N: ")
    if photo == "Y":
        bill += 3

    print(f"Your final bill is: ${bill}")


else:
    print("Sorry, you've to grow taller before you can ride...")