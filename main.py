import turtle
t=turtle.Turtle()
t.screen.bgcolor("yellow")
t.speed(2000000)
t.color('grey')
t.pensize(2)

c=0
d=0
while True:
    for i in range(4):
        t.forward(80)
        t.right(90)
    t.right(15)
    c=c+1
    if c>= 390/15:
        t.forward(50)
        c=0
        d=d+1
        if d>=12:
            break
t.hideturtle()
turtle.done()

