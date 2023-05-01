def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today?")
greet("Nabil")
greet("Hitman")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the weather nice today in {location}?")
greet_with("Nabil", "Dhaka")
greet_with(location="Saidpur", name="Hitman")