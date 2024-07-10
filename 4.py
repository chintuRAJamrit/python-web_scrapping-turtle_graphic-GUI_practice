#Develop a program using Turtle graphic, write a program that asks the user for the number of
#sides, the length of the side, the colour, and the �ll colour of a regular polygon. The program
#should draw the polygon and then �ll it in.

import turtle

sides = int(input("enter the number of side fo the polygon : "))
length = int(input("enter the length of each of sides : "))
pencol = input("enter the pen color : ")
fillcol = input("enter the color to fill : ")

angle = 360/sides
t = turtle.Turtle()
t.color(pencol)
t.fillcolor(fillcol)

t.begin_fill()
for i in range (sides):
    t.forward(length)
    t.right(angle)
t.end_fill()

turtle.done()
