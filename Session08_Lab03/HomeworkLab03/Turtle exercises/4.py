import turtle as t


def draw_Square(length,Color):
  
    for i in range(4):
        t.color(Color)
        t.forward(length)
        t.left(90)

draw_Square(200,"blue")

for i in range(30):
    draw_Square(i * 5, 'red')
    t.left(17)
    t.penup()
    t.forward(i * 2)
    t.pendown()