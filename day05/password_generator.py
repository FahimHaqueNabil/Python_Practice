import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy -> input = 4 2 2 -> output = qbFD~!15
password_easy = ""
for char in range(1, nr_letters + 1):
    password_easy += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password_easy += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_easy += random.choice(numbers)

print(f"Easy Password: {password_easy}")


# Hard -> input = 4 2 2 -> output = q<Ye58F?
password_hard = []
for char in range(1, nr_letters + 1):
    password_hard.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_hard.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_hard.append(random.choice(numbers))

random.shuffle(password_hard)
password = ""
for char in password_hard:
    password += char
print(f"Hard Password: {password}")