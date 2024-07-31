# Dictionaries

my_dict = {
    "name": "Dileep",
    "age": 23,
    "occupation": "student",
}

print(my_dict["name"])
my_dict["address"] = "1001 S Center ST"
my_dict["city"] = "Arlington"

# Grading problem
"""
Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"
"""
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for i in student_scores.keys():
  if student_scores[i] > 90 and student_scores[i] <= 100:
    student_grades[i] = "Outstanding"
  elif student_scores[i] > 80 and student_scores[i] <= 90:
    student_grades[i] = "Exceeds Expectations"
  elif student_scores[i] > 70 and student_scores[i] <= 80:
    student_grades[i] = "Acceptable"
  else:
    student_grades[i] = "Fail"
print(student_grades)

