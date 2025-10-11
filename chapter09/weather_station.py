# WRITE YOUR SOLUTION HERE:

class WeatherStation:
    def __init__(self, name: str):
        if name != "":
            self.__name = name
        else:
            raise ValueError()
        
        self.__observation = []

    def add_observation(self, observation: str):
        self.__observation.append(observation)

    def latest_observation(self):
        if self.__observation == []:
            return ""
        else:
            return self.__observation[-1]

    def number_of_observations(self):
        return len(self.__observation)

    def __str__(self):
        return f"{self.__name}, {len(self.__observation)} observations"
