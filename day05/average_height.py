student_heights = input("Enter a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(f"Student heights: {student_heights}")

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height: {total_height}")

total_students = 0
for student in student_heights:
    total_students += 1
print(f"Number of students: {total_students}")

avg = round(total_height/ total_students)
print(f"Average height: {avg}")

# total_height = sum(student_heights)
# num_of_students = len(student_heights)
# avg = round(total_height/ num_of_students)
# print(f"Average height: {avg}")

