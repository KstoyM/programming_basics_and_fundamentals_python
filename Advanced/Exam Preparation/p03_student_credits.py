def students_credits(*args):
    courses_dict = {}
    for arg in args:
        course_name, cred, max_test_points, diyan_points = arg.split('-')
        cred_per_point = int(cred) / int(max_test_points)
        diyan_curr_cred = int(diyan_points) * cred_per_point
        courses_dict[course_name] = diyan_curr_cred

    total_credits = sum(courses_dict.values())

    if total_credits >= credits_needed:
        print(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        print(f"Diyan needs {credits_needed - total_credits:.1f} credits more for a diploma.")

    for k, v in sorted(courses_dict.items()):
        print(f"{k} - {v:.1f}")


credits_needed = 240

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
