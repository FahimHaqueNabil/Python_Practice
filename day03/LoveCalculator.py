print("Welcome to Love Calculator!")

name1 = input("What's your name?: ")
name2 = input("What's his/her name? ")

combined_name = name1 + name2
combined_lowered_name = combined_name.lower()

t = combined_lowered_name.count("t")
r = combined_lowered_name.count("r")
u = combined_lowered_name.count("u")
e = combined_lowered_name.count("e")
true = t + r + u + e
# print(true)

l = combined_lowered_name.count("l")
o = combined_lowered_name.count("o")
v = combined_lowered_name.count("v")
e = combined_lowered_name.count("e")
love = l + o + v + e
# print(love)

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go like coke and mentos!")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together!")
else:
    print(f"Your love score is {love_score}.")