# WRITE YOUR SOLUTION HERE:
class ListHelper:
    
    @classmethod
    def greatest_frequency(self, my_list: list):
        frequency = {}
        most_common_count = 0
        most_common = None
        for item in my_list:
            if item not in frequency:
                frequency[item] = 1
            else:
                frequency[item] += 1
        
        for key, value in frequency.items():
            if value > most_common_count:
                most_common_count = value
                most_common = key
            
        return most_common
    
    @classmethod
    def doubles(self, my_list: list):
        frequency = {}
        number_unique = 0

        for item in my_list:
            if item not in frequency:
                frequency[item] = 1
            else:
                frequency[item] += 1

        for key, value in frequency.items():
            if value >= 2:
                number_unique += 1

        return number_unique