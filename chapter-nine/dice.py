# Exercise 9-14: Dice
from random import randint

class Die():
    """Makes a dice class"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for _ in range(10):
            print(randint(1, self.sides))

        print('')

die_one = Die()
die_one.roll_die()

die_two = Die(10)
die_two.roll_die()

die_three = Die(20)
die_three.roll_die()