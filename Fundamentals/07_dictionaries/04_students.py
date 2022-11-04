students = {}

while True:

    command = input().split(":")

    if len(command) == 1:
        break

    name, ident, course = command
    if course not in students.keys():
        students[course] = []
    students[course].append(f'{name} - {ident}')

command = command[0].replace("_", " ")

for student in students[command]:
    print(student)
