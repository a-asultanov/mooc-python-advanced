# Write your solution here:
class Person:
    def __init__(self, name: str):
        self.name = name
  
      

    def return_first_name(self):
        first_name = self.name.split()

        return first_name[0]

    def return_last_name(self):

        last_name = self.name.split()

        return last_name[1]











