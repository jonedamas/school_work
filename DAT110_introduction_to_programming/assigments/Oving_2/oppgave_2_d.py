import turtle


def mangekant(kanter, farge):
    turtle.fillcolor(farge)
    turtle.begin_fill()

    for i in range(int(kanter)):
        turtle.forward(15 ** 2 / int(kanter))
        turtle.left(360 / int(kanter))
    turtle.end_fill()
