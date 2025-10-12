# WRITE YOUR SOLUTION HERE:
import string

def most_common_words(filename: str, lower_limit: int):
    with open(filename, "r") as file:  
        no_punctuation = []
        content = file.read()
        words = content.split()
        no_punctuation += ["".join(ch for ch in word if ch not in string.punctuation) for word in words]
    
    words_count = {}
    words_dictionary = {}
    for word in no_punctuation:
        if word not in words_count:
            words_count[word] = 1
        else:
            words_count[word] += 1

    for word, count in words_count.items():
        if count >= lower_limit:
            words_dictionary[word] = count


    return words_dictionary