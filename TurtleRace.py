from turtle import *
from random import randit

def Race():

    speed(0)
    penup()
    goto(-140, 140)

    for step in range(15):
        write(step, align='center')
        right(90)
        for num in range(8):
            penup()
            forward(10)
            pendown()
            forward(10)
        penup()
        backward(160)
        left(90)
        forward(20)

    ada = Turtle()
    ada.color('red')
    ada.shape('turtle')

    ada.penup()
    ada.goto(-160, 100)
    ada.pendown()

    bob = Turtle()
    bob.color('blue')
    bob.shape('turtle')

    bob.penup()
    bob.goto(-160, 70)
    bob.pendown()

