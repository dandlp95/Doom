from actor import Actor

class Player(Actor):

    def __init__(self):
        super().__init__()
        self._lives = 0
        #self._image = '../media/player/standing.png'
        self._image = "../media/player/doom-guy.png"
        self._walk_right = ['../media/player/R1.png', '../media/player/R2.png', '../media/player/R3.png', '../media/player/R4.png', '../media/player/R5.png', '../media/player/R6.png', '../media/player/R7.png', '../media/player/R8.png', '../media/player/R9.png']
        self._walk_left = ['../media/player/L1.png', '../media/player/L2.png', '../media/player/L3.png', '../media/player/L4.png', '../media/player/L5.png', '../media/player/L6.png', '../media/player/L7.png', '../media/player/L8.png', '../media/player/L9.png']
        

    def set_lives(self, lives):
        self._lives = lives

    def get_lives(self, lives):
        return self._lives
    
    def is_shooting(self, is_shooting):
        return is_shooting
    
    def get_walkRight_animation(self):
        return self._walk_right
    
    def get_walkLeft_animation(self):
        return self._walk_left
    
    def get_image(self):
        return self._image
