class Party:

    people = []


while True:
    command = input()

    if command == "End":
        break

    Party.people.append(command)

print(f"Going: {', '.join(Party.people)}")
print(f"Total: {len(Party.people)}")