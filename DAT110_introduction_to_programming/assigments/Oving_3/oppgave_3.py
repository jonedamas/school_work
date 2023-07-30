import turtle

turtle.pensize(3)
index = 0

with open("tegne_eksempel_2.txt", "r") as fil_1:
    for line in fil_1:
        try:
            line_value = float(line)
            if index == 0:
                turtle.right(line_value)
                index = 1
            else:
                if float(line) < 0:
                    turtle.penup()
                    turtle.forward(abs(line_value))
                    turtle.pendown()
                else:
                    turtle.forward(line_value)
                index = 0

        except ValueError:
            turtle.pencolor(line.strip())


turtle.done()
