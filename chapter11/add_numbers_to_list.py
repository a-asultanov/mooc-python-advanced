# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list): 
    if len(numbers) % 5 == 0:
        return
    else:
        i = numbers[-1] + 1
        numbers.append(i)
    add_numbers_to_list(numbers)
