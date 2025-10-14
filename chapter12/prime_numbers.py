# Write your solution here
def prime_numbers():
    number = 2
    def is_prime(n):
            if n < 2:
                return False

            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
    while True:
        if is_prime(number):
            yield number
        number += 1
            
    
