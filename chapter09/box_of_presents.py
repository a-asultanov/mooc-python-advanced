# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

class Box:
    def __init__(self):
        self.presents = []

    def add_present(self, present: Present):
        self.presents.append(present)
    
    def total_weight(self):
        box_total_weight = 0
        
        for present in self.presents:
            box_total_weight += present.weight

        return box_total_weight
        

