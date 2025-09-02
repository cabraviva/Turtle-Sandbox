import turtle as t
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

sprite = Sprite(wn, "./assets/plane.gif", x=0, y=0)
sprite_bombe = Sprite(wn, "./assets/bomber.gif", x=0, y=0)
# Move instantly
sprite.move_to(100, 100)

# Move smoothly over 2 seconds
sprite.move_to_animated(-100, -100, duration=2)

# Mainloop
wn.mainloop()