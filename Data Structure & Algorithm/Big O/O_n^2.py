def print_items(n):
    for i in range(n): # O(n)
        for j in range(n): # O(n)
            for k in range(n): # O(n)
                print(i, j, k)

print_items(10)

# n * n = n^2 = O(n^2)
# n * n * n = n^3 = n^2 = O(n^2) [Simplify]