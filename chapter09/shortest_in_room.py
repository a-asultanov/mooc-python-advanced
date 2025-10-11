# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []


    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        
        if self.persons == []:
            return True
        else:
            return False

    def print_contents(self):

        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if self.persons == []:
            return None
        else:
            shortking = self.persons[0]
            for person in self.persons:
                if person.height < shortking.height:
                    shortking = person
            return shortking

    def remove_shortest(self):
        if self.persons == []:
            return None
        else:
            shortking = self.shortest()
            self.persons.remove(shortking)
            return shortking