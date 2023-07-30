from Oving_2 import oppgave_2_d
import turtle

turtle.penup()
turtle.backward(300)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.pendown()

for i in range(1, 21):
    if i % 2 == 0:
        oppgave_2_d.mangekant(6, 'red')
    else:
        oppgave_2_d.mangekant(6, 'blue')

    if i % 5 == 0:
        turtle.penup()
        turtle.backward(625)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)

    turtle.penup()
    turtle.forward(125)
    turtle.pendown()


turtle.done()
