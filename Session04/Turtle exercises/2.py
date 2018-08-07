from turtle import *

speed(-1)
shape("classic")
color("blue")
pensize(1)

a = 56
b = 100
c = b / a

right(140)
for i in range (a):
    for k in range(4):
        forward(b)
        right(90)
    right(560/a)
    b -= c

exitonclick()
mainloop()
