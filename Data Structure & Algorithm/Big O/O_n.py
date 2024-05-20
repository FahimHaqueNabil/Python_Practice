def print_items(n):
    for i in range(n): # O(n)
        print(i)
    for j in range(n): # O(n)
        print(j)

print_items(10)

# n + n -> 2n -> n -> O(n) [Drop constant]