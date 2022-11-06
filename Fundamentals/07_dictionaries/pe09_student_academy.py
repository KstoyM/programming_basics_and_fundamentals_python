school = {}

iterations = int(input())

for index in range(iterations):
    name = input()
    grade = float(input())

    if name not in school:
        school[name] = []
    school[name].append(grade)

for student in school.keys():
    average_grade = float(sum(school[student]) / len(school[student]))
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")