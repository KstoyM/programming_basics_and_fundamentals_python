def cast_spell_func(h_dict, h_name, mp_need, spell):
    hero_mp = h_dict[h_name][1]
    if hero_mp >= mp_need:
        hero_mp -= mp_need
        h_dict[h_name][1] -= mp_need
        print(f"{h_name} has successfully cast {spell} and now has {hero_mp} MP!")
    else:
        print(f"{h_name} does not have enough MP to cast {spell}!")
    return h_dict


def take_damage_func(h_dict, h_name, dmg, attacker_name):
    hero_hp = h_dict[h_name][0]
    if hero_hp > dmg:
        hero_hp -= dmg
        h_dict[h_name][0] -= dmg
        print(f"{h_name} was hit for {damage} HP by {attacker_name} and now has {hero_hp} HP left!")
    else:
        del h_dict[h_name]
        print(f"{h_name} has been killed by {attacker_name}!")
    return h_dict


def recharge_func(h_dict, h_name, recharge):
    hero_mp = h_dict[h_name][1]
    if hero_mp + recharge > 200:
        mp_need = 200 - hero_mp
        h_dict[h_name][1] = hero_mp + mp_need
        print(f"{h_name} recharged for {mp_need} MP!")
    else:
        hero_mp += recharge
        h_dict[h_name][1] += recharge
        print(f"{h_name} recharged for {recharge} MP!")
    return h_dict


def heal_func(h_dict, h_name, heal_amt):
    hero_hp = h_dict[h_name][0]
    if heal_amt + hero_hp > 100:
        hp_need = 100 - hero_hp
        h_dict[h_name][0] = hero_hp + hp_need
        print(f"{h_name} healed for {hp_need} HP!")
    else:
        hero_hp += heal_amt
        h_dict[h_name][0] += heal_amt
        print(f"{h_name} healed for {heal_amt} HP!")
    return h_dict


number_of_heroes = int(input())

heroes_dict = {}

for _ in range(number_of_heroes):
    hero_name, hp, mp = input().split(" ")
    heroes_dict[hero_name] = [int(hp), int(mp)]

while True:

    command = input().split(" - ")
    action = command[0]

    if action == 'End':
        for hero in heroes_dict:
            print(hero)
            print(f"  HP: {heroes_dict[hero][0]}")
            print(f"  MP: {heroes_dict[hero][1]}")
        break

    elif action == 'CastSpell':
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        heroes_dict = cast_spell_func(heroes_dict, hero_name, mp_needed, spell_name)

    elif action == 'TakeDamage':
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes_dict = take_damage_func(heroes_dict, hero_name, damage, attacker)

    elif action == 'Recharge':
        hero_name = command[1]
        recharge_amount = int(command[2])
        heroes_dict = recharge_func(heroes_dict, hero_name, recharge_amount)

    elif action == 'Heal':
        hero_name = command[1]
        heal = int(command[2])
        heroes_dict = heal_func(heroes_dict, hero_name, heal)