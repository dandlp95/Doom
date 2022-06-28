from actor import Actor

class Enemy(Actor):
    
    def __init__(self):
        super().__init__()
        self._lives = 0
        # Left 
        self._image_l = "../media/enemy/L2.png"
        self._attack_l_img = "../media/enemy/attack.png"
        self._walk_left = ["../media/enemy/L1.png", "../media/enemy/L2.png", "../media/enemy/L3.png", "../media/enemy/L4.png", "../media/enemy/L1.png", "../media/enemy/L2.png", "../media/enemy/L3.png", "../media/enemy/L4.png", "../media/enemy/L1.png"]
        # Right
        self._image_r = "../media/enemy/R2.png"
        self._attack_r_img = "../media/enemy/r-attack.png"
        self._walk_right = ["../media/enemy/R1.png", "../media/enemy/R2.png", "../media/enemy/R3.png", "../media/enemy/R4.png"]
        self._last_direction = ""
        
        
    def set_lives(self, lives):
        self._lives = lives

    def get_lives(self):
        return self._lives
    
    def is_shooting(self, is_shooting):
        return is_shooting
    
    def set_last_direction(self, last_direction):
        self._last_direction = last_direction
    
    def get_walkRight_animation(self):
        return self._walk_right
    
    def get_walkLeft_animation(self):
        return self._walk_left
    
    def get_image_l(self):
        return self._image_l
    
    def get_image_r(self):
        return self._image_r
    
    def get_last_direction(self):
        return self._last_direction
    
    def get_img_attack_r(self):
        return self._attack_r_img
    
    def get_img_attack_l(self):
        return self._attack_l_img
    
    
    
        
        