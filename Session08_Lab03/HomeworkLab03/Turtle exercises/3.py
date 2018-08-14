import turtle as t

def draw_Square(length,Color):

    for i in range(4):
        t.color(Color)
        t.forward(length)
        t.right(90)

draw_Square(200,"blue")