import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
# print(f"Chosen word is: {chosen_word}")

lives = 6

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_game = False

while not end_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You've {lives} lives remaining...")
        if lives == 0:
            print("You lose......")
            end_game = True

    print(display)

    if "_" not in display:
        end_game = True
        print("You win!")