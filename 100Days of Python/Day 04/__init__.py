import random
import my_module

random_integer = random.randint(1, 6)
print(random_integer)

print(my_module.pi)

# 0.00000000 - 0.999999999......
random_float = random.random()
print(random_float)

# 0.0000000 - 4.99999999
print(random_float * 5)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")