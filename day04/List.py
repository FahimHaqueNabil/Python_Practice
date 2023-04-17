division_of_BD = ["Dhaka", "Chittagong", "Rangpur", "Rajshahi", "Barishal"]
print(division_of_BD)
print(division_of_BD[0])
print(division_of_BD[-2])

division_of_BD.append("Mymensingh")
print(division_of_BD)

division_of_BD.extend(["Sylhet", "Khulna"])
print(division_of_BD)

num_of_division = len(division_of_BD)
print(num_of_division)

# Dirty Dozen
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)