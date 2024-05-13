print("Welcome to the treasure island......")
print("Your mission is to find the treasure....")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right": ').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There\'s an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross: ').lower()
    if choice2 == "wait":
        choice3 = input("You've at the island unharmed. There's a house with 3 doors: Red, Yellow, Blue. Which one do you choose?: ").lower()
        if choice3 == "red":
            print("It's a room of fire. Game Over.")
        elif choice3 == "yellow":
            print("Congratulations! You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You entered a room of beasts. Game Over.")
    else:
        print("You got attacked by a shark. Game Over.")
else:
    print("You fell into a hole. Game Over.")