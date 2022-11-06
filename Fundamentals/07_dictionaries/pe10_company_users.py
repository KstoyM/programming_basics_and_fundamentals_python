companies = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break

    company_name, employee_id = command
    if company_name not in companies:
        companies[company_name] = []
    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

for company in companies.keys():
    print(company)
    for employee in companies[company]:
        print(f"-- {employee}")