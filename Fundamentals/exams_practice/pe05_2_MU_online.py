def potion_func(hp, action_value):
    if hp + action_value <= 100:
        hp += action_value
        print(f'You healed for {action_value} hp.')
        print(f'Current health: {hp} hp.')
    else:
        healed_amount = 100 - hp
        hp = 100
        print(f'You healed for {healed_amount} hp.')
        print(f'Current health: {hp} hp.')
    return hp


def chest_func(btc, action_value):
    btc += action_value
    print(f"You found {action_value} bitcoins.")
    return btc


def monster_func(best_room, hp, monster_name, action_value):
    if hp - action_value <= 0:
        hp -= action_value
        print(f"You died! Killed by {monster_name}.")
        print(f"Best room: {best_room}")
    else:
        hp -= action_value
        print(f"You slayed {monster_name}.")
    return hp


health = 100
bitcoins = 0
current_room = 0
dungeon = input().split("|")
did_character_die = False

for element in dungeon:
    room_type, room_value = element.split()
    room_value = int(room_value)
    current_room += 1
    if room_type == 'potion':
        health = potion_func(health, room_value)
    elif room_type == 'chest':
        bitcoins = chest_func(bitcoins, room_value)
    else:
        health = monster_func(current_room, health, room_type, room_value)
        if health <= 0:
            did_character_die = True
            break

if not did_character_die:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
