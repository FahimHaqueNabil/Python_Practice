import random

wordlist = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(wordlist)

lives = 6

# Testing code
print(f"Chosen word is: {chosen_word}")

# Creating unterstrich -> (_)
display = []
word_length = len(chosen_word)
for x in range(word_length):
    display += "_"
# print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Checking for guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You have {lives} life left.")
        if lives == 0:
            end_of_game = True
            print("You Lose!")


    if "_" not in display:
        end_of_game = True
        print("You win!")