from actor import Actor

class Bullet(Actor):
    def __init__(self):
        super().__init__()
        self._state = ""
        self._image = "../media/bullet16.png"
    
    def set_state(self, state):
        self._state = state
    
    def get_state(self):
        return self._state        
    
    def get_image(self):
        return self._image
    
    def set_image(self, image):
        self._image = image
    
    