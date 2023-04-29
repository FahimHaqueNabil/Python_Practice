student_scores = input("Enter a list of student scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(f"Student scores: {student_scores}")

maximum_score = student_scores[0]
for score in student_scores:
    if score > maximum_score:
        maximum_score = score

print(f"Maximum score: {maximum_score}")

minimum_score = student_scores[0]
for score in student_scores:
    if score < minimum_score:
        minimum_score = score

print(f"Minimum score: {minimum_score}")

# print(f"Maximum scores: {max(student_scores)}")
# print(f"Minimum scores: {min(student_scores)}")