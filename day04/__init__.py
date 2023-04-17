import random

random_integer = random.randint(1,100)
print(random_integer)

# 0.0000000.... - 0.9999999...
random_float = random.random()
print(random_float)

# 0 - 5
random_float = (random_float * 5) + 1
print(int(random_float))

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")