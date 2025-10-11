# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"


    def __eq__(self, another):
        if not isinstance(another, Money):
            return False
        return self._euros == another._euros and self._cents == another._cents

    def __gt__(self, another):
        if not isinstance(another, Money):
            return False
        total_self = self._euros * 100 + self._cents
        total_another = another._euros * 100 + another._cents

        return total_self > total_another

    def __add__(self, another):
        if not isinstance(another, Money):
            return False

        total_eur = (self._euros + another._euros)
        total_cents = (self._cents + another._cents)

        if total_cents >= 100:
            total_eur += total_cents // 100
            total_cents = total_cents % 100

        return Money(total_eur, total_cents)

    def __sub__(self, another):
        if not isinstance(another, Money):
            return False
        euros = 0
        cents = 0
        total_eur = (self._euros - another._euros)
        total_cents = (self._cents - another._cents)
        
        total_self_cents = self._euros * 100 + self._cents
        another_cents = another._euros * 100 + another._cents
        result_cents = total_self_cents - another_cents
            
        if result_cents < 0:
            raise ValueError()

        else:
            euros = result_cents // 100
            cents = result_cents % 100
         
            
            
        return Money(euros, cents)