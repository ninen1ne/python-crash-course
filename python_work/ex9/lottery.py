# 11/5/2024
from random import choice

class Lottery():
    """model function for behavior of lottery. :D"""

    def __init__(self):
        """Initialize attribute for lottery class."""
        self.posibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
        self.prize = []
        self.ticket = []

    def make_prize(self):
        """Generate prize ticket with the 4 element."""
        while len(self.prize) < 4:
            pull_item = choice(self.posibilities)
            if pull_item not in self.prize:
                self.prize.append(pull_item)

    def generate_ticket(self):
        """Generate my own ticket."""
        while len(self.ticket) < 4:
            pull_item = choice(self.posibilities)
            if pull_item not in self.ticket:
                self.ticket.append(pull_item)


    def check_ticket(self):
        """Check if ticket match prize ticket."""
        for element in self.ticket:
            if element not in self.prize:
                return False
            
        return True
    


winning_ticket = Lottery()
winning_ticket.make_prize()
print(f'the winning code is: {winning_ticket.prize}!!!')
won_code = winning_ticket.prize

won = False
count = 0
max_tries = 10_000

while not won:
    my_ticket = Lottery()
    my_ticket.prize = won_code
    my_ticket.generate_ticket()
    print(my_ticket.ticket)
    won = my_ticket.check_ticket()
    count += 1 
    if count >= max_tries:
        break

if won:
    print('We have a winning ticket!!!')
    print(my_ticket.ticket)
    print(f'It only took {count} tries to win')
else:
    print(f"Tried {count} times, without pulling a winner. :(")
    print(f"Your ticket: {my_ticket.ticket}")
    print(f"Winning ticket: {won_code}")
