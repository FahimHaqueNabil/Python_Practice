states_USA = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia"]
print(states_USA)
print(states_USA[-1])

states_USA[1] = "Pencilvania"
print(states_USA)

states_USA.append("New York")
print(states_USA)

states_USA.extend(["Nabil Land", "Sama Land"])
print(states_USA)

# print(states_USA[13])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)