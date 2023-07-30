# This program draws stars in turtle graphics based on input of number of lines
# and line length, and number of stars.

import turtle

lines = int(input('Enter number of lines: '))
distance = float(input('Enter line distance: '))
stars = int(input('Enter number of stars: '))
angle = 360 / lines

turtle.penup()
turtle.backward(350)
turtle.pendown()

for i in range(stars):
    for j in range(int(lines)):
        turtle.forward(50)
        turtle.backward(50)
        turtle.left(angle)
    turtle.penup()
    turtle.forward(distance * 3)
    turtle.pendown()

turtle.done()
