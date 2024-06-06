def greet():
    print("Hello...")
    print("Welcome to function..")
greet()

print()
def greet(name):
    print(f"Hello {name}...")
    print(f"{name}, Welcome to function..")
greet("Nabil")

print()
def greets(name, location):
    print(f"Hello {name}!")
    print(f"How's the weather in {location}?")
greets("Nabil", "Saidpur")
print()
greets(location="Bangladesh", name="Fahim")