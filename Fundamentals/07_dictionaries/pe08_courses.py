school = {}

while True:
    command = input().split(" : ")

    if command[0] == "end":
        break

    course_name, student_name = command

    if course_name not in school:
        school[course_name] = []
    school[course_name].append(student_name)

for course in school.keys():
    print(f"{course}: {len(school[course])}")
    for name in school[course]:
        print(f"-- {name}")