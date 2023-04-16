print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad, where do you want to go? Type \"left\" or \"right\": ").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake, there's an island in the middle of the lake. Type \"wait\" to wait for a boat or type \"swim\" to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("you've arrived at the island unharmed. There's a house with 3 door. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3 == "yellow":
            print("Congratulations! You've found the treasure!")
        elif choice3 == "red":
            print("Sorry. It's a room full of beasts. Game over...")
        elif choice3 == "blue":
            print("Sorry. It's a room full of fire. Game over...")
        else:
            print("You chose a door that doesn't exist. Game over...")
    else:
        print("You got attacked by an angry trout. Game over...")
else:
    print("You fell into a hole. Game Over...")