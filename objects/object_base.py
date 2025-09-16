# This is the base class for all other objects to inherit from
# For an example, see ./PlaneObject.py
class Object:
    def __init__(self, sprite):
        self.sprite = sprite

    def add_hook(self, hook_fn):
        """
        Applies a hook to the object
        """
        # Applies a hook (like use_gravity())
        hook_fn(self)