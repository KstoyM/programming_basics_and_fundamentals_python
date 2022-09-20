height_of_the_house = float(input())
length_of_the_house = float(input())
height_of_the_roof = float(input())

area_of_square_wall = height_of_the_house * height_of_the_house
area_of_rectangle_wall = length_of_the_house * height_of_the_house
area_of_right_angle_triangle = height_of_the_house * height_of_the_roof * 1/2
area_of_the_rectangular_roof = length_of_the_house * height_of_the_house

area_of_wall_with_door = area_of_square_wall - 1.2 * 2
area_of_walls_with_window = area_of_rectangle_wall - 1.5 * 1.5

area_of_the_house = area_of_wall_with_door + area_of_square_wall + area_of_walls_with_window * 2
area_of_the_roof = area_of_right_angle_triangle * 2 + area_of_the_rectangular_roof * 2

liters_of_green_paint_needed = area_of_the_house / 3.4
liters_of_red_paint_needed = area_of_the_roof / 4.3

print(f'{liters_of_green_paint_needed:.2f}')
print(f'{liters_of_red_paint_needed:.2f}')
