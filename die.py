from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self, rolls=1):
        results = [randint(1, self.sides) for _ in range(rolls)]
        return results

my_roll = Die(6)
print(my_roll.roll_dice(10))