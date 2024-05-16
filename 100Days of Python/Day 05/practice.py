student_heights = input("Input a list of student heights: ").split()
total_height = 0
count = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

for height in student_heights:
    total_height += height
    count += 1

# print(f"Total height: {total_height}")

avg_height = total_height/count

print(f"Average height is: {avg_height}")