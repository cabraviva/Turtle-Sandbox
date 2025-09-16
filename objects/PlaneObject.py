from objects import Object
class PlaneObject(Object):
    def __init__(self):
        super().__init__() # Init object base features
        self.add_hook(use_gravity(strength=2))