# WRITE YOUR SOLUTION HERE:
def begin_with_vowel(words: list):
    return [word for word in words if word[0].lower() in ["a", "e", "i", "o", "u"]]

def filter_forbidden(string: str, forbidden: str):
    return "".join(character for character in string if character not in forbidden) 