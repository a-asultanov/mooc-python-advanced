# Write your solution here:

class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def weight(self):
        return self.__weight

    def name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"         

class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.current_weight = 0
        self.items = []

    def add_item(self, item: Item):
        if self.current_weight + item.weight() <= self.max_weight:
            self.current_weight += item.weight()
            self.items.append(item)
        else:
            pass
    def weight(self):
        return self.current_weight

    def __str__(self):

        
        if len(self.items) == 1:
            return f"{len(self.items)} item ({self.current_weight} kg)"
        else:
            return f"{len(self.items)} items ({self.current_weight} kg)"


    def print_items(self):
        for item in self.items:
            print(item)

    def heaviest_item(self):
        current_heaviest = self.items[0]
        for item in self.items:
            if item.weight() > current_heaviest.weight():
                current_heaviest = item
        return current_heaviest

class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.suitcases = []

    def add_suitcase(self, suitcase):
        current_max_weight = 0
        for item in self.suitcases:
            current_max_weight += item.current_weight
        
        if current_max_weight + suitcase.current_weight <= self.max_weight:
            self.suitcases.append(suitcase)
    
    def __str__(self):
        current_weight = 0
        for suitcase in self.suitcases:
            current_weight += suitcase.current_weight

        if len(self.suitcases) == 1:
            return f"{len(self.suitcases)} suitcase, space for {self.max_weight - current_weight} kg"
        else:
            return f"{len(self.suitcases)} suitcases, space for {self.max_weight - current_weight} kg"

    def print_items(self):
        for suitcase in self.suitcases:
            for item in suitcase.items:
                print(f"{item.name()} ({item.weight()} kg)")