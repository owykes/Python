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

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a number (or 0 to exit): "))
            if num == 0:
                break
            print(f"{num} is prime? {is_it_prime(num)}")
        except ValueError:
            print("Please enter a valid integer.")