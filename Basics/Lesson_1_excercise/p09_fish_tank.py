#Read Input

length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percent = float(input())

#Process_Input

volume_of_aquarium_in_cubic_cm = length_in_cm * width_in_cm * height_in_cm
volume_of_aquarium_in_cubic_dm = volume_of_aquarium_in_cubic_cm / 1000
liters_of_water_necessary_to_fill_the_aquarium = volume_of_aquarium_in_cubic_dm - volume_of_aquarium_in_cubic_dm * percent / 100

#Print_output

print(liters_of_water_necessary_to_fill_the_aquarium)