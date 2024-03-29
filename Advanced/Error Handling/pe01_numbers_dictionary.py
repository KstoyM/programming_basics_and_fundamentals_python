numbers_dictionary = {}

line = input()

while line != "Search":

    try:
        number_as_string = line
        numbers_dictionary[number_as_string] = int(input())
    except ValueError:
        print('The variable number must be an integer')

    line = input()

line = input()
while line != "Remove":

    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')

    line = input()

line = input()
while line != "End":

    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print('Number does not exist in dictionary')

    line = input()

print(numbers_dictionary)
