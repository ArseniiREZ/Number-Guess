import random

class Game:
    def __init__(self):
        self.number = random.randint(1,6)
        self.attempts = 5
    def guess(self, number):
        self.attempts -= 1
        if number == self.number:
            return "You guessed the number!"
        elif number > self.number:
            return "Too high!"
        elif number < self.number:
            return "Too low!"
        return None
