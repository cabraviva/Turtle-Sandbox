import turtle as t
from objects import PlaneObject
from sprite import Sprite

# Start game
print("Initializing game")

t.setup(1500, 800)
wn = t.Screen()
wn.title('Turtle Sandbox')
move = t.Turtle()
# t.showturtle()

# Background option
# wn.bgcolor('lightblue')
wn.bgpic('./assets/background.gif')


# NOTE: Test for plane object
plane_obj = PlaneObject(wn)


# Mainloop
wn.mainloop()