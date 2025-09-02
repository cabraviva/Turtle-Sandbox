import turtle as t

"""
Initializes window and turtle
returns (window, move)
"""
def init_screen():
    t.setup(2000, 1000)
    wn = t.Screen()
    wn.title('Turtle Sandbox')
    move = t.Turtle()
    t.showturtle()
    return (wn, move)