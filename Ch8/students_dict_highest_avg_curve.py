
# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Colin': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Mary': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}
sum_scores = 0
highest_score_student = ''
assignments_totals = [0,0,0,0,0]

for st, scores in student_grades.items():
    for idx, score in enumerate(scores):
        assignments_totals[idx] += score

    print(st, "has", sum(scores), "total points.")
    if (sum_scores < sum(scores)):
        sum_scores = sum(scores)
        highest_score_student = st
print("Student:", highest_score_student, "has", sum_scores, "total points.")

print("Curve Grades...")
for st, sc in student_grades.items():
    print("Student {} has a curve grade of {:.2f}%.".format(st, (sum(sc)/sum_scores)*100))

for idx, grade in enumerate(assignments_totals):
    print("assignment", idx+1, "total:", grade, "and avg:", grade/5)
