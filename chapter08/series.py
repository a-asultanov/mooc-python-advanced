# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rating = 0
        self.rating_total = 0
        self.ratings_count = 0
    def __str__(self):
        ratings_ok = False
        if self.rating == 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\nno ratings"
        else:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {", ".join(self.genres)}\n{self.ratings_count} ratings, average {self.rating} points"

    def rate(self, rating: int):
        self.rating_total += rating
        self.ratings_count += 1
        self.rating = round(self.rating_total / self.ratings_count, 1)

    def get_rating(self):
        return self.rating

    def get_genres(self):
        return self.genres

def minimum_grade(grade: float, series: list):
    new_list = []
    for s in series:
        if s.get_rating() >= grade:
            new_list.append(s)
    return new_list

def includes_genre(genre: str, series: list):
    new_list = []
    for s in series:
        if genre in s.get_genres():
            new_list.append(s)
    return new_list
