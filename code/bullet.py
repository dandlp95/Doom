from actor import Actor

class Bullet(Actor):
    def __init__(self):
        super().__init__()
        self._state = ""
    
    def set_state(self, state):
        self._state = state
    
    def get_state(self):
        return self._state        
    
    