import random

names_string = input("Everybody's names, separated by a comma: ")
names = names_string.split(",")

# print(names)

num_person = len(names)

random_person = random.randint(0, num_person - 1)
person_pay = names[random_person]

print(f"{person_pay} will pay today!")

person_pay2 = random.choice(names)
print(f"{person_pay2} will pay next time")