import math


def is_it_prime(n):
    if n <= 1: 
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    limit = int(math.sqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_prime():
    try:
        n = int(input("Enter a integer: "))
        result = "It's prime" if is_it_prime(n) else "It's not prime"
        print(f"{result}!")
    except ValueError:
        print("Please enter a valid integer.")

check_prime()
