student = {}

student['name'] = str(input("Name: "))
student['average'] = float(input(f"Average grade of {student['name']}: "))

if student['average'] >= 7:
    student['status'] = 'Approved'
elif 5 <= student['average'] < 7:
    student['status'] = 'Recovery'
else:
    student['status'] = 'Failed'

for k, v in student.items():
    print(f"{k} is {v}")
