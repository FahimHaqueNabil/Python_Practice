import random

wordlist = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(wordlist)

# Testing code
print(f"Chosen word is: {chosen_word}")

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")