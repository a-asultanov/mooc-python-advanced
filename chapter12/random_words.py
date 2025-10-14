# Write your solution here:
import random

def word_generator(characters: str, length: int, amount: int):
    count = 1
    while count <= amount:
        i = 0
        rand_word = ""
        for i in range(length):
            rand_word += random.choice(characters)      
        yield rand_word
        count += 1