class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == 'fish':
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        else:
            result += f"Birds in {self.name}: {', '.join(self.birds)}"
        result += f"\nTotal animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count_of_animals = int(input())

for animal in range(count_of_animals):
    lst_input = input().split(" ")
    specie = lst_input[0]
    name_of_animal = lst_input[1]
    zoo.add_animal(specie, name_of_animal)

type_of_animal = input()
print(zoo.get_info(type_of_animal))

