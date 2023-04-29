fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits)

# print(fruits)

for number in range(1, 11):
    print(number)

for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(f"Sum of 1 to 100: {total}")