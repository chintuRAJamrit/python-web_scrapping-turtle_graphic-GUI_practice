import turtle

def shape(t,x1,y1,x2,y2,depth):
    if depth == 0:
        t.penup()
        t.goto(x1,y1)
        t.pendown()
        t.goto(x2,y2)

    else:
        xa = x1 + (x2 - x1) / 3
        ya = y1 + (y2 - y1) / 3
        xb = x1 + 2 * (x2 - x1) / 3
        yb = y1 + 2*(y2 - y1 ) / 3
        xc = (x1 + x2) / 2 - (y2 - y1)*(3 ** 0.5)/6
        yc = (y1+y2) / 2 + (x2 - x1)*(3 ** 0.5 )/6

        shape(t,x1,y1,xa,ya,depth-1)
        shape(t,xa,ya,xc,yc,depth-1)
        shape(t,xc,yc,xb,yb,depth-1)
        shape(t,xb,yb,x2,y2,depth-1)

t = turtle.Turtle()
t.speed(0)

depth =2
size = 300
x1 = -size/2
y1 = size *(3 ** 0.5 )/6
x2 = size/2
y2 = size *(3 ** 0.5 )/6
x3 = 0
y3 = -size *(3 ** 0.5 )/3

shape(t,x1,y1,x2,y2,depth)
shape(t,x2,y2,x3,y3,depth)
shape(t,x3,y3,x1,y1,depth)

turtle.done()
