import turtle


bia = turtle.Turtle()


def desenhe_quadrado():
    for _ in range(4):
        bia.forward(25)
        bia.right(90)


def pular(pixels):
    bia.penup()
    bia.forward(pixels)
    bia.pendown()


for _ in range(4):
    for _ in range(2):
        for _ in range(4):
            desenhe_quadrado()
            pular(50)
        bia.right(180)
    bia.left(90)
    pular(50)
    bia.right(90)
