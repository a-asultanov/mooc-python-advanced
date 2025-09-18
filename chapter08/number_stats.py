# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.numbers_added = 0

    def add_number(self, number:int):
        self.numbers += number
        self.numbers_added += 1

    def count_numbers(self):

        return self.numbers_added


    def get_sum(self):
        if self.numbers > 0:
            return self.numbers
        else:
            return 0
    
    def average(self):
        if self.numbers > 0:
            return self.numbers / self.numbers_added
        else:
            return 0

stats = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()
while True:
    user_input = int(input("Please type in integer numbers: "))
    if user_input == -1:
        break
    stats.add_number(user_input)
    if user_input % 2 == 0:
        even_numbers.add_number(user_input)
    else:
        odd_numbers.add_number(user_input)

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {even_numbers.get_sum()}")
print(f"Sum of odd numbers: {odd_numbers.get_sum()}")


