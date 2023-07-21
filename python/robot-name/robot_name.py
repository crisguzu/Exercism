import random
import string

class Robot:

    def __init__(self):
        seed = random.choice(string.ascii_uppercase)
        self.name = ''
        for i in range(5):
            if i < 2:
                self.name += random.choice(string.ascii_uppercase)
            else:
                self.name += random.choice(string.digits)
                
    def reset(self):
        self.name = ''
        for i in range(5):
            if i < 2:
                self.name += random.choice(string.ascii_uppercase)
            else:
                self.name += random.choice(string.digits)
