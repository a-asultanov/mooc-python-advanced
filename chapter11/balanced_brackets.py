
def balanced_brackets(my_string: str):
    brackets = ["(", ")", "[", "]"]
    new_string = ""
    for ch in my_string:
        if ch in brackets:
            new_string += ch
    if len(new_string) == 0:
        return True
    if not (new_string[0] == '(' and new_string[-1] == ')' or new_string[0] == '[' and new_string[-1] == ']'):
        return False

    # remove first and last character
    return balanced_brackets(new_string[1:-1])