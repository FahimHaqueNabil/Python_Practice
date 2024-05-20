# NOt using POINTERS
num1 = 11
num2 = num1

print("Before value is updated..........")
print(f"Num 1: {num1}")
print(f"Num 2: {num2}")

num1 = 22
print("After value is updated..........")
print(f"Num 1: {num1}")
print(f"Num 2: {num2}")

# Using POINTERS
dict1 = {
    'value' : 11
}

dict2 = dict1

print("Before value is updated..........")
print(f"dict 1: {dict1}")
print(f"dict 2: {dict2}")

dict1['value'] = 22

print("After value is updated..........")
print(f"dict 1: {dict1}")
print(f"dict 2: {dict2}")

dict3 = dict2
print(f"dict 3: {dict3}")