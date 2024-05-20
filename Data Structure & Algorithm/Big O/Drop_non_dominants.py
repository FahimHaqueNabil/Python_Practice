def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j) # O(n^2)

    for k in range(n):
        print(k) # O(n)

print_items(10)

# O(n^2) + O(n) -> O(n^2 + n) -> O(n^2)