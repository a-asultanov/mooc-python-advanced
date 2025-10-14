class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here
def most_goals(players: list):
    most_goals_scored = max(players, key=lambda player: player.goals)
    return most_goals_scored.name

def most_points(players: list):
    total_points = 0
    earned_most_points = None
    for player in players:
        if player.goals + player.passes > total_points:
            earned_most_points = (player.name, player.number)
            total_points = player.goals + player.passes
    return earned_most_points

def least_minutes(players: list):
    least_minutes_played = min(players, key=lambda player: player.minutes)
    return least_minutes_played