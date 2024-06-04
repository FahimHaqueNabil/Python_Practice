import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"Chosen word is: {chosen_word}")

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")