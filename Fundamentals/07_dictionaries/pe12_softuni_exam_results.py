user_scores = {}
total_submissions = {}
banned_users = []

while True:
    command = input()
    if command == "exam finished":
        break

    if command.split("-")[1] == "banned":
        banned_users.append(command.split("-")[0])
        continue

    username, language, points = command.split("-")
    if username not in user_scores.keys():
        user_scores[username] = 0
    user_scores[username] = max(user_scores[username], int(points))

    if language not in total_submissions.keys():
        total_submissions[language] = 0
    total_submissions[language] += 1

print("Results:")
for name, score in user_scores.items():
    if name not in banned_users:
        print(f"{name} | {score}")
print("Submissions:")
for course in total_submissions.keys():
    print(f"{course} - {total_submissions[course]}")