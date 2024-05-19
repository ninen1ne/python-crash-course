# 10/5/2024
import random

class Die():
    """Try to model a dice which can be rolled."""
    
    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """"""
        return random.randint(1, self.sides)
    
d6 = Die()
results = []

for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)

print('\n10 rolls of a 6 sided die:')
print(results)

d10 = Die(sides=10)
results = []

for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)

print('\n10 rolls of a 10 sided die:')
print(results)

d20 = Die(20)
results = []

for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)

print('\n10 rolls of a 20 sided die:')
print(results)