# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self, name: str, acc_number: str, balance: float):
        self.__name = name
        self.__acc_number = acc_number
        self.__balance = balance

    
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()
        else:
            raise ValueError()
    
    def withdraw(self, amount: float):
        if amount > 0:
            self.__balance -= amount
            self.__service_charge()
        else:
            raise ValueError()

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance = self.__balance * 0.99

