from hooks.use_gravity import use_gravity
from objects import Object
from sprite import Sprite

class PlaneObject(Object):
    def __init__(self, window):

        super().__init__(
            Sprite(window, "./assets/plane.gif", x=0, y=0) # Base Sprite
        ) # Init object base features

        # Hooks
        self.add_hook(use_gravity(strength=2))