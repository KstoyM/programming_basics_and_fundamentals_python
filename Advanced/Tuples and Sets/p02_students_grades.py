students = {}

for i in range(int(input())):
    student, score = input().split(" ")
    if student not in students:
        students[student] = []
    students[student].append(float(score))

for k, v in students.items():
    average_score = sum(v) / len(v)
    grades_to_string = " ".join(map(lambda grade: f'{grade:.2f}', v))
    print(f"{k} -> {grades_to_string} (avg: {average_score:.2f})")