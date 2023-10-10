import turtle 


bia = turtle.Turtle()


def desenhe_flor():
    for n in range(6):
        for n in range(8):
            bia.forward(20)
            bia.right(30)
        bia.right(60)    


for _ in range(3):
    desenhe_flor()
    bia.penup()
    bia.forward(150)
    bia.pendown()