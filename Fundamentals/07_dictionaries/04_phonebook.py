phonebook = {}

command = input().split("-")

while len(command) > 1:

    person, number = command

    phonebook[person] = number

    command = input().split("-")

for i in range(int(command[0])):
    search_name = input()
    if search_name not in phonebook:
        print(f"Contact {search_name} does not exist.")
    else:
        print(f"{search_name} -> {phonebook[search_name]}")