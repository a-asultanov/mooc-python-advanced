# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)
    
    def round_winner(self, p1_word, p2_word):
        if len(p1_word) == len(p2_word):
            pass
        elif len(p1_word) > len(p2_word):
            return 1
        else: 
            return 2

class MostVowels(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)
    
    def round_winner(self, p1_word, p2_word):
        vowels_list = ["a", "e", "i", "o", "u"]
        p1_vowels = []
        p2_vowels = []

        for i in p1_word:
            if i in vowels_list:
                p1_vowels.append(i)

        for i in p2_word:
            if i in vowels_list:
                p2_vowels.append(i)

        if len(p1_vowels) == len(p2_vowels):
            pass
        elif len(p1_vowels) > len(p2_vowels):
            return 1
        else: 
            return 2

class RockPaperScissors(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)
    def round_winner(self, p1_word, p2_word):
        options_list = ["rock", "paper", "scissors"]
        if p2_word not in options_list and p1_word not in options_list:
            pass 
            
        elif p2_word not in options_list:
            return 1
        elif p1_word not in options_list:
            return 2
        elif p1_word == p2_word:
            pass
        elif p1_word == "rock":
            if p2_word == "scissors":
                return 1
            elif p2_word == "paper":
                return 2
        elif p1_word == "scissors":
            if p2_word == "paper":
                return 1
            elif p2_word == "rock":
                return 2
        elif p1_word == "paper":
            if p2_word == "scissors":
                return 2
            elif p2_word == "rock":
                return 1
        else:
            pass