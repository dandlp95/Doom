class Actor:
    
    def  __init__(self):
        self._width = 0
        self._height = 0
        
        # Next 2 lines are position
        self._x = 0
        self._y = 0
        
        # This is velocity
        self._velocity = 0
        
        # Actions
        self._left = False
        self._right = False
        self._shooting = False
        self._hurting = False
        self._dying = False
        
    def set_left(self, is_moving):
        self._left = is_moving
    
    def set_right(self, is_moving):
        self._right = is_moving
    
    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y
    
    def set_velocity(self, velocity):
        self._velocity = velocity
    
    def set_width(self, width):
        self._width = width
    
    def set_height(self, height):
        self._height = height
    
    def get_height(self):
        return self._height

    def get_width(self):
        return self._width
        
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
    
    def get_velocity(self):
        return self._velocity
    
    def get_left(self):
        return self._left

    def get_right(self):
        return self._right
    
    
        
    
    
    
    
        
        