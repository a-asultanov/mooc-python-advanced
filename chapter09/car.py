# WRITE YOUR SOLUTION HERE:

class Car:
    def __init__(self):
        self.__amount_of_petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__amount_of_petrol = 60    

    def drive(self, km:int):
        i = 0
        for i in range(km):
            if self.__amount_of_petrol > 0:
                self.__amount_of_petrol -= 1
                self.__odometer += 1
    
    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__amount_of_petrol} litres"