# This program draws a star in turtle graphics based on input of number of lines
# and line length.

import turtle

lines = int(input('Enter number of lines: '))
distance = float(input('Enter line distance: '))
angle = 360 / lines

for i in range(int(lines)):
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(angle)

turtle.done()
