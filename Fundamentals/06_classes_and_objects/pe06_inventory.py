class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.for_decrease = capacity
        self.items = []

    def add_item(self, item: str):
        if self.for_decrease > 0:
            self.items.append(item)
            self.for_decrease -= 1
        return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.for_decrease}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
