# Given a list of dictionaries
# (e.g., [{'name': 'Alice', 'marks': 25}, ...]),
# use sorted() with a lambda to sort by marks.

students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Ahmed", "marks": 75},
]

sortStudents = sorted(students, key=lambda s: s["marks"])

print(sortStudents)
