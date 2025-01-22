# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again."}

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# student_grades = #new dict with key names + assessesd grades as values
student_grades = {}
print(student_grades)

for key in student_scores:
    if student_scores[key] <= 70:
        student_grades[key] = "Fail"
        print(key, student_grades[key])
    elif student_scores[key] > 70 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
        print(key, student_grades[key])
    elif student_scores[key] > 81 and student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
        print(key, student_grades[key])
    else:
        student_grades[key] = "Outstanding"
        print(key, student_grades[key])

print(student_grades)