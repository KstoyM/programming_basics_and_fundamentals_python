def grader(rec_grade):
    if 2 <= rec_grade < 3:
        return "Fail"
    elif 3 <= rec_grade < 3.50:
        return "Poor"
    elif 3.50 <= rec_grade <= 4.49:
        return "Good"
    elif 4.50 <= rec_grade < 5.50:
        return "Very Good"
    return "Excellent"


grade = float(input())

print(grader(grade))
