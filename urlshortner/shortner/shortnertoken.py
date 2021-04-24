import random
import string

class Shortnerclass:
    def __init__(self,token_size=None):
        self.token_size = token_size if token_size is not None else 5
    
    def generateToken(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(self.token_size))
