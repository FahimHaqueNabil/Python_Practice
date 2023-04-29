total_even = 0
total_odd = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_even += number
    else:
        total_odd += number

print(f"Total of Even Numbers from 1 to 100: {total_even}")
print(f"Total of Odd Numbers from 1 to 100: {total_odd}")