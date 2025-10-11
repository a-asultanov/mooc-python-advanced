# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
   
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def to_days(self):
        return self.day + self.month * 30 + self.year * 360


    def __eq__(self, another):
        if not isinstance(another, SimpleDate):
            return False
        return self.to_days() == another.to_days()


    def __ne__(self, another):
        if not isinstance(another, SimpleDate):
            return False
        return self.to_days() != another.to_days()

    def __gt__(self, another):
        if not isinstance(another, SimpleDate):
            return False
        return self.to_days() > another.to_days()

    def __lt__(self, another):
        if not isinstance(another, SimpleDate):
            return False
        return self.to_days() < another.to_days()

    def __add__(self, days_to_add):
        total_current_days = self.to_days()
        new_total_days = total_current_days + days_to_add
        years = new_total_days // 360
        days_left = new_total_days % 360
        months = days_left // 30
        days = days_left % 30

        return SimpleDate(days, months, years)

    def __sub__(self, another):
        new_total_days = self.to_days() - another.to_days()

        return abs(new_total_days)
    