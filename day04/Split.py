import random

names_string = input("Enter everybody's name, separated by a comma: ")

names = names_string.split(",")
# print(names)

num_names = len(names)
random_choice = random.randint(0, num_names - 1)
# print(random_choice)

person_paying = names[random_choice]
print(f"{person_paying} is going to pay today!")

# SHORTCUT
# person_paying = random.choice(names)
# print(f"{person_paying} is going to pay today!")