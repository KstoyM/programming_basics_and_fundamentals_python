def flights(*args):
    flight_dict = {}

    for ind in range(0, len(args), 2):
        if ind + 1 < len(args):
            city = args[ind]
            people = args[ind + 1]
            if city == 'Finish' or people == 'Finish':
                break
            else:
                if city not in flight_dict:
                    flight_dict[city] = people
                else:
                    flight_dict[city] += int(people)
        else:
            break

    return flight_dict


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
