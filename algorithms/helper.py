import random

def generate_list(n=10):
    """Generate random list of n unique integers from 1 to 100"""
    return random.sample(range(1, 101), n)

def get_target(arr):
    """Pick a random target value from the list"""
    return random.choice(arr)