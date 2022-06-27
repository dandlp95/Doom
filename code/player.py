from actor import Actor

class Player(Actor):

    def __init__(self):
        super().__init__()
        self._lives = 0

    def set_lives(self, lives):
        self._lives = lives

    def get_lives(self, lives):
        return self._lives
    
    def is_shooting(self, is_shooting):
        return is_shooting
