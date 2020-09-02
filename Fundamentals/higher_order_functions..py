operations = {
  "average": lambda seq: sum(seq) / len(seq),
  "total": lambda seq: sum(seq),
  "top": lambda seq: max(seq)
}

students = [
  {'name': 'Rolf', 'grades': (67, 90, 95, 100)},
  {'name': 'Bob', 'grades': (64, 96, 93, 87)},
  {'name': 'Jen', 'grades': (62, 80, 55, 70)},
  {'name': 'Auba', 'grades': (90, 90, 90, 95)},
]

for student in students:
  name = student['name']
  grades = student['grades']

  print(f'Student: {name}')
  operation = input("Enter 'average', 'total' or 'top: ")

  result = operations[operation](grades)
  print(result)